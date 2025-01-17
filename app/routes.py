from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import products, Product

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', products=products)

@main.route('/buy/<int:product_id>', methods=['POST'])
def buy(product_id):
    for product in products:
        if product.id == product_id:
            if product.stock > 0:
                product.stock -= 1
                flash('Purchase successful!', 'success')
            else:
                flash('Sorry, this product is out of stock.', 'error')
            break
    return redirect(url_for('main.home'))