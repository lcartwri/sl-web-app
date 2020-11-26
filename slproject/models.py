#model.py
from slproject import db
# db setup in the __init__.py under slproject file


class AarTest(db.Model):

    __tablename__ = 'sdwanaartest'

    id = db.Column(db.Integer,primary_key= True)
    test_name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    #puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,test_name):
        self.test_name = test_name
        #self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.test_name}"