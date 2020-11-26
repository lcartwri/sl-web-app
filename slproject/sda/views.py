#views.py under sda folder

from flask import Blueprint,render_template,redirect,url_for
from slproject import db
from slproject.models import AarTest
from slproject.sda.forms import AddTest,DelTest

sda_blueprint = Blueprint('sda',
                              __name__,
                              template_folder='templates/sda')

@sda_blueprint.route('/add_test', methods=['GET', 'POST'])
def add_test():

    form = AddTest()

    if form.validate_on_submit():
        test_name = form.test_name.data
        test_id = form.test_id.data
        # Add new test to database
        new_test = AarTest(test_name)
        db.session.add(new_test)
        db.session.commit()

        return redirect(url_for('sda.list_test'))
    return render_template('add_test.html',form=form)
