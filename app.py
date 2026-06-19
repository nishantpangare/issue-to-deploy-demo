from flask import Flask, request, jsonify
from utils import calculate_discount, get_user

app = Flask(__name__)

@app.route("/user/<int:user_id>")
def user(user_id):
    user = get_user(user_id)
    return jsonify(user)

@app.route("/discount")
def discount():
    price = request.args.get("price")
    result = calculate_discount(price, 10)
    return jsonify({"discounted_price": result})

@app.route("/divide")
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"result": a / b})

if __name__ == "__main__":
    app.run(debug=True)
