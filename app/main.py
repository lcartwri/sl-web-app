import os
from forms.forms import AddTest,DelTest
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

##################################
###### SQL DATABASE SECTION ######
##################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#Migrate(app,db)


##################################
######### MODELS SECTION #########
##################################
class ImpairmentTestConfig(db.Model):
    
    __tablename__ = 'impairment_values_table'
    id = db.Column(db.Integer,primary_key=True)
    test_name = db.Column(db.Text)
    #bandwidth = db.Column(db.Integer)
    #delay = db.Column(db.Integer)
    #loss = db.Column(db.Integer)

    def __init__(self,test_name):
        self.test_name = test_name
    

##################################################
###### VIEW FUNCTIONS == HAVE FORMS SECTION ######
##################################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aci')
def aci_home():
    return render_template('home_aci.html')

@app.route('/sda')
def sda_home():
    return render_template('home_sda.html')

@app.route('/xdomain')
def xdomain_home():
    return render_template('home_xdomain.html')

@app.route('/sdwan')
def sdwan_home():
    return render_template('home_sdwan.html')

@app.route('/sdwan/add_test',methods=['GET','POST'])
def new_test():

    form = AddTest()
    if form.validate_on_submit():
        test_name = form.test_name.data
        new_test = ImpairmentTestConfig(test_name)
        db.session.add(new_test)
        db.session.commit()

        return redirect(url_for('list_test'))
    
    return render_template('add_test.html',form=form)

@app.route('/sdwan/list_test')
def list_test():
    tests = ImpairmentTestConfig.query.all()
    return render_template('list_test.html',tests=tests)

@app.route('/sdwan/delete_test', methods=['GET','POST'])
def del_test():

    form = DelTest()
    if form.validate_on_submit():
        id = form.id.data
        test = ImpairmentTestConfig.query.get(id)
        db.session.delete(test)
        db.session.commit()

        return redirect(url_for('list_test'))
    
    return render_template('delete_test.html',form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host='0.0.0.0')