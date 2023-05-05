from flask import Blueprint, Flask, render_template, request, url_for, flash, redirect
from flask_mail import Mail, Message
from flask_login import login_required, current_user
import json
from . import db
from .models import *
import enum

#initialize flask app
main = Blueprint('main', __name__)

mail_app = Flask(__name__)
#Email app config
mail_app.config['MAIL_SERVER']='smtp.gmail.com'
mail_app.config['MAIL_PORT'] = 587
mail_app.config['MAIL_USERNAME'] = 'georgsinventory@gmail.com'
mail_app.config['MAIL_PASSWORD'] = 'udqkmynqxdduvvci'
mail_app.config['MAIL_USE_TLS'] = True
mail_app.config['MAIL_USE_SSL'] = False
mail = Mail(mail_app)

def query_to_dict(f, name):
    dictionary = {}
    dictionary[name] = []
    my_string = ''
    for key in f:
        for k in key:
            dictionary[name].append(my_string.join(str(k)))

    #dictionary[name].append(names)
    return dictionary

@login_required
@main.route('/')
def index():
    if current_user.is_authenticated:
        #print(current_user.username)
        print(current_user.is_admin)
        return render_template('index.html', username=current_user.username, is_admin=current_user.is_admin)
    else:
        return render_template('index.html')

@login_required
@main.route('/access')
def access():
    if current_user.is_authenticated:
        #print(current_user.username)
        unactive_users = db.session.query(User.email, User.surname, User.name, User.username, User.user_id).filter(User.is_active=='0').all()
        return render_template('access.html', username=current_user.username, is_admin=current_user.is_admin, unactive_users=unactive_users)
    else:
        return render_template('access.html')
    
@login_required
@main.route('/access/grant_access', methods=['POST'])
def grant_access():
    f = request.form
    ids = []
    emails = []
    #print(f)
    
    for key in f.keys():
        for value in f.getlist(key):
            #print(key,":",value)  
            ids.append(key)
            db.session.query(User).filter(User.user_id == key).update({'is_active': True})
            emails.append(db.session.query(User.email).filter(User.user_id == key).first())
            db.session.commit()

    #print(ids)
    #print(emails)
    for key in emails:
        for k in key:
            #print(k)  
            #send email to user
            msg = Message('Your account has been activated!', sender =   'georgsinventory@gmail.com', recipients = [k])
            msg.body = "You can now login to your own inventory!"
            mail.send(msg)
            flash('Changes have been saved!')
    
    return redirect(url_for('main.access'))
   
@login_required
@main.route('/dashboard')
def dashboard():
    if current_user.is_authenticated:
        #print(current_user.username)
        return render_template('dashboard.html', username=current_user.username, is_admin=current_user.is_admin)
    else:
        return render_template('dashboard.html')

@login_required
@main.route('/inventory')
def inventory():
    if current_user.is_authenticated:
        #print(current_user.username)
        cats = db.session.query(Category.category_id, Category.name).all()
        categories = db.session.query(Category.name).all()
        subcategories = db.session.query(Subcategory.name).all()
        categories_id = db.session.query(Category.category_id).all()
        subcategories_id = db.session.query(Subcategory.subcategory_id).all()
        items = db.session.query(Item.item_id, Item.name, Item.description, Item.external_url, Item.brand, Item.color, Item.code_number, Item.count, Item.user_id, Category.name, Subcategory.name, Item.time_created).filter(Item.user_id==User.user_id).filter(Category.category_id==Subcategory.category_id).filter(Item.user_id==current_user.user_id).all()
        subcats = db.session.query(Subcategory.subcategory_id, Category.category_id, Category.name, Subcategory.name).join(Category).filter(Category.category_id==Subcategory.category_id).all()
        
        categories = query_to_dict(categories, 'categories')
        subcategories = query_to_dict(subcategories, 'subcategories')
        categories_id = query_to_dict(categories_id, 'category ids')
        subcategories_id = query_to_dict(subcategories_id, 'subcategory ids')
        print(categories, subcategories)

        #make color list

        #print(subcats)
        #print(items)
        return render_template('inventory.html', username=current_user.username, user_id=current_user.user_id, cats=cats, items=items, subcats=subcats, is_admin=current_user.is_admin, categories=categories, subcategories=subcategories, categories_id=categories_id, subcategories_id=subcategories_id)
    else:
        return render_template('index.html')
    
@login_required
@main.route('/category', methods=['POST'])
def category():
    if request.form.get('cat-name') != None:
        new_cat = Category(name=request.form.get('cat-name'))
        db.session.add(new_cat)
        db.session.commit()
        flash('New category ' + request.form.get('cat-name') + ' has been successfully added.')
    else:
        flash('New category ' + request.form.get('cat-name') + ' has not been successfully added.')
    
    return redirect(url_for('main.inventory'))

@login_required
@main.route('/item', methods=['POST'])
def item():
    if request.form.get('item-name') != None:
        new_cat = Item(name=request.form.get('item-name'),
                       count=request.form.get('item-count'),
                       description=request.form.get('item-description'),
                       brand=request.form.get('item-brand'),
                       color=request.form.get('item-color'),
                       external_url=request.form.get('item-url'),
                       code_number=request.form.get('item-number'),
                       user_id=current_user.user_id,
                       subcategory_id=request.form.get('item-subcat'))
        db.session.add(new_cat)
        db.session.commit()
        flash('New item ' + request.form.get('item-name') + ' has been successfully added.')
    else:
        flash('New item ' + request.form.get('item-name') + ' has not been successfully added.')
    
    return redirect(url_for('main.inventory'))

@login_required
@main.route('/subcat', methods=['POST'])
def subcat():
    if request.form.get('subcat-name') != None:
        new_subcat = Subcategory(category_id=request.form.get('subcat-id'), name=request.form.get('subcat-name'))
        db.session.add(new_subcat)
        db.session.commit()
        flash('New subcategory ' + request.form.get('subcat-name') + ' has been successfully added.')
    else:
        flash('New subcategory ' + request.form.get('subcat-name') + ' has not been successfully added.')
    
    return redirect(url_for('main.inventory'))


@login_required
@main.route('/delete/item', methods=['POST'])
def deleteitem():
    f = request.form
    names = []
    if f:
        for key in f.keys():
            for value in f.getlist(key):
                print(key,":",value)  
                names.append(key)             
                Item.query.filter_by(item_id=value).delete()
                db.session.commit()
        flash("Items: '" + ", ".join(names) + "' have been successfully deleted.")
    else:
        flash('No items selected.')
    
    return redirect(url_for('main.inventory'))

@login_required
@main.route('/edit/item', methods=['POST'])
def edititem():
    f = request.form
    if f:
        for key in f.keys():
            for value in f.getlist(key):
                print(key,":",value)  
    
    return redirect(url_for('main.inventory'))