from . import db

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20))
    action = db.Column(db.String(10))
    price = db.Column(db.Float)
    timestamp = db.Column(db.String(50))
    reasons = db.Column(db.String(200))
