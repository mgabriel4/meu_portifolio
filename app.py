from flask import Flask, render_template
import config
from datetime import datetime

app = Flask(__name__)
app.secret_key = "portifolio"
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.get("/")
def index():
    hoje = datetime.today().strftime("%Y-%m-%d")
    return render_template(
        "index/index.html",
        hoje=hoje,
        titulo="Portfólio | Maria Gabriela"
    )

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=True)