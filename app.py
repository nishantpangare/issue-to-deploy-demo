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
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        if b == 0:
            return jsonify({"error": "Divisor cannot be zero"}), 400
        return jsonify({"result": a / b})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. 'a' and 'b' must be integers."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)