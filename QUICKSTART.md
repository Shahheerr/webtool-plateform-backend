# Quick Start Guide - Web Tool Platform Backend

## 🎯 Overview

You now have a **production-ready, modular FastAPI backend** with 31 AI agents, each with its own dedicated endpoint. This guide will help you get started quickly.

## ⚡ 5-Minute Quick Start

### Step 1: Get Your API Key (CRITICAL)

The current API key has been leaked and disabled. You **must** get a new one:

1. Visit: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key

### Step 2: Update Environment Variables

Open `.env` and replace the API key:

```env
GEMINI_API_KEY=YOUR_NEW_API_KEY_HERE
```

### Step 3: Start the Server

```bash
uv run python run.py
```

✅ Server should start at: http://127.0.0.1:8000

### Step 4: Test It

Open your browser:
- **API Docs**: http://127.0.0.1:8000/docs
- **Health Check**: http://127.0.0.1:8000/health

---

## 🧪 Testing Your First Agent

### Using Browser (Swagger UI)

1. Go to http://127.0.0.1:8000/docs
2. Find **POST /api/v1/agents/story-generator**
3. Click "Try it out"
4. Enter request body:
   ```json
   {
     "prompt": "Write a 2-sentence story about a robot"
   }
   ```
5. Click "Execute"
6. See the AI-generated story in the response!

### Using PowerShell

```powershell
$body = @{
    prompt = "Write a haiku about programming"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/agents/poem-generator" `
    -Method POST `
    -Body $body `
    -ContentType "application/json"
```

### Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/agents/email-writer" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a thank you email to my team"}'
```

---

## 📚 Available Endpoints

### Discovery Endpoints

```http
GET /                      # API info
GET /health                # Health check
GET /api/v1/agents/        # List all agents
GET /docs                  # Interactive API docs
```

### Agent Endpoints (31 total)

All follow this pattern:
```http
POST /api/v1/agents/{agent-slug}
```

**Most Popular Agents:**

| Endpoint | Purpose | Example Prompt |
|----------|---------|----------------|
| `/story-generator` | Creative stories | "Write a sci-fi short story" |
| `/email-writer` | Professional emails | "Write a meeting invitation" |
| `/poem-generator` | Poetry | "Write a haiku about nature" |
| `/essay-writer` | Academic essays | "Essay about climate change" |
| `/grammar-checker` | Fix grammar | "Their going to the store" |
| `/slogan-generator` | Brand slogans | "Tech startup selling AI tools" |
| `/cover-letter-generator` | Job applications | "Software engineer at Google" |

Full list in `README.md` → 31 agents + 4 non-AI tools

---

## 🎨 Request Examples

### Basic Request

```json
{
  "prompt": "Your request here"
}
```

### With Settings Override

```json
{
  "prompt": "Write a creative story",
  "settings": {
    "temperature": 0.9,
    "top_p": 0.95,
    "max_tokens": 500
  }
}
```

### With Context

```json
{
  "prompt": "Write a product description",
  "user_context": {
    "product_name": "SmartWidget",
    "target_audience": "developers",
    "tone": "professional"
  }
}
```

---

## ✅ Response Format

### Success Response

```json
{
  "status": "success",
  "agent_id": "550e8400-e29b-41d4-a716-446655440000",
  "content": "The AI-generated content goes here...",
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 150,
    "total_tokens": 160
  }
}
```

### Error Response

```json
{
  "status": "error",
  "message": "Descriptive error message",
  "agent_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

---

## 🔗 Next.js Integration

### Step 1: Create API Route

In your Next.js project: `app/api/tools/[slug]/route.ts`

```typescript
import { NextRequest, NextResponse } from 'next/server';

const BACKEND_URL = process.env.BACKEND_URL || 'http://127.0.0.1:8000';

export async function POST(
  request: NextRequest,
  { params }: { params: { slug: string } }
) {
  const { slug } = params;
  const body = await request.json();

  const response = await fetch(
    `${BACKEND_URL}/api/v1/agents/${slug}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    }
  );

  const data = await response.json();
  return NextResponse.json(data, { status: response.status });
}
```

### Step 2: Set Environment Variable

`.env.local`:
```env
BACKEND_URL=http://127.0.0.1:8000
```

### Step 3: Use in Components

```typescript
// In your React component
const generateStory = async () => {
  const response = await fetch('/api/tools/story-generator', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      prompt: userInput
    })
  });

  const result = await response.json();
  
  if (result.status === 'success') {
    setOutput(result.content);
  } else {
    setError(result.message);
  }
};
```

---

## 🎯 Agent Categories

### 🎨 Creative (9 agents)
High temperature (0.9) for imaginative content
- story-generator
- poem-generator
- backstory-generator
- slogan-generator
- caption-generator
- message-generator
- reply-generator
- business-name-generator
- book-title-generator

### ✍️ Writing (11 agents)
Balanced temperature (0.5) for quality content
- cover-letter-generator
- email-writer
- essay-writer
- article-rewriter
- review-generator
- paragraph-generator
- paragraph-expander
- sentence-expander
- humanize-ai
- conclusion-writer
- ai-prompt-generator

### 🎯 Precise (11 agents)
Low temperature (0.1) for accuracy
- outline-generator
- answer-generator
- thesis-statement-generator
- faq-generator
- acronym-generator
- meta-description-generator
- small-text-generator
- spell-checker
- grammar-checker
- sentence-shortener
- sentence-generator

---

## 🔧 Advanced Features

### 1. Streaming (for long responses)

```http
POST /api/v1/agents/{slug}/stream
```

Returns Server-Sent Events for progressive text display.

```javascript
const eventSource = new EventSource(
  '/api/v1/agents/story-generator/stream'
);

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  if (data.type === 'chunk') {
    appendText(data.content);
  } else if (data.type === 'complete') {
    eventSource.close();
  }
};
```

### 2. Custom Model Settings

Override default settings per request:

```json
{
  "prompt": "Write something creative",
  "settings": {
    "temperature": 1.5,    // Higher = more creative
    "top_p": 0.9,          // Nucleus sampling
    "max_tokens": 1000     // Limit response length
  }
}
```

### 3. Usage Tracking

Every response includes token usage:

```json
{
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 150,
    "total_tokens": 165
  }
}
```

Use this for:
- Cost tracking
- Performance monitoring
- Rate limiting

---

## 🐛 Troubleshooting

### Server Won't Start

```bash
# Check Python version
python --version  # Should be 3.13+

# Reinstall dependencies
uv sync

# Check .env file exists
cat .env
```

### API Key Error

```
Error: Your API key was reported as leaked
```

**Solution:** Get a new API key from Google AI Studio

### CORS Error from Frontend

Update `app/core/config.py`:

```python
CORS_ORIGINS: list[str] = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://your-domain.com",  # Add your domain
]
```

### Agent Returns Error

Check if agent slug is correct:
```bash
# List all available agents
curl http://127.0.0.1:8000/api/v1/agents/
```

---

## 📊 Performance Tips

1. **Use Caching**: Agents are cached after first use
2. **Enable GZip**: Automatic for responses > 500 bytes
3. **Monitor Usage**: Check `X-Response-Time` header
4. **Async All the Way**: All operations are async
5. **Connection Pooling**: HTTP connections are reused

---

## 🚀 Deployment Checklist

- [ ] Get production API key
- [ ] Set `DEBUG=false` in `.env`
- [ ] Configure production CORS origins
- [ ] Add rate limiting middleware
- [ ] Set up logging/monitoring
- [ ] Use production ASGI server (gunicorn)
- [ ] Enable HTTPS
- [ ] Set up health check monitoring

---

## 📞 Support

- **API Docs**: http://127.0.0.1:8000/docs
- **GitHub Issues**: [Your repo]
- **Documentation**: See `README.md`

---

## 🎉 You're Ready!

Your modular, production-ready FastAPI backend is complete. Just add your API key and start building amazing AI-powered applications!

**Happy Coding! 🚀**
