#model.py
from slproject import db
# db setup in the __init__.py under slproject file


class AarTest(db.Model):

    __tablename__ = 'sdwanaartest'

    id = db.Column(db.Integer,primary_key=True)
    test_name = db.Column(db.Text)
    ###bandwidth = db.Column(db.Integer)
    ###delay = db.Column(db.Integer)
    ###loss = db.Column(db.Integer)

    def __init__(self,test_name,bandwidth,delay,loss):
        self.test_name = test_name
        ###self.bandwidth = bandwidth
        ###self.delay = delay
        ###self.loss = loss

    def __repr__(self):
        return f"Owner Name: {self.test_name}"

class SdaTest(db.Model):

    __tablename__ = 'sdatest'

    id = db.Column(db.Integer,primary_key=True)
    test_name = db.Column(db.Text)
    ###bandwidth = db.Column(db.Integer)
    ###delay = db.Column(db.Integer)
    ###loss = db.Column(db.Integer)

    def __init__(self,test_name,bandwidth,delay,loss):
        self.test_name = test_name
        ###self.bandwidth = bandwidth
        ###self.delay = delay
        ###self.loss = loss
        
    def __repr__(self):
        return f"Owner Name: {self.test_name}"