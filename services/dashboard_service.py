import os
import json
import httpx
from dotenv import load_dotenv
from services.logger import get_logger

load_dotenv()

logger = get_logger("dashboard")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
RPC_URL = f"{SUPABASE_URL}/rest/v1/rpc/obtener_dashboard"


class DashboardError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(mensaje)


async def get_dashboard(id_padre: str) -> dict:
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        logger.error("Configuración de Supabase incompleta")
        raise DashboardError("Error de configuración del servidor")

    logger.info("Obteniendo dashboard para id_padre=%s", id_padre)

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                RPC_URL,
                json={"p_id_padre": id_padre},
                headers={
                    "apikey": SUPABASE_ANON_KEY,
                    "Content-Type": "application/json",
                },
                timeout=15,
            )
        logger.debug("Respuesta dashboard: status=%s", resp.status_code)
    except httpx.TimeoutException:
        logger.warning("Timeout obteniendo dashboard para %s", id_padre)
        raise DashboardError("El servidor no respondió a tiempo")
    except httpx.NetworkError:
        logger.warning("Error de red obteniendo dashboard para %s", id_padre)
        raise DashboardError("Error de conexión con el servidor")
    except Exception as exc:
        logger.error("Error inesperado en dashboard: %s", exc)
        raise DashboardError("Ocurrió un error inesperado")

    try:
        data = resp.json()
    except (json.JSONDecodeError, ValueError):
        logger.error("Respuesta no JSON del servidor")
        raise DashboardError("Respuesta inválida del servidor")

    if not isinstance(data, dict):
        logger.error("Respuesta no es un dict: %s", type(data).__name__)
        raise DashboardError("Respuesta inválida del servidor")

    logger.info("Dashboard obtenido: %s hijos, %s eventos",
                len(data.get("hijos", [])),
                len(data.get("proximos_eventos", [])))
    return data
