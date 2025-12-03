from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(docs_url=None, redoc_url=None)

HTML_PAGE = """
<!doctype html>
<html>
<head><meta charset="utf-8"/><title>Welcome</title>
<style>
  body{background:#222;color:#fff;font-family:Arial,Helvetica,sans-serif;padding:40px}
  h1{font-size:56px;margin:6px 0}
  p.lead{color:#cfcfcf;margin:0 0 40px 0;font-size:16px}
  .rocket{width:220px;display:block;margin:40px auto;transform:rotate(-20deg)}
  h2{font-size:40px;margin-top:80px}
  .btn{display:inline-block;margin:10px;padding:10px 14px;background:#2b8fd6;color:#fff;border-radius:6px;text-decoration:none}
</style>
</head>
<body>
  <h1>Welcome to the webpage, Sreeja!</h1>
  <p class="lead">Here's a quote for you: "The only way to do great work is to love what you do." - Steve Jobs</p>
  <img class="rocket" src="https://cdn-icons-png.flaticon.com/512/814/814513.png" alt="rocket"/>
  <h2>Containerized Python API</h2>
  <p style="color:#cfcfcf">This is a containerized application that exposes a JSON API using FastAPI.</p>
  <a class="btn" href="/docs">Try it out</a>
  <a class="btn" href="#" onclick="return false;" style="background:#3b3b3b;margin-left:8px">Project source</a>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_PAGE
