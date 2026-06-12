from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()


@app.get("/")
def root():
    """Root endpoint — shown when you visit just '/'."""
    return {"message": "Hello, FastAPI!"}


@app.get("/hello")
def hello():
    """Says hello back."""
    return {"greeting": "Hello, World!"}


@app.get("/hello/{name}")
def hello_name(name: str):
    """Hello with a personalized name from the URL."""
    return {"greeting": f"Hello, {name}!"}