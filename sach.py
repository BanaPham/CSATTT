from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'banana' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
MODEL_FOLDER = 'model'

@app.route('/')
def signin():
    return render_template('signin.html')

@app.route('/home')
def home():
    return render_template('user/home.html')

@app.route('/book')
def book():
    return render_template('user/book.html')

@app.route('/account')
@app.route('/account/<active_tab>')
def account(active_tab='profile'):
    if active_tab not in ['profile', 'order']:
        active_tab = 'profile' 
    return render_template('user/account.html', active_tab=active_tab)

@app.route('/cart')
def cart():
    return render_template('user/cart.html')

@app.route('/admin')
def admin():
    return render_template('admin/home.html')

@app.route('/profile')
def profile():
    return render_template('admin/profile.html')

@app.route('/category')
def category():
    return render_template('admin/category.html')

@app.route('/invoice')
def invoice():
    return render_template('admin/invoice.html')

@app.route('/admin_staff')
def adminnstaff():
    return render_template('admin/adminnstaff.html')
# @app.route('/admin/<active_tab>')
# def admin(active_tab='category'):
#     if active_tab not in ['category', 'invoice', 'adminnstaff']:
#         active_tab = 'category' 
#     return render_template('admin/home.html', active_tab=active_tab)

@app.route('/model_images/<filename>')
def get_model_image(filename):
    return send_from_directory(MODEL_FOLDER, filename)
    
if __name__ == "__main__":
    with app.app_context():
        if not path.exists('user.db'):
            db.create_all() 
    app.run(debug = True)

