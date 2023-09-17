import os
import keyboard
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src import settings
from src.shortcuts import Shortcuts

app = FastAPI(title="VLC remote control")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="src/templates")

shortcuts = Shortcuts(settings.DB)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/action/{command}")
def action(command: str):
    os.system(shortcuts.get("open_vlc"))
    action = shortcuts.get(command)
    keyboard.send(action)


@app.get("/config", response_class=HTMLResponse)
async def config(request: Request):
    return templates.TemplateResponse(
        "config.html", {"request": request, "shortcuts": shortcuts.get_all()}
    )


@app.post("/config", response_class=HTMLResponse)
async def update_config(
    request: Request,
):
    form = await request.form()

    data = dict(form)
    save = data.pop("save", None)
    reset = data.pop("reset", None)
    message = None

    if save is not None:
        shortcuts.update(data)
        message = "Configurations updated successfully"
    elif reset is not None:
        shortcuts.update(settings.DEFAULT_SHORTCUTS)
        message = "Configuration reset successfully"

    return templates.TemplateResponse(
        "config.html",
        {
            "request": request,
            "shortcuts": shortcuts.get_all(),
            "message": message,
        },
    )
