import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
RPC_URL = f"{SUPABASE_URL}/rest/v1/rpc/iniciar_sesion"

class LoginError(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(mensaje)

async def login(correo: str, contrasena: str) -> dict:
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        raise LoginError("Error de configuración del servidor")

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
    except httpx.TimeoutException:
        raise LoginError("El servidor no respondió a tiempo. Verifica tu conexión")
    except httpx.NetworkError:
        raise LoginError("Error de conexión con el servidor. Verifica tu internet")
    except Exception:
        raise LoginError("Ocurrió un error inesperado. Intenta de nuevo")

    try:
        data = resp.json()
    except (json.JSONDecodeError, ValueError):
        raise LoginError("Respuesta inválida del servidor")

    if not isinstance(data, dict):
        raise LoginError("Respuesta inválida del servidor")

    if not data.get("success", False):
        error_msg = data.get("error", "Credenciales inválidas")
        raise LoginError(error_msg)

    return data
