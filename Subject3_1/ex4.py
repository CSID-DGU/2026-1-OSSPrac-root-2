from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input_page():
    return render_template('input.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        result['StudentNumber'] = request.form.get('student_number')
        result['Gender'] = request.form.get('gender')
        
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)