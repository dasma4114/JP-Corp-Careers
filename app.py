from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'data analyst',
        'location': 'San Francisco, USA'
        'salary': 105,000
    },
    {
        'id': 2,
        'title': 'data scientist',
        'location': 'San Francisco, USA'
        'salary': 135,000
    },
    {
        'id': 3,
        'title': 'Frontend Dev',
        'location': 'San Francisco, USA'
        'salary': 125,000
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Remote'
        'salary': 125,000
    },
]

@app.route("/")
def hello_world():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
