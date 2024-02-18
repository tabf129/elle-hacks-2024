from flask import Flask, request
from flask_cors import CORS
from transcribe import transcribe_audio
import base64


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://curly-space-spoon-7xgxqx6wj542rr4j-3000.app.github.dev"}})


@app.route("/api/transcribe", methods=["POST"])
def index():
    data = request.json
    if "audio" in data:
        audio = base64.b64decode(data["audio"])
        # audio = data["audio"]
        return {
            "response": str(transcribe_audio(audio))
        }

    return "Request has been received"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

# EOF
