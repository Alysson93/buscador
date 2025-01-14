from fastapi import FastAPI

from routes import distribuidores, revendas

app = FastAPI()
app.include_router(distribuidores.router)
app.include_router(revendas.router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
