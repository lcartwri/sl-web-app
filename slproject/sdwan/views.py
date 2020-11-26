#views.py under sdwan folder

from flask import Blueprint,render_template,redirect,url_for
from slproject import db
from slproject.models import AarTest
from slproject.sdwan.forms import AddTest,DelTest

sdwan_blueprint = Blueprint('sdwan',
                              __name__,
                              template_folder='templates/sdwan')

@sdwan_blueprint.route('/add_test', methods=['GET', 'POST'])
def add_test():

    form = AddTest()

    if form.validate_on_submit():
        test_name = form.test_name.data
        test_id = form.test_id.data
        # Add new test to database
        new_test = AarTest(test_name)
        db.session.add(new_test)
        db.session.commit()

        return redirect(url_for('sdwan.list_test'))
    return render_template('add_test.html',form=form)
