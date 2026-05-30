import os
import json
import httpx
from dotenv import load_dotenv
from services.logger import get_logger

load_dotenv()

logger = get_logger("registro")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
RPC_URL = f"{SUPABASE_URL}/rest/v1/rpc/registrar_hijo"


class RegistroError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(mensaje)


async def registrar_hijo(
    id_padre: str,
    nombre: str,
    apellido_paterno: str,
    apellido_materno: str | None = None,
    correo: str | None = None,
    id_grupo: int = 1,
    parentesco: str = "TUTOR",
) -> dict:
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        logger.error("Configuración de Supabase incompleta")
        raise RegistroError("Error de configuración del servidor")

    logger.info("Registrando hijo para padre=%s, nombre=%s", id_padre, nombre)

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                RPC_URL,
                json={
                    "p_id_padre": id_padre,
                    "p_nombre": nombre,
                    "p_apellido_paterno": apellido_paterno,
                    "p_apellido_materno": apellido_materno,
                    "p_correo": correo,
                    "p_id_grupo": id_grupo,
                    "p_parentesco": parentesco,
                },
                headers={
                    "apikey": SUPABASE_ANON_KEY,
                    "Content-Type": "application/json",
                },
                timeout=15,
            )
        logger.debug("Respuesta registro: status=%s", resp.status_code)
    except httpx.TimeoutException:
        logger.warning("Timeout registrando hijo para %s", id_padre)
        raise RegistroError("El servidor no respondió a tiempo")
    except httpx.NetworkError:
        logger.warning("Error de red registrando hijo para %s", id_padre)
        raise RegistroError("Error de conexión con el servidor")
    except Exception as exc:
        logger.error("Error inesperado en registro: %s", exc)
        raise RegistroError("Ocurrió un error inesperado")

    try:
        data = resp.json()
    except (json.JSONDecodeError, ValueError):
        logger.error("Respuesta no JSON del servidor")
        raise RegistroError("Respuesta inválida del servidor")

    if not isinstance(data, dict):
        logger.error("Respuesta no es un dict: %s", type(data).__name__)
        raise RegistroError("Respuesta inválida del servidor")

    if not data.get("success", False):
        error_msg = data.get("error", "Error desconocido")
        logger.warning("Registro fallido: %s", error_msg)
        raise RegistroError(error_msg)

    logger.info("Hijo registrado exitosamente: id=%s", data.get("id_alumno"))
    return data
