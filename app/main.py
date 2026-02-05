from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "CI/CD FastAPI test running successfully!!!!!!!"}


@app.get("/health")
def health():
    return {"status": "ok"}
  
   