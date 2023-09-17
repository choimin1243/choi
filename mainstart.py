from fastapi import FastAPI
from main import appends
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from package import pack
import models
from database import engine
from fastapi import FastAPI, Form, Request, Depends
import time
import keyboard

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

templates = Jinja2Templates(directory="templates")
templates.env.globals.update(enumerate=enumerate)

app.include_router(appends, prefix="/api")
app.include_router(pack, prefix="/package")
models.Base.metadata.create_all(bind=engine)

@app.get("/pack/")
def 누른_작동버튼():
    time.sleep(3)
    keyboard.write('Hello, World!')

    keyboard.press_and_release('tab')

    # "Hello, World!"를 입력
    keyboard.write('Hello, World!')


@app.get("/")
async def render_upload_form(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
