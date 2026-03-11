from flask import Flask, render_template, request, redirect, session
import os
import smtplib
from email.message import EmailMessage

from models.predict import predict_image
from utils.database import connect_db, create_tables
from utils.suggestions import get_suggestions

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

app = Flask(__name__)
app.secret_key = "secret"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

create_tables()


# ---------------- CREATE ADMIN IF NOT EXISTS ----------------
conn = connect_db()
cur = conn.cursor()

cur.execute("SELECT * FROM users WHERE role='admin'")
admin = cur.fetchone()

if not admin:
    cur.execute(
        "INSERT INTO users(name,phone,email,password,role) VALUES(?,?,?,?,?)",
        ("Admin","9999999999","admin@gmail.com","admin123","admin")
    )
    conn.commit()

conn.close()


# ---------------- PDF REPORT FUNCTION ----------------
def generate_pdf_report(image_path, result, suggestions, pdf_path):

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Insect Damage Detection Report", styles["Title"]))
    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"<b>Prediction Result:</b> {result}", styles["Normal"]))
    elements.append(Spacer(1,10))

    elements.append(Paragraph(f"<b>Suggestions:</b> {suggestions}", styles["Normal"]))
    elements.append(Spacer(1,20))

    elements.append(Paragraph("<b>Uploaded Image:</b>", styles["Normal"]))
    elements.append(Spacer(1,10))

    img = Image(image_path, width=300, height=200)
    elements.append(img)

    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
    pdf.build(elements)


# ---------------- EMAIL FUNCTION ----------------
def send_detection_email(user_email, image_path, result, suggestions):

    print("Sending email to:", user_email)

    sender_email = "projectdemo348@gmail.com"
    sender_password = "ihxxyxaunntmqrep"   # Gmail App Password (NO SPACES)

    pdf_path = f"report_{user_email}.pdf"

    generate_pdf_report(image_path, result, suggestions, pdf_path)

    msg = EmailMessage()

    msg["Subject"] = "Insect Damage Detection Report"
    msg["From"] = sender_email
    msg["To"] = user_email

    msg.set_content(f"""
Hello,

Your insect damage detection result is ready.

Prediction Result: {result}

Suggestions:
{suggestions}

A detailed PDF report is attached.

Regards,
Insect Damage Detection System
""")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="Detection_Report.pdf"
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Email sending failed:", e)

@app.route("/")
def home():
    return render_template("landing.html")
# ---------------- HOME ----------------
@app.route("/register_page")
def register_page():
    return render_template("register.html")


# ---------------- USER LOGIN PAGE ----------------
@app.route("/login_page")
def login_page():
    return render_template("login.html")


# ---------------- ADMIN LOGIN PAGE ----------------
@app.route("/admin_login_page")
def admin_login_page():
    return render_template("admin_login.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    password = request.form["password"]

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    existing_user = cur.fetchone()

    if existing_user:
        conn.close()
        return "Email already registered. Please login."

    cur.execute(
        "INSERT INTO users(name,phone,email,password,role) VALUES(?,?,?,?,?)",
        (name, phone, email, password, "user")
    )

    conn.commit()
    conn.close()

    return redirect("/login_page")


# ---------------- USER LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=? AND role='user'",
        (email, password)
    )

    user = cur.fetchone()
    conn.close()

    if user:
        session["user"] = email
        return redirect("/dashboard")

    return "Invalid User Login"


# ---------------- ADMIN LOGIN ----------------
@app.route("/admin_login", methods=["POST"])
def admin_login():

    email = request.form["email"]
    password = request.form["password"]

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=? AND role='admin'",
        (email, password)
    )

    admin = cur.fetchone()
    conn.close()

    if admin:
        session["admin"] = email
        return redirect("/admin")

    return "Invalid Admin Login"


# ---------------- USER DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login_page")

    email = session["user"]

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM history WHERE email=? AND result='normal'", (email,))
    normal = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM history WHERE email=? AND result='moderate'", (email,))
    moderate = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM history WHERE email=? AND result='severe'", (email,))
    severe = cur.fetchone()[0]

    conn.close()

    return render_template(
        "user_dashboard.html",
        normal=normal,
        moderate=moderate,
        severe=severe
    )


# ---------------- ADMIN DASHBOARD ----------------
@app.route("/admin")
def admin():

    if "admin" not in session:
        return redirect("/admin_login_page")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM history")
    scans = cur.fetchone()[0]

    conn.close()

    return render_template("admin_dashboard.html", users=users, scans=scans)


# ---------------- HISTORY ----------------
@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/login_page")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT image, result FROM history WHERE email=?", (session["user"],))
    data = cur.fetchall()

    conn.close()

    return render_template("history.html", data=data)


# ---------------- PROFILE ----------------
@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login_page")

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT name, phone, email FROM users WHERE email=?", (session["user"],))
    user = cur.fetchone()

    conn.close()

    return render_template("profile.html", name=user[0], phone=user[1], email=user[2])


# ---------------- PREDICT ----------------
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if "user" not in session:
        return redirect("/login_page")

    if request.method == "POST":

        file = request.files["image"]

        if file.filename == "":
            return "No Image Selected"

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        result, prob = predict_image(path)

        normal = round(prob[0] * 100, 2)
        moderate = round(prob[1] * 100, 2)
        severe = round(prob[2] * 100, 2)

        suggestions = get_suggestions(result)

        conn = connect_db()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO history(email,image,result) VALUES(?,?,?)",
            (session["user"], file.filename, result)
        )

        conn.commit()
        conn.close()

        # Send email with PDF report
        send_detection_email(session["user"], path, result, suggestions)

        return render_template(
            "result.html",
            result=result,
            normal=normal,
            moderate=moderate,
            severe=severe,
            suggestions=suggestions,
            image=file.filename
        )

    return render_template("predict.html")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login_page")


if __name__ == "__main__":
    app.run(debug=True)