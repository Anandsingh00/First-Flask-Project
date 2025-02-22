from flask import Flask , render_template,jsonify



app = Flask(__name__)


JOBS =[
    {
        'id':1,
        'title' : 'Maths Faculty',
        'salary' :'Rs: 10,000'
    },
    {
        'id':2,
        'title' : 'Physics Faculty',
        'salary' :'Rs: 12,000'
    },
    {
        'id':3,
        'title' :  'Chemistry Faculty',
        'salary' : 'Rs: 11,000'
    },
     {
        'id':4,
        'title' :  'English Faculty',
        'salary' : 'Rs: 11,000'
    }
]
@app.route('/')
def home():
    return render_template('home.html' ,jobs= JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(debug=True)