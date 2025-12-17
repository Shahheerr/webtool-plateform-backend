# 🚀 Web Tool Platform - FastAPI Backend

A powerful AI-powered content generation platform with 34 AI agents and 4 deterministic tools.

## ✨ Features

- **34 AI Agents** - Story generation, email writing, grammar checking, and more
- **4 Deterministic Tools** - Hex-to-RGB, code beautifier, domain checker, plagiarism checker
- **FastAPI** - High-performance async API framework
- **Gemini AI** - Powered by Google's Gemini 2.5 Flash model
- **Modular Architecture** - Clean separation of concerns
- **CORS Enabled** - Ready for frontend integration

## 📋 Quick Start

### 1. Install Dependencies
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your Gemini API key
# Get your key from: https://aistudio.google.com/app/apikey
```

### 3. Run the Server
```bash
# Using uvicorn
python -m uvicorn main:app --reload

# Or using the run script
python run.py
```

### 4. Test the API
- **API Docs**: http://127.0.0.1:8000/docs
- **Health Check**: http://127.0.0.1:8000/health
- **List Tools**: http://127.0.0.1:8000/api/v1/agents/list

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI |
| GET | `/api/v1/agents/list` | List all tools |
| GET | `/api/v1/agents/agents` | List AI agents |
| GET | `/api/v1/agents/tools` | List deterministic tools |
| POST | `/api/v1/agents/process/{slug}` | Execute any tool |

## 📝 Usage Example

### Using PowerShell
```powershell
# Hex to RGB
$body = @{prompt="#FF5733"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/agents/process/hex-to-rgb" -Method Post -Body $body -ContentType "application/json"

# Generate a story
$body = @{prompt="Write a short story about a brave knight"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/agents/process/story-generator" -Method Post -Body $body -ContentType "application/json"
```

### Using curl/JavaScript
```javascript
// Fetch example
const response = await fetch('http://127.0.0.1:8000/api/v1/agents/process/story-generator', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        prompt: 'Write a haiku about programming',
        settings: { temperature: 0.9 }
    })
});
const data = await response.json();
console.log(data.content);
```

## 🎨 Available Tools

### AI Agents (34)
- **Creative**: story-generator, poem-generator, caption-generator, slogan-generator...
- **Writing**: email-writer, essay-writer, cover-letter-generator, article-rewriter...
- **Utility**: grammar-checker, spell-checker, sentence-shortener, faq-generator...

### Deterministic Tools (4)
- `hex-to-rgb` - Convert hex colors to RGB
- `code-beautifier` - Format code
- `domain-checker` - Check domain availability (mock)
- `plagiarism-checker` - Check plagiarism score (mock)

## 📁 Project Structure

```
backend/
├── main.py                 # Main entry point
├── run.py                  # Server runner
├── pyproject.toml          # Dependencies
├── .env                    # Environment config
├── API_ENDPOINTS.md        # Full API documentation
├── app/
│   ├── api/v1/agents/      # Agent endpoints & registry
│   ├── core/               # Settings & config
│   ├── schemas/            # Pydantic models
│   └── services/           # Agent executor
├── Agents/                 # AI agent definitions
├── config/                 # Gemini client config
└── core/                   # Deterministic tools
```

## ⚙️ Configuration

See `.env.example` for all configuration options:

```env
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.5-flash
HOST=127.0.0.1
PORT=8000
DEBUG=true
```

## 📖 Full Documentation

See [API_ENDPOINTS.md](./API_ENDPOINTS.md) for complete API documentation with examples.

## 🔧 Development

```bash
# Install dev dependencies
uv sync --dev

# Run tests
python test_agent.py
```

## 📄 License

MIT License
