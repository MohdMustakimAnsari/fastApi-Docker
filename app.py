from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/about')
def about(name:str):
    return{f'your name is :{name}'}


if __name__=='__main__':
    uvicorn.run(app)