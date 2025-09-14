from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定（Astroからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World from FastAPI!"}

@app.get("/api/hello")
def hello():
    return {"greeting": "Hello from FastAPI API!"}

@app.get("/helloworld")
def helloworld():
    return {"message": "Hello, World from /helloworld! By Astoro"}