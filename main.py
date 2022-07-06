from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-count")
def getC():
    f = open("count.txt", "r")
    c = int(f.read())
    f.close()
    return c

@app.get("/increment-count")
def incrementC():
    f = open("count.txt", "r")
    c = int(f.read()) + 1
    f.close()
    f = open("count.txt", "w")
    f.write(str(c))
    f.close()
    return c
