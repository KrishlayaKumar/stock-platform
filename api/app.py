from flask import Flask, request, jsonify, render_template
from app.pipeline import run_pipeline

app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    symbol = data.get("symbol")

    if not symbol:
        return jsonify({"error": "Stock symbol required"}), 400

    result = run_pipeline(symbol)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
