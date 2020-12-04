#views.py under sdwan folder

from flask import Blueprint,render_template,redirect,url_for
from slproject import db
from slproject.models import AarTest
from slproject.sdwan.forms import AddTest,DelTest
from slproject.sdwan.sdwan_py_functions.sdwan_functions import get_devicecontrollers
from slproject.sdwan.sdwan_py_functions.auth import login

sdwan = Blueprint('sdwan',__name__,template_folder='templates/sdwan')


@sdwan.route('/')
def home():
    controller_name = get_devicecontrollers()
    return render_template('sdwan_index.html',controller_name=controller_name)
######@sdwan.route('/')
######def home():
######    return render_template('sdwan_index.html')


@sdwan.route('/add_test', methods=['GET', 'POST'])
def add_test():

    form = AddTest()
    if form.validate_on_submit():
        test_name = form.test_name.data
        #test_id = form.id.data
        # Add new test to database
        new_test = AarTest(test_name,0,0,0)
        db.session.add(new_test)
        db.session.commit()

        return redirect(url_for('sdwan.list_test'))
    return render_template('sdwan_add_test.html',form=form)

@sdwan.route('/list_test')
def list_test():
    tests = AarTest.query.all()
    return render_template('sdwan_list_test.html',tests=tests)

@sdwan.route('/delete_test<int:id>', methods=['GET', 'POST'])
def del_test(id):

    test = AarTest.query.get(id)
    db.session.delete(test)
    db.session.commit()

    return redirect(url_for('sdwan.list_test'))