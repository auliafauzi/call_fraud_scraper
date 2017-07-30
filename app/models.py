from app import db

class Reports(db.Model):

    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.Integer)
    phone_number = db.Column(db.String(50))
    number_of_comments = db.Column(db.Integer)
    comment = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Reports.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Reports: {}>".format(self.name)