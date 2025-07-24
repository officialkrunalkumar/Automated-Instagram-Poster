from flask import Flask, request, jsonify
from instagrapi import Client
import requests
import os
import tempfile

app = Flask(__name__)

@app.route("/post", methods=["POST"])
def post_to_instagram():
    try:
        data = request.get_json()

        # Validate input
        required_fields = ["username", "password", "caption", "image_url"]
        if not all(field in data for field in required_fields):
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        username = data["username"]
        password = data["password"]
        caption = data["caption"]
        image_url = data["image_url"]

        # Download the image
        response = requests.get(image_url)
        if response.status_code != 200:
            return jsonify({"status": "error", "message": "Image could not be downloaded"}), 400

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(response.content)
            image_path = tmp.name

        # Log in to Instagram
        cl = Client()
        cl.login(username, password)

        # Upload photo with caption
        cl.photo_upload(image_path, caption)

        # Cleanup
        os.remove(image_path)

        return jsonify({"status": "success", "message": "Post uploaded"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
