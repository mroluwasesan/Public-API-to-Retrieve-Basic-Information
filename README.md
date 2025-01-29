# HNG Stage 0 API (FastAPI)

A FastAPI-based API for the HNG Stage 0 task.






  # HNG Stage 0 API

A FastAPI-based public API that returns basic information including a registered email address, current UTC datetime, and GitHub repository URL. Built for the HNG internship Stage 0 task.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Local Development
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hng-stage0-api.git
   cd hng-stage0-api

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

3.  **Run the API locally**:
    ```bash
    uvicorn main:app --reload

4.  **Test the API**:
    Open http://<IP>:8000 in your browser or use:
    ```bash
    curl http://<IP>:8000

## API Documentation
- **Endpoint**: `GET /`
- **Response**:
  ```json
  {
    "email": "your-email@example.com",
    "current_datetime": "2024-05-15T12:34:56.789Z",
    "github_url": "https://github.com/yourusername/Public-API-to-Retrieve-Basic-Information" 
  }


**Fields**:

  email: The registered HNG Slack workspace email address.

  current_datetime: Current UTC datetime in ISO 8601 format.

  github_url: URL of this project's GitHub repository.


**Example Usage**
    ```bash
    # Using curl
    curl https://your-deployed-url.xyz/

## 🔗 Backlinks
    ```bash
    .
    ├── main.py             # FastAPI application code
    ├── requirements.txt    # Dependencies
    └── README.md           # This documentation