from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지 (ROOT팀 소개)
@app.route('/')
def home():
    return render_template('index.html')


# 팀원 상세 페이지
members = {
    1: {
        "id": 1,
        "name": "오승현",
        "department": "교육학과",
        "student_id": "2024110423",
        "role": "팀장",
        "language": "Java",
        "email": "example@email.com",
        "phone": "010-0000-0000",
        "image": "/static/images/default.png",
        "github": "#",
        "sns": "#",
        "editable": False,
        "portfolio": [
            {
                "title": "ROOT 팀 소개 페이지",
                "period": "2026.05",
                "role": "프론트엔드",
                "description": "메인 페이지와 CSS 디자인 담당"
            }
        ]
    },
    2: {
        "id": 2,
        "name": "김유미",
        "department": ".",
        "student_id": "2026",
        "role": "팀원",
        "language": "Python",
        "email": "example@email.com",
        "phone": "010-0000-0000",
        "image": "/static/images/default.png",
        "github": "#",
        "sns": "#",
        "editable": False,
        "portfolio": []
    },
    3: {
        "id": 3,
        "name": "오지윤",
        "department": ".",
        "student_id": "2026",
        "role": "팀원",
        "language": "Python",
        "email": "example@email.com",
        "phone": "010-0000-0000",
        "image": "/static/images/default.png",
        "github": "#",
        "sns": "#",
        "editable": False,
        "portfolio": []
    }
}

@app.route('/member/<int:id>')
def member_detail(id):
    member = members.get(id)
    return render_template('member_detail.html', member=member)


# 커뮤니티 (게시판)
@app.route('/community')
def community():
    return render_template('contact.html')  # 일단 재사용


# 팀페이지 제작
@app.route('/input')
def input_page():
    return render_template('input.html')


# 결과 페이지
@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


# 비상연락망
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)