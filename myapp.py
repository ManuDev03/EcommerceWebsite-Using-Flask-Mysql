from flask import Flask,render_template
import pymysql

app = Flask (__name__)

class Database:
    def __init__(self):
        host = ""
        user = "root"
        password = ""
        db = "tshirtshop"
        self.con = pymysql.connect(host=host, user=user, password="",db = db,
        cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def mens_products(self):
        self.cur.execute("SELECT pid,pname,price,pimgurl FROM menstshirts")
        result = self.cur.fetchall()
        return result

    def womens_products(self):
        self.cur.execute("SELECT pid,pname,price,pimgurl FROM womenstshirts")
        result = self.cur.fetchall()
        return result

    def kids_products(self):
        self.cur.execute("SELECT pid,pname,price,pimgurl FROM kidstshirts")
        result = self.cur.fetchall()
        return result


@app.route('/')
def home():
    return render_template ("home.html")



@app.route('/product')
def product():
    def db_queryMens():
        db = Database()
        mensShirts = db.mens_products()
        return mensShirts

    def db_queryWomens():
        db = Database()
        womensShirts = db.womens_products()
        return womensShirts

    def db_queryKids():
        db = Database()
        kidsShirts = db.kids_products()
        return kidsShirts

    res1 = db_queryMens()
    res2 = db_queryWomens()
    res3 = db_queryKids()

    return render_template("product.html", result1=res1, result2=res2, result3=res3)

if __name__ == "__main__":
    app.run(debug=True)
