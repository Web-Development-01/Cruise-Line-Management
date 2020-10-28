from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Trans.sqlite3'  
app.config['SECRET_KEY'] = "secret key"  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  

class Transaction(db.Model):
    ID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Amount = db.Column(db.Integer)
    PaymentMode = db.Column(db.String(30))
    def __init__(self,Amount,PaymentMode):
        self.Amount=Amount
        self.PaymentMode=PaymentMode

@app.route('/')
def home():
    return render_template("Dest.html")

@app.route('/Display',methods=['POST',"GET"])
def Display():
    if request.method == "POST":
        #return request.form['dob']
        amt=request.form['amount']
        pmd=request.form['payment_mode']
        obj = Transaction(amt,pmd)
        db.session.add(obj)
        db.session.commit()
        return str(obj.Amount)+" "+obj.PaymentMode+" "+str(obj.ID)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)