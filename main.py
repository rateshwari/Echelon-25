from fastapi import FastAPI
from app.routes import auth, dashboard, career

app = FastAPI(title="AI Learning Platform")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(career.router, prefix="/career", tags=["Career Paths"])

@app.get("/")
def root():
    return {"message": "Welcome to the AI-powered backend!"}
