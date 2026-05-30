import os
import json
import httpx
from dotenv import load_dotenv
from services.logger import get_logger

load_dotenv()

logger = get_logger("supabase")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
RPC_URL = f"{SUPABASE_URL}/rest/v1/rpc/iniciar_sesion"

class LoginError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(mensaje)

async def login(correo: str, contrasena: str) -> dict:
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        logger.error("Configuración de Supabase incompleta: URL=%s, KEY=%s",
                      bool(SUPABASE_URL), bool(SUPABASE_ANON_KEY))
        raise LoginError("Error de configuración del servidor")

    logger.info("Intento de login: correo=%s", correo)

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                RPC_URL,
                json={"p_correo": correo, "p_contrasena": contrasena},
                headers={
                    "apikey": SUPABASE_ANON_KEY,
                    "Content-Type": "application/json",
                },
                timeout=15,
            )
        logger.debug("Respuesta HTTP: status=%s", resp.status_code)
    except httpx.TimeoutException:
        logger.warning("Timeout en login para %s", correo)
        raise LoginError("El servidor no respondió a tiempo. Verifica tu conexión")
    except httpx.NetworkError:
        logger.warning("Error de red en login para %s", correo)
        raise LoginError("Error de conexión con el servidor. Verifica tu internet")
    except Exception as exc:
        logger.error("Error inesperado en login para %s: %s", correo, exc)
        raise LoginError("Ocurrió un error inesperado. Intenta de nuevo")

    try:
        data = resp.json()
    except (json.JSONDecodeError, ValueError) as exc:
        logger.error("Respuesta no JSON del servidor: %s", exc)
        raise LoginError("Respuesta inválida del servidor")

    if not isinstance(data, dict):
        logger.error("Respuesta no es un dict: %s", type(data).__name__)
        raise LoginError("Respuesta inválida del servidor")

    if not data.get("success", False):
        error_msg = data.get("error", "Credenciales inválidas")
        logger.warning("Login fallido para %s: %s", correo, error_msg)
        raise LoginError(error_msg)

    if data.get("rol") != "PADRE":
        logger.warning("Acceso denegado: rol=%s para %s (se espera PADRE)",
                        data.get("rol"), correo)
        raise LoginError("Solo los padres de familia pueden acceder a esta aplicación")

    logger.info("Login exitoso: id_usuario=%s rol=%s nombre=%s",
                data.get("id_usuario"), data.get("rol"), data.get("nombre"))
    return data
