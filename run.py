import socket
import uvicorn
from src import settings

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    print("\n\n", f"Ensure your other device is on the same network and go to: http://{ip}:{settings.PORT}", "\n\n")
    uvicorn.run("src.app:app", host="0.0.0.0", port=settings.PORT, reload=True)
