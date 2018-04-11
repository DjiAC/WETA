from app.models import db


class Disease(db.Model):
    __tablename__ = 'diseases'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    link = db.Column(db.String(255))
    added = db.Column(db.DateTime())

    def __repr__(self):
        return "<Disease(name='{}', link='{}', added={})>".format(self.name, self.link, self.added)
