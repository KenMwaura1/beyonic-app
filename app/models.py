from dataclasses import dataclass

# from sqlalchemy.orm import backref
from sqlalchemy_utils import PhoneNumber
from commands import db


@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=True, nullable=False)
    last_name = db.Column(db.String(255), unique=True, nullable=False)
    # phone_number = db.Column(db.String(255), unique=True, nullable=False)
    _phone_number = db.Column(db.Unicode(255))
    phone_country_code = db.Column(db.Unicode(8))

    phone_number = db.composite(
        PhoneNumber,
        _phone_number,
        phone_country_code
    )


@dataclass
class Payment(db.Model):
    __tablename__ = 'payments'
    account_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    first_name = db.relationship('Users', backpopulates="payments")
    last_name = db.relationship('Users', backpopulates="payments")
    payment_type = db.Column(db.String(20), default="money")
    description = db.Column(db.String(140), nullable=False)
    amount = db.Column(db.Integer(), default=0)
    callback_url = db.Column(db.String(255), default="https://my.website/payments/callback")

    def airtime(self):
        self.payment_type = "airtime"

@dataclass
class BeyonicResponse(db.Model):
    account = db.Column(db.Integer())
    amount = db.Column(db.String(30))
    author = db.Column(db.BigInteger())
    charged_fee = db.Column(db.Integer())
    created = db.Column(db.String(255))
    modified = db.Column(db.String(255))
    currency = db.Column(db.String(255))
    description = db.Column(db.String(255))
    state = db.Column(db.String(255))

