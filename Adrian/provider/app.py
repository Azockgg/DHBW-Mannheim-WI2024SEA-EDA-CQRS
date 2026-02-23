from flask import Flask, Response, render_template
import os

app = Flask(__name__)


@app.get("/styles.css")
def styles():
    return Response(render_template("styles.css"), mimetype="text/css")


@app.get("/")
def index():
    consumer_url = os.getenv("CONSUMER_COMMAND_URL", "http://localhost:8081/commands/stop-button-press")
    return render_template("index.html", consumer_command_url=consumer_url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
