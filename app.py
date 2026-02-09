from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("scam.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS records(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value TEXT,
            type TEXT,
            status TEXT
        )
    """)
    conn.commit()

    # demo data
    sample = [
        ("9876543210", "mobile", "scam"),
        ("amazon-support.net", "website", "scam"),
        ("realstore.com", "website", "safe"),
        ("helpdesk_whatsapp", "whatsapp", "scam"),
        ("official_brand", "instagram", "safe")
    ]

    for s in sample:
        c.execute("INSERT INTO records(value,type,status) VALUES(?,?,?)", s)

    conn.commit()
    conn.close()

init_db()


def check_record(value, type_):
    conn = sqlite3.connect("scam.db")
    c = conn.cursor()
    c.execute("SELECT status FROM records WHERE value=? AND type=?", (value, type_))
    row = c.fetchone()
    conn.close()
    return row[0] if row else "not found"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        value = request.form["value"]
        type_ = request.form["type"]
        result = check_record(value, type_)
        return render_template("result.html", result=result, value=value)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

