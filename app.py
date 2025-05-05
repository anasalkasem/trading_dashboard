from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

# نموذج الصفقة
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20))
    action = db.Column(db.String(10))
    price = db.Column(db.Float)
    timestamp = db.Column(db.String(50))
    reasons = db.Column(db.String(200))

# الصفحة الرئيسية
@app.route('/')
def dashboard():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    trades = Trade.query.order_by(Trade.id.desc()).paginate(page=page, per_page=per_page)
    last_trade = Trade.query.order_by(Trade.id.desc()).first()
    return render_template('dashboard.html', trades=trades, last_trade=last_trade)

@app.route('/delete_all', methods=['POST'])
def delete_all_trades():
    Trade.query.delete()
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)