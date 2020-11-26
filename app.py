# This is app.py, this is the main file called.
from slproject import app,db
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host='0.0.0.0')