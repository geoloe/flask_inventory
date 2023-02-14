from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, Table, LargeBinary, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_login import UserMixin
from . import db


user_subscription = db.Table('user_subscriptions',
    Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    Column('subscription_id', db.Integer, db.ForeignKey('subscriptions.subscription_id'))
)

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
    
    # 1 to many relationships #
    item_id = relationship('Item', cascade='all, delete', backref='users', lazy=True)  
    # 1 to many relationships #
    
    # 1 to 1 relationships #
    budget_id = Column(Integer, ForeignKey('budgets.budget_id'), unique=True)
    budgets = relationship("MonthlyBudget", backref=db.backref("users", uselist=False))
    # 1 to 1 relationships #

    # many to many relationships #
    subscription = relationship("Subscription", secondary=user_subscription, lazy='subquery', backref=db.backref('users'))
    # many to many relationships #
    
    def __repr__(self):
        return f"<User: {self.username}>"

class Item(db.Model):

    __tablename__ = 'items'

    item_id = Column(db.Integer, primary_key=True, autoincrement="auto")

    def get_id(self):
        return (self.item_id)

    name = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    subcategory_id = Column(Integer, ForeignKey("subcategories.subcategory_id"), nullable=False)
    
    time_created = Column(DateTime(timezone=True), server_default=func.now())


    def __repr__(self):
        return f"<Item: {self.name}>"
    
class Category(db.Model):

    __tablename__ = 'categories'

    category_id = Column(db.Integer, primary_key=True, autoincrement="auto")
    
    # 1 to many relationships #
    item_id = relationship('Item', cascade='all, delete', backref='categories', lazy=True)
    subcategory_id = relationship('Subcategory', cascade='all, delete', backref='categories', lazy=True)
    # 1 to many relationships #
    
    def get_id(self):
        return (self.category_id)

    name = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<Category: {self.name}>"

class Subcategory(db.Model):

    __tablename__ = 'subcategories'

    subcategory_id = Column(db.Integer, primary_key=True, autoincrement="auto")
    category_id = Column(Integer, ForeignKey("categories.category_id"))


    def get_id(self):
        return (self.category_id)

    name = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<Subcategory: {self.name}>"

class Subscription(db.Model):

    __tablename__ = 'subscriptions'

    subscription_id = Column(db.Integer, primary_key=True, autoincrement="auto")
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    
    user_id = Column(Integer, ForeignKey("users.user_id"))

    def get_id(self):
        return (self.subscription_id)

    name = Column(String(100), nullable=False)
    cost = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<Subscription: {self.name}>"

class MonthlyBudget(db.Model):

    __tablename__ = 'budgets'

    budget_id = Column(db.Integer, primary_key=True, autoincrement="auto")

    def get_id(self):
        return (self.subscription_id)

    budget = Column(String(100), nullable=False)

    
    def __repr__(self):
        return f"<Monthly Budget: {self.budget}>"

    

