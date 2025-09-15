from flask import Flask, render_template, request, redirect, flash
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "super_secret_key_change_this_123"

# ===== Routes =====
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        whatsapp = request.form["whatsapp"]
        message = request.form["message"]

        # ===== Send Email =====
        try:
            sender = "vasanthakumar28042001@gmail.com"       # your Gmail
            password = "hnno yqiw rjjq pgdx"                 # Gmail App Password
            recipient = "vasanthakumar28042001@gmail.com"    # receiver email

            body = f"""
            📩 New Contact Form Submission:

            Name: {name}
            Email: {email}
            Phone: {phone}
            WhatsApp: {whatsapp}

            Message:
            {message}
            """

            msg = MIMEText(body, "plain", "utf-8")
            msg["Subject"] = "New Contact Message"
            msg["From"] = sender
            msg["To"] = recipient

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)

            flash("✅ Your message was sent successfully!", "success")
        except Exception as e:
            print("Email send failed:", e)
            flash("❌ Error sending your message. Try again later.", "danger")

        return redirect("/contact")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
