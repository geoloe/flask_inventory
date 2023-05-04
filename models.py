from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, Table, LargeBinary, Float, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_login import UserMixin
from . import db
import enum

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    user_id = Column(db.Integer, primary_key=True, autoincrement="auto")

    def get_id(self):
        return (self.user_id)

    username = Column(String(256), nullable=False)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    api_key = Column(String(100), nullable=False)
    is_admin = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    
    # 1 to many relationships #
    item_id = relationship('Item', cascade='all, delete', backref='users', lazy=True)  
    # 1 to many relationships #
    
    def __repr__(self):
        return f"<User: {self.username}>"

class Color(enum.Enum):
    red = "red"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    white = "white"
    black = "black"
    pink = "pink"
    purple = "purple"
    grey = "grey"
    no_color = "n/a"

class Item(db.Model):

    __tablename__ = 'items'

    item_id = Column(db.Integer, primary_key=True, autoincrement="auto")

    def get_id(self):
        return (self.item_id)

    name = Column(String(256), nullable=False)
    description = Column(String(256), nullable=False)
    brand = Column(String(256), nullable=False)
    color = Column(Enum(Color), nullable=False)
    code_number = Column(String(256), nullable=False)
    external_url = Column(String(256), nullable=False)
    count = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    subcategory_id = Column(Integer, ForeignKey("subcategories.subcategory_id"), nullable=False)
    
    time_created = Column(DateTime(timezone=True), server_default=func.now())


    def __repr__(self):
        return f"<Item: {self.name}>"
    
class Category(db.Model):

    __tablename__ = 'categories'

    category_id = Column(db.Integer, primary_key=True, autoincrement="auto")
    
    subcategory_id = relationship('Subcategory', cascade='all, delete', backref='categories', lazy=True)
    # 1 to many relationships #
    
    def get_id(self):
        return (self.category_id)

    name = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<Category: {self.name}>"

class Subcategory(db.Model):

    __tablename__ = 'subcategories'
    
    # 1 to many relationships #    
    item_id = relationship('Item', cascade='all, delete', backref='subcategories', lazy=True)

    subcategory_id = Column(db.Integer, primary_key=True, autoincrement="auto")
    category_id = Column(Integer, ForeignKey("categories.category_id"))


    def get_id(self):
        return (self.category_id)

    name = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<Subcategory: {self.name}>"

