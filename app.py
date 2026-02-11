from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "job_tracker_secret_key"

# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- AUTH : REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# ---------------- AUTH : LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

    return render_template("login.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ---------------- HOME (READ) ----------------
@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    jobs = conn.execute(
        "SELECT * FROM job_applications WHERE user_id=?",
        (session["user_id"],)
    ).fetchall()
    conn.close()

    return render_template("index.html", jobs=jobs)

# ---------------- CREATE ----------------
@app.route("/add", methods=["GET", "POST"])
def add_job():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        date = request.form["date"]
        status = request.form["status"]

        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO job_applications
            (company_name, job_role, applied_date, status, user_id)
            VALUES (?, ?, ?, ?, ?)
            """,
            (company, role, date, status, session["user_id"])
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add_job.html")

# ---------------- UPDATE ----------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_job(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    job = conn.execute(
        "SELECT * FROM job_applications WHERE id=? AND user_id=?",
        (id, session["user_id"])
    ).fetchone()

    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        date = request.form["date"]
        status = request.form["status"]

        conn.execute(
            """
            UPDATE job_applications
            SET company_name=?, job_role=?, applied_date=?, status=?
            WHERE id=? AND user_id=?
            """,
            (company, role, date, status, id, session["user_id"])
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    conn.close()
    return render_template("edit_job.html", job=job)

# ---------------- DELETE ----------------
@app.route("/delete/<int:id>")
def delete_job(id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    conn.execute(
        "DELETE FROM job_applications WHERE id=? AND user_id=?",
        (id, session["user_id"])
    )
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
