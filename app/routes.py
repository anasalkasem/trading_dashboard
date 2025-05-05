from flask import Blueprint, render_template, request, redirect
from .models import Trade
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    trades = Trade.query.order_by(Trade.id.desc()).paginate(page=page, per_page=per_page)
    last_trade = Trade.query.order_by(Trade.id.desc()).first()
    is_admin = request.remote_addr == '127.0.0.1'
    return render_template('dashboard.html', trades=trades, last_trade=last_trade, is_admin=is_admin)

@main.route('/delete_all', methods=['POST'])
def delete_all_trades():
    if request.remote_addr == '127.0.0.1':
        Trade.query.delete()
        db.session.commit()
    return redirect('/')
