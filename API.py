from flask import Flask, jsonify
from Par import parse_all
from Config import FIRSTID, MAXID, MAX_WORKERS, MIN_PRICE, MAX_PRICE

app = Flask(__name__)

@app.route("/api/get_products", methods=["GET"])
def GetProducts():
    products_id = range(FIRSTID, MAXID)
    products = parse_all(products_id, max_workers=MAX_WORKERS)
    filtered = [p for p in products if MIN_PRICE <= p["price"] <= MAX_PRICE]
    return jsonify(filtered)

@app.route("/api/check_health", methods=["GET"])
def CheckHealth():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)