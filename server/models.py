from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Numeric

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    price = Column(Numeric(precision=10, scale=2))