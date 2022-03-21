from flask import Flask, request, make_response
from RotatingLogger import RotatingLogger


LOGGER_NAME = "client_side"

CONFIG_FILE = "logging.yml"

app = Flask(__name__)

logger = RotatingLogger(CONFIG_FILE, LOGGER_NAME)


def format_log(request):
    return "Client IP : %s, Post Data : %s" % (str(request.remote_addr), request.data)


@app.route("/", methods=["POST"])
def client_side_logging():
    log_data = format_log(request)
    logger.log.error(log_data)
    return make_response(request.data, 201)


if __name__ == "__main__":
    app.run()