from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

# Webhook URL của bạn
url = "https://discord.com/api/webhooks/1089726987104428062/AnZ-7kUxSVKBq3Yo6eqlsWc3gCHn243zfFadgC5ZDKrfbbfuT5y_7vyq_Mlji5x4a11v"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_data", methods=["POST"])
def send_data():
    # Lấy tên và tuổi từ form
    name = request.form["name"]
    age = request.form["age"]

    # Tạo message embed
    embed = {
        "title": "Thông tin người dùng",
        "description": f"Tên: {name}\nTuổi: {age}",
        "color": 16711680 # Red color
    }

    # Tạo payload với message embed
    payload = {
        "embeds": [embed]
    }

    # Gửi webhook
    response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

    # Kiểm tra kết quả gửi webhook
    if response.status_code == 204:
        return render_template("troll.html")

if __name__ == "__main__":
    app.run()

