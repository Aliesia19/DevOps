import logging
import socket
import time

from flask import Flask, jsonify

app = Flask(__name__)


start_time = time.time()


request_count = 0


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)



def send_error_to_statsd(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(
                message.encode("utf-8"),
                ("127.0.0.1", 8125)
            )
    except OSError:
        logger.warning("Could not send message to StatsD server")



@app.before_request
def count_requests():
    global request_count
    request_count += 1



@app.route("/")
def home():
    logger.info("Main page was requested")
    return "Сервіс працює"



@app.route("/error")
def error():
    try:
        result = 10 / 0
        return str(result)

    except Exception:
        logger.exception("An exception occurred")

        send_error_to_statsd(
            "application.error:1|c"
        )

        return "Виникла помилка сервера", 500



@app.route("/status")
def status():
    uptime = time.time() - start_time

    logger.info("Status page was requested")

    return jsonify({
        "status": "running",
        "uptime_seconds": round(uptime, 2),
        "request_count": request_count
    })



if __name__ == "__main__":
    app.run(debug=False)
