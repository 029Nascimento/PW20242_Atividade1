from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
import uvicorn

from models.produto_model import Produto
from repositories import produto_repo

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def paginaInicial(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro", response_class=HTMLResponse)
def cadastro(request: Request):
  return templates.TemplateResponse("cadastro.html", {"request": request})

@app.get("/cadastro_recebido")
def get_contato(request: Request):
  return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    nome: str = Form(...), 
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...), 
    categoria: str = Form(...)):
  
  produto = Produto(None, nome, descricao, estoque, preco, categoria)
  produto = produto_repo.inserir(produto)

  if produto:
    return RedirectResponse("/cadastro_recebido", 303)
  else: return RedirectResponse("/cadastro", 303)
  



if __name__ == "__main__":
  produto_repo.criar_tabela()
  uvicorn.run("main:app", port=8000, reload=True)