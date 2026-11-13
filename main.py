from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from database import get_db_connection, add_data, get_data
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
    return templates.TemplateResponse(request=request, name="view.html", context={"names":make_list_of_names()})




@app.post("/add/send_data")
def add_data_to_database(name: str = Form(...), university: str = Form(...)):
    add_data(name, university)

    return RedirectResponse(
        url="/add",
        status_code=303
    )

data = [{'id': 1, 'name': 'Peter Parker', 'University': 'Queens Colleg3e'}, 
        {'id': 2, 'name': 'Gary Houston', 'University': 'University of Newcastle'}]



def make_list_of_names():
    data = get_data()
    names = []
    for _, dict_data in enumerate(data):
        print(dict_data)
        names.append(dict_data["name"])
    return(names)

make_list_of_names()