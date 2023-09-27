import socket
import uvicorn
from src import settings
import qrcode


def main():
    ip = socket.gethostbyname(socket.gethostname())
    url = f"http://{ip}:{settings.PORT}"
    qr = qrcode.QRCode()
    qr.add_data(url)
    print(
        "\n\n",
        f"Ensure your other device is on the same network and go to {url} or scan this qr code:",
        "\n\n",
    )
    qr.print_ascii()
    uvicorn.run("src.app:app", host="0.0.0.0", port=settings.PORT, reload=True)


if __name__ == "__main__":
    main()
