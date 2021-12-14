import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from static.routers import advanced, analysis, enrichment, edit
from internal.tasks import document_enrichment, document_annotation

app = FastAPI()
templates = Jinja2Templates(directory="static/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Looks up other modules for  the creation of new pages. 
app.include_router(advanced.router)
app.include_router(analysis.router)
app.include_router(enrichment.router)
app.include_router(edit.router)
app.include_router(document_enrichment.router)
app.include_router(document_annotation.router)


@app.get("/", response_class=HTMLResponse)
def get_start_page(request: Request):
    """ Creates the page for the starting page. """
    return templates.TemplateResponse("start.html", {"request": request, })


@app.get("/about", response_class=HTMLResponse)
def get_about(request: Request):
    """ Creates the page for the starting page. """
    return templates.TemplateResponse("about.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run("main:app")
