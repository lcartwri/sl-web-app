# This is app.py, this is the main file called.
from slproject import app,db
from flask import render_template



#####@app.route('/')
#####def home():
#####    return render_template('home.html')

@app.route('/')
@app.route('/<page>')
def home(page=None):
   if page:
      # called with page parameter
      return render_template('%s.html' % page)
   else:
      # called with no parameters 
      return render_template('home.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host='0.0.0.0')