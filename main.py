from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from database import get_db_connection
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="template")

@app.get("/", response_class=HTMLResponse)
async def show_index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/add", response_class=HTMLResponse)
async def show_index(request: Request):
    return templates.TemplateResponse(request=request, name="add.html")

@app.get("/view", response_class=HTMLResponse)
async def show_index(request: Request):
    return templates.TemplateResponse(request=request, name="view.html")




@app.post("/add/send_data")
def add_data_to_database(name: str = Form(...), university: str = Form(...)):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Survey (name, University) VALUES (?, ?)",
        (name, university)
    )
    connection.commit()
    connection.close()

    return RedirectResponse(
        url="/add",
        status_code=303
    )


