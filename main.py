from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (adjust for production)
    allow_methods=["GET"],
)

@app.get("/")
async def get_info():
    return {
        "email": "mr.oluwasesan@gmail.com",  # Replace with your email
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/mroluwasesan/Public-API-to-Retrieve-Basic-Information"  # Replace with your repo,
        
    }