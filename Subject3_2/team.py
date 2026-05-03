from flask import Flask, render_template
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

DATA_FILE = os.path.join(app.root_path, "data", "members.json")

def load_root_data():
    # members.json에서 ROOT 팀 전체 데이터를 불러오기
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_root_team():
    # ROOT 팀 소개 정보 반환
    data = load_root_data()
    return data.get("team", {})


def load_root_members():
    # ROOT 팀원 목록 반환
    data = load_root_data()
    return data.get("members", [])

@app.route("/")
def index():
    # ROOT 팀 소개 메인 페이지
    team = load_root_team()
    members = load_root_members()

    return render_template(
        "index.html",
        team=team,
        members=members
    )


if __name__ == "__main__":
    app.run(debug=True)