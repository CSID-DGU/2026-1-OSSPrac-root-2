from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return "서버 구동" 

if __name__ == "__main__":
    app.run(debug=True)