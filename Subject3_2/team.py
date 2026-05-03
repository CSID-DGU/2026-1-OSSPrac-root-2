from flask import Flask, render_template, redirect, url_for, session, abort
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


def init_generated_team():
    if "generated_team" not in session:
        session["generated_team"] = {
            "team_name": "",
            "team_intro": "",
            "team_image": "images/default-team.png",
            "members": [],
            "next_member_id": 1000
        }


def get_generated_team():
    init_generated_team()
    return session["generated_team"]


def save_generated_team(team):
    session["generated_team"] = team
    session.modified = True


def get_generated_member_by_id(member_id):
    team = get_generated_team()

    for member in team.get("members", []):
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
    root_member = get_root_member_by_id(member_id)

    if root_member:
        return render_template(
            "member_detail.html",
            member=root_member,
            is_root_member=True
        )

    generated_member = get_generated_member_by_id(member_id)

    if generated_member:
        return render_template(
            "member_detail.html",
            member=generated_member,
            is_root_member=False
        )

    abort(404)

#테스트용
@app.route("/reset")
def reset_generated_team():
    session.pop("generated_team", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)