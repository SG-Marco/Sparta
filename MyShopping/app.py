from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

client = MongoClient('mongodb://allenpoe:3333@localhost', 27017)
db = client.dbhomework

app = Flask(__name__)

@app.route('/')
def homework():
    return render_template('index.html')




# orders
# doc = {"buyer", "number", "address", "phone"}

# all_orders = list(db.orders.find({}))


@app.route('/order', methods=['POST'])
def save_order():
    buyer_recieve = request.form['buyer_give']
    number_recieve = request.form['number_give']
    adderss_recieve = request.form['address_give']
    phone_recieve = request.form['phone_give']

    doc={
        "buyer" : buyer_recieve,
        "number" : number_recieve,
        "address" : adderss_recieve,
        "phone" : phone_recieve
    }

    db.orders.insert_one(doc)

    return jsonify({"result": "success", "msg": "포르쉐 주문이 완료되었습니다!!!!"})
    


@app.route('/order', methods=['GET'])
def view_order():
    orders = list(db.orders.find({},{"_id" : False}))

    return jsonify({"result" : "success", "all_orders" : orders})





if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
