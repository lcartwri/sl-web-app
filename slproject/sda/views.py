#views.py under sda folder

from flask import Blueprint,render_template,redirect,url_for
from slproject import db
from slproject.models import SdaTest
from slproject.sda.forms import AddTest,DelTest

sda = Blueprint('sda',__name__,template_folder='templates/sda')

@sda.route('/')
def home():
    return render_template('sda_index.html')


@sda.route('/add_test', methods=['GET', 'POST'])
def add_test():

    form = AddTest()
    if form.validate_on_submit():
        test_name = form.test_name.data
        #test_id = form.id.data
        # Add new test to database
        new_test = SdaTest(test_name,0,0,0)
        db.session.add(new_test)
        db.session.commit()

        return redirect(url_for('sda.list_test'))
    return render_template('sda.add_test.html',form=form)

@sda.route('/list_test')
def list_test():
    tests = SdaTest.query.all()
    return render_template('sda.list_test.html',tests=tests)

@sda.route('/delete_test<int:id>', methods=['GET', 'POST'])
def del_test(id):

    test = SdaTest.query.get(id)
    db.session.delete(test)
    db.session.commit()

    return redirect(url_for('sda.list_test'))
