# app.py
from flask import Flask, render_template, jsonify
import ids   # Import our IDS logic

app = Flask(__name__)

# Start IDS sniffing
ids.run_ids()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    # Convert defaultdict to normal dict for JSON
    return jsonify({
        "total": ids.alerts["total"],
        "syn_flood": ids.alerts["syn_flood"],
        "port_scan": ids.alerts["port_scan"],
        "suspicious_ips": dict(ids.alerts["suspicious_ips"])
    })

if __name__ == "__main__":
    app.run(debug=True)
