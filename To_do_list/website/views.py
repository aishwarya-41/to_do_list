from flask import Blueprint, render_template, request, redirect, jsonify,flash
from .models import User_Name, Item
from flask_login import current_user, login_user, logout_user, login_required
from . import db
import json

views = Blueprint('views',__name__)


@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        data = request.form.get("i1")
        if len(data)<1:
            flash('Please enter something')
        if data:
            new_item = Item(data=data,user_id=current_user.id)
            db.session.add(new_item)
            db.session.commit()
        return redirect('/')
    
    user_items = User_Name.query.filter_by(id=current_user.id).all()
    return render_template('home.html',user=current_user,items=user_items)

@views.route('/delete-item',methods=['POST'])
@login_required
def delete_item():
    item = json.loads(request.data)
    itemId = item['itemId']
    item = Item.query.get(itemId)

    if item:
        if item.user_id == current_user.id:
            db.session.delete(item)
            db.session.commit()
            return jsonify({})
