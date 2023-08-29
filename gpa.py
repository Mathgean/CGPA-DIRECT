from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        marks = []
        credit = []
        for i in range(1, int(request.form['op']) + 1):
            marks.append(int(request.form["g"+str(i)]))
            credit.append(int(request.form["c"+str(i)]))
        result = []
        for i in range(len(credit)):
            result.append(credit[i] * marks[i])
        for i in range(len(result)):
            if result[i] == 0:
                credit[i] = 0
        sum_total = 0
        for i in result:
            sum_total += i
        sum_credit = 0
        for i in credit:
            sum_credit += i
        try:
            gpa = sum_total / sum_credit
        except ZeroDivisionError:
            gpa = 0
        return render_template('u.html', data=gpa)
    return render_template("u.html")

if __name__ == "__main__":
    app.run(debug=True)