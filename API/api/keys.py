from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAZORPAY_KEY_ID = "rzp_test_HmRCPtukNJXMaA"
RAZORPAY_SECRET = "A5R9QD2c9E0Pvw114Uuapoh0"

my_pass = "Aniket"

@app.route("/payment-key", methods=["GET"])
def payment():
    password = request.args.get("password")

    if my_pass == password:
        return jsonify({
            "key" : RAZORPAY_KEY_ID,
            "secret" : RAZORPAY_SECRET
        })
    else:
        return jsonify({
            "error" : "Password Miss Match"
        })


if __name__ == "__main__":
    app.run(debug=True, port=3000)
