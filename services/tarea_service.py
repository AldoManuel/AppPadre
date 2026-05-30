import os
import json
import httpx
from dotenv import load_dotenv
from services.logger import get_logger

load_dotenv()

logger = get_logger("tarea")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
RPC_URL = f"{SUPABASE_URL}/rest/v1/rpc/obtener_tareas"


class TareaError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(mensaje)


async def get_tareas(id_alumno: str) -> list:
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        logger.error("Configuración de Supabase incompleta")
        raise TareaError("Error de configuración del servidor")

    logger.info("Obteniendo tareas para id_alumno=%s", id_alumno)

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                RPC_URL,
                json={"p_id_alumno": id_alumno},
                headers={
                    "apikey": SUPABASE_ANON_KEY,
                    "Content-Type": "application/json",
                },
                timeout=15,
            )
        logger.debug("Respuesta tareas: status=%s", resp.status_code)
    except httpx.TimeoutException:
        logger.warning("Timeout obteniendo tareas para %s", id_alumno)
        raise TareaError("El servidor no respondió a tiempo")
    except httpx.NetworkError:
        logger.warning("Error de red obteniendo tareas para %s", id_alumno)
        raise TareaError("Error de conexión con el servidor")
    except Exception as exc:
        logger.error("Error inesperado en tareas: %s", exc)
        raise TareaError("Ocurrió un error inesperado")

    try:
        data = resp.json()
    except (json.JSONDecodeError, ValueError):
        logger.error("Respuesta no JSON del servidor")
        raise TareaError("Respuesta inválida del servidor")

    if not isinstance(data, list):
        logger.error("Respuesta no es una lista: %s", type(data).__name__)
        raise TareaError("Respuesta inválida del servidor")

    logger.info("Tareas obtenidas: %s", len(data))
    return data
