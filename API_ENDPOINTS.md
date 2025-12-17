# 🚀 Web Tool Platform API - Endpoints Documentation

## Base URL
```
http://127.0.0.1:8000
```

---

## 📋 Overview Endpoints

### 1. Root - API Information
```http
GET /
```
**Response:**
```json
{
    "name": "Web Tool Platform API",
    "version": "2.0.0",
    "status": "running",
    "docs": "/docs",
    "health": "/health"
}
```

### 2. Health Check
```http
GET /health
```
**Response:**
```json
{
    "status": "healthy"
}
```

### 3. Interactive API Documentation
```http
GET /docs
```
Opens Swagger UI for interactive API testing.

```http
GET /redoc
```
Opens ReDoc for API documentation.

---

## 🛠️ Tool Discovery Endpoints

### 4. List All Available Tools
```http
GET /api/v1/agents/list
```
**Response:**
```json
{
    "agents": [
        "story-generator",
        "poem-generator",
        // ... 34 AI agents
    ],
    "tools": [
        "hex-to-rgb",
        "code-beautifier",
        "domain-checker",
        "plagiarism-checker"
    ],
    "all": [
        // Combined list of 38 tools
    ]
}
```

### 5. List AI Agents Only
```http
GET /api/v1/agents/agents
```
**Response:** Array of 34 AI agent slugs

### 6. List Deterministic Tools Only
```http
GET /api/v1/agents/tools
```
**Response:** Array of 4 deterministic tool slugs

---

## ⚡ Tool Execution Endpoint

### 7. Process Any Tool (POST)
```http
POST /api/v1/agents/process/{slug}
```

**URL Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `slug` | string | Tool identifier (e.g., `story-generator`, `hex-to-rgb`) |

**Request Body:**
```json
{
    "prompt": "Your input text here",
    "settings": {
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 1000
    },
    "user_context": {
        "key": "value"
    }
}
```

**Response (Success):**
```json
{
    "status": "success",
    "agent_id": "uuid-string",
    "content": "Generated output text",
    "usage": {
        "prompt_tokens": 50,
        "completion_tokens": 100,
        "total_tokens": 150
    }
}
```

**Response (Error):**
```json
{
    "detail": "Error message"
}
```

---

## 🎨 AI Agents List (34 Total)

### Creative Agents
| Slug | Description |
|------|-------------|
| `story-generator` | Generate captivating stories |
| `ai-story-generator` | Same as story-generator |
| `poem-generator` | Create beautiful poems |
| `backstory-generator` | Create character backstories |
| `slogan-generator` | Generate catchy slogans |
| `caption-generator` | Write social media captions |
| `message-generator` | Draft various messages |
| `reply-generator` | Compose replies to messages |
| `business-name-generator` | Generate business names |
| `book-title-generator` | Create book titles |

### Writing & Content Agents
| Slug | Description |
|------|-------------|
| `cover-letter-generator` | Write professional cover letters |
| `email-writer` | Compose professional emails |
| `essay-writer` | Write structured essays |
| `article-rewriter` | Rewrite articles |
| `ai-content-improver` | Same as article-rewriter |
| `review-generator` | Generate product/service reviews |
| `paragraph-generator` | Write coherent paragraphs |
| `paragraph-expander` | Expand short paragraphs |
| `sentence-expander` | Expand simple sentences |
| `humanize-ai` | Make AI text sound human |
| `conclusion-writer` | Write strong conclusions |
| `ai-prompt-generator` | Generate AI prompts |

### Precise & Structural Agents
| Slug | Description |
|------|-------------|
| `outline-generator` | Create structured outlines |
| `answer-generator` | Provide direct answers |
| `thesis-statement-generator` | Draft thesis statements |
| `faq-generator` | Generate FAQ lists |
| `acronym-generator` | Create meaningful acronyms |
| `meta-description-generator` | Write SEO meta descriptions |
| `meta-tag-generator` | Same as meta-description-generator |
| `small-text-generator` | Generate short text snippets |
| `spell-checker` | Check and fix spelling |
| `grammar-checker` | Check and fix grammar |
| `sentence-shortener` | Condense long sentences |
| `sentence-generator` | Generate sentences from keywords |

---

## 🔧 Deterministic Tools (4 Total)

| Slug | Description | Example Input |
|------|-------------|---------------|
| `hex-to-rgb` | Convert hex color to RGB | `#FF5733` |
| `code-beautifier` | Format/beautify code | Any code string |
| `domain-checker` | Check domain availability (mock) | `example-domain` |
| `plagiarism-checker` | Check plagiarism score (mock) | Any text |

---

## 📝 Usage Examples

### Example 1: Hex to RGB Conversion
```bash
# Request
POST /api/v1/agents/process/hex-to-rgb
Content-Type: application/json

{
    "prompt": "#FF5733"
}

# Response
{
    "status": "success",
    "agent_id": "abc-123-uuid",
    "content": "rgb(255, 87, 51)"
}
```

### Example 2: Generate a Story
```bash
# Request
POST /api/v1/agents/process/story-generator
Content-Type: application/json

{
    "prompt": "Write a short story about a dragon who loves to bake cookies",
    "settings": {
        "temperature": 0.9
    }
}

# Response
{
    "status": "success",
    "agent_id": "xyz-456-uuid",
    "content": "In the misty valleys of Mount Ember, there lived a peculiar dragon named Cinnamon..."
}
```

### Example 3: Grammar Check
```bash
# Request
POST /api/v1/agents/process/grammar-checker
Content-Type: application/json

{
    "prompt": "Their going to the store tommorow to buy some grocerys."
}

# Response
{
    "status": "success",
    "agent_id": "def-789-uuid",
    "content": "They're going to the store tomorrow to buy some groceries."
}
```

---

## 🔐 Configuration

### Environment Variables (.env)
```env
# Gemini API
GEMINI_API_KEY=AIzaSyCebWBWt6Ct_iNAes8k6bKSV507POrWz9w
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
GEMINI_MODEL=gemini-2.5-flash

# Server
HOST=127.0.0.1
PORT=8000
DEBUG=true

# CORS
CORS_ORIGINS=["http://localhost:3000","http://127.0.0.1:3000"]
```

---

## 🚀 Running the Server

```bash
# Using uvicorn directly
python -m uvicorn main:app --reload

# Using run script
python run.py
```

---

## ⚠️ Error Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 404 | Tool not found |
| 422 | Validation error (invalid request body) |
| 500 | Internal server error (AI execution failed) |

---

## 📊 Testing with PowerShell

```powershell
# Test root endpoint
Invoke-RestMethod -Uri "http://127.0.0.1:8000/" -Method Get

# Test tool listing
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/agents/list" -Method Get

# Test hex to RGB
$body = @{prompt="#FF5733"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/agents/process/hex-to-rgb" -Method Post -Body $body -ContentType "application/json"

# Test AI agent
$body = @{prompt="Write a haiku about coding"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/agents/process/poem-generator" -Method Post -Body $body -ContentType "application/json"
```

---

## 📁 Project Structure
```
backend/
├── main.py                 # Main entry point
├── run.py                  # Server runner script
├── pyproject.toml          # Dependencies
├── .env                    # Environment variables
├── .env.example            # Example environment config
├── app/
│   ├── __init__.py
│   ├── main.py             # App factory
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py   # API v1 router
│   │       └── agents/
│   │           ├── __init__.py
│   │           ├── registry.py  # Tool/Agent registry
│   │           └── router.py    # Agent endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py       # Settings & Gemini config
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── base.py         # Pydantic models
│   └── services/
│       ├── __init__.py
│       └── agent_executor.py  # AI agent execution
├── Agents/
│   └── generation_agent.py  # AI agent definitions
├── config/
│   └── gemini_config.py     # Gemini client config
└── core/
    └── tools.py             # Deterministic tools
```
