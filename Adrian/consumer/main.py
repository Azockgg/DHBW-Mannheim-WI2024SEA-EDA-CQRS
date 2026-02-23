from dataclasses import asdict
from datetime import datetime, timezone
from uuid import uuid4

from flask import Flask, Response, jsonify, request, render_template

from event_definitions import StopRequestedEvent
from event_runtime import event_bus, event_store, projection

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response


@app.route("/commands/stop-button-press", methods=["POST", "OPTIONS"])
def stop_button_press_command():
    if request.method == "OPTIONS":
        return ("", 204)

    payload = request.get_json(silent=True) or {}
    bus_id = payload.get("busId", "UNKNOWN-BUS")

    event = StopRequestedEvent(
        event_id=str(uuid4()),
        bus_id=bus_id,
        occurred_at=datetime.now(timezone.utc).isoformat(),
    )

    # Command side: erzeugt und speichert Event
    event_store.append(event)
    event_bus.publish(event)

    return jsonify({"status": "accepted", "eventId": event.event_id}), 202


@app.get("/queries/stop-status")
def stop_status_query():
    # Query side: liefert vorbereitete Read-Projection
    return jsonify(projection.to_dict())


@app.get("/queries/events")
def events_query():
    return jsonify([asdict(event) for event in event_store.events])


@app.get("/styles.css")
def styles():
    return Response(render_template("styles.css"), mimetype="text/css")


@app.get("/")
def reaction_page():
    return render_template("reaction.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
