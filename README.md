# Public API basic info Retrieve 🚀

A sleek and lightweight FastAPI-based public API built for the HNG Internship Stage 0 task. This API returns essential details such as a registered email address, the current UTC datetime, and the GitHub repository URL.

---

## 📌 Features
- FastAPI-powered high-performance API.
- Provides structured JSON responses.
- Displays registered email, UTC datetime, and GitHub repository link.
- Well-documented and easy to deploy.

---

## 🛠 Setup Instructions

### ✅ Prerequisites
- Python **3.9+**
- pip (Python package manager)

### 🚀 Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hng-stage0-api.git
   cd hng-stage0-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API locally**:
   ```bash
   uvicorn main:app --reload
   ```

4. **Test the API**:
   - Open [http://localhost:8000](http://localhost:8000) in your browser.
   - Or use cURL:
     ```bash
     curl http://localhost:8000
     ```

---

## 📖 API Documentation

### **Endpoint:** `GET /`

#### **Response:**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2024-05-15T12:34:56.789Z",
  "github_url": "https://github.com/yourusername/Public-API-to-Retrieve-Basic-Information"
}
```

### **Response Fields:**
| Field | Description |
|--------|-------------|
| `email` | The registered HNG Slack workspace email address. |
| `current_datetime` | The current UTC datetime in ISO 8601 format. |
| `github_url` | The URL of this project's GitHub repository. |

---

## 📌 Example Usage

### Using `curl`
```bash
curl https://your-deployed-url.xyz/
```

---

## 🔗 Backlinks
- **To further explore career opportunities in DevOps and related fields, check out the following links**: [Hire Python Developers](https://hng.tech/hire/python-developers)

---

## 📁 Repository Structure
```bash
.
├── main.py             # FastAPI application code
├── requirements.txt    # Dependencies
└── README.md           # This documentation
```

---

🎯 Built with ❤️ for the HNG Internship Stage 0 Challenge! 🚀

