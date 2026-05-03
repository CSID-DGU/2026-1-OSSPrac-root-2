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


def get_root_member_by_id(member_id):
    members = load_root_members()

    for member in members:
        if int(member.get("id")) == member_id:
            return member

    return None


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

@app.route("/members/<int:member_id>")
def member_detail(member_id):
    # 팀원 상세조회 페이지
    member = get_root_member_by_id(member_id)

    if member is None:
        return "존재하지 않는 팀원입니다.", 404

    return render_template(
        "member_detail.html",
        member=member,
        is_root_member=True
    )


if __name__ == "__main__":
    app.run(debug=True)