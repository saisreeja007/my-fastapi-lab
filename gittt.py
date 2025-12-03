# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(docs_url=None, redoc_url=None)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Portfolio - Kura Sai Sreeja</title>
  <style>
    /* Simple CSS to match the sample layout */
    :root{--bg:#faf7f6;--nav:#f0e9e7;--text:#0b0b0b}
    html,body{height:100%;margin:0;font-family: 'Helvetica Neue', Arial, sans-serif;background:var(--bg);color:var(--text)}
    nav{background:var(--nav);backdrop-filter: blur(4px);height:72px;display:flex;align-items:center;justify-content:flex-end;padding:0 40px;box-shadow:0 1px 0 rgba(0,0,0,0.03)}
    nav a{margin-left:28px;color:#222;text-decoration:none;font-weight:500}
    .hero{display:grid;grid-template-columns:420px 1fr;align-items:center;min-height:88vh;padding:28px 40px;}
    .hero-left{padding-left:10px}
    .name{font-size:120px;line-height:0.9;font-family: Georgia, 'Times New Roman', serif;margin:0;color:#0b0b0b}
    .subtitle{font-size:28px;margin-top:20px;color:#111; font-weight:300}
    .hero-right{height:70vh;background-position:center;background-size:cover;border-radius:2px;overflow:hidden;margin-left:20px; display:flex; align-items:center; justify-content:center;}
    .hero-right img{width:100%;height:100%;object-fit:cover; display:block}
    .down-indicator{position:absolute;left:50%;transform:translateX(-50%);bottom:30px;width:56px;height:56px;border-radius:50%;border:2px solid rgba(255,255,255,0.7);display:flex;align-items:center;justify-content:center}
    .section{padding:48px 40px}
    .btn{display:inline-block;padding:10px 14px;border-radius:8px;background:#2b8fd6;color:white;text-decoration:none;margin-right:12px}
    @media(max-width:900px){
      .hero{grid-template-columns:1fr;min-height:80vh}
      .name{font-size:56px}
    }
  </style>
</head>
<body>
  <nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Portfolio</a>
    <a href="#">Contact</a>
  </nav>

  <main>
    <section class="hero">
      <div class="hero-left">
        <h1 class="name">Kura<br/>Sai Sreeja</h1>
        <div class="subtitle">Frontend Developer</div>
      </div>
      <div class="hero-right" style="position:relative">
        <!-- sample image - keeps everything self-contained and public -->
        <img src="https://images.unsplash.com/photo-1531123414780-f77fbc0f5f9a?q=80&w=1800&auto=format&fit=crop&ixlib=rb-4.0.3&s=6f4be1d1a35b2b1763f2cfec189b4b23" alt="hero image"/>
        <div class="down-indicator">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Containerized Python API</h2>
      <p style="color:#444;max-width:760px">
        This is a containerized application that exposes a JSON API using FastAPI.
      </p>
      <div style="margin-top:18px">
        <a class="btn" href="#" onclick="return false;">Try it out</a>
        <a class="btn" href="#" style="background:#555" onclick="return false;">Project source</a>
      </div>
    </section>
  </main>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def homepage():
    return HTMLResponse(content=HTML, status_code=200)

if __name__ == "__main__":
    # fallback run when executed directly
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=1234, reload=True)
