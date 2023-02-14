from flask import Blueprint, Flask, render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user
from . import db
from .models import *

#initialize flask app
main = Blueprint('main', __name__)

@login_required
@main.route('/')
def index():
    if current_user.is_authenticated:
        #print(current_user.username)
        return render_template('index.html', username=current_user.username)
    else:
        return render_template('index.html')
    
@login_required
@main.route('/dashboard')
def dashboard():
    if current_user.is_authenticated:
        #print(current_user.username)
        return render_template('dashboard.html', username=current_user.username)
    else:
        return render_template('dashboard.html')

@login_required
@main.route('/inventory')
def inventory():
    if current_user.is_authenticated:
        #print(current_user.username)
        cats = db.session.query(Category.category_id, Category.name).all()
        items = db.session.query(Item.item_id, Item.name, Item.price, Item.count, Item.user_id, Category.name, Subcategory.name, Item.time_created).filter(Item.user_id==User.user_id).filter(Category.category_id==Subcategory.category_id).filter(Item.user_id==current_user.user_id).all()
        subcats = db.session.query(Subcategory.subcategory_id, Category.category_id, Category.name, Subcategory.name).join(Category).filter(Category.category_id==Subcategory.category_id).all()
        #print(subcats)
        print(items)
        return render_template('inventory.html', username=current_user.username, user_id=current_user.user_id, cats=cats, items=items, subcats=subcats)
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
        new_cat = Item(name=request.form.get('item-name'), price=request.form.get('item-price'), count=request.form.get('item-count'), user_id=current_user.user_id, category_id=request.form.get('item-cat'), subcategory_id=request.form.get('item-subcat'))
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