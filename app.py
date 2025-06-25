from flask import Flask, render_template, request, redirect, url_for, session, flash
from send_notification import send_email_notification  # Import the email sending function
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')  # Set a secure secret key

# Mock users with hashed passwords
users = {
    "user1": generate_password_hash("pass123"),  # Example regular user (hashed)
    "admin": generate_password_hash("adminpass")  # Admin credentials (hashed)
}

@app.route('/')
def root():
    # Redirect to the home page
    return redirect(url_for('home'))

@app.route('/home')
def home():
    # Main page that links to other parts of the website
    return render_template('home.html')

@app.route('/about')
def about():
    # Renders the About page
    return render_template('about.html')

@app.route('/services')
def services():
    # Renders the Services page
    return render_template('services.html')

@app.route('/feedback')
def feedback():
    # Renders the Feedback page
    return render_template('feedback.html')

@app.route('/search')
def search():
    # Renders the Search page
    return render_template('search.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Clear any previous flash messages to avoid displaying them on the login page
    if 'login_success' in session or 'logout_message' in session:
        flash('')  # Clear any flash messages that were set in previous requests

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and password matches the hashed version
        if username in users and check_password_hash(users[username], password):
            # Set user session
            session['username'] = username
            flash("Login successful!", "success")  # Success message
            return redirect(url_for('home'))  # Redirect to home page after successful login
        else:
            flash("Invalid username or password.", "error")  # Error message

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session to log out
    session.pop('username', None)
    flash("You have been logged out.", "info")  # Info message on logout
    return redirect(url_for('home'))  # Redirect to home after logout

@app.route('/send_notification', methods=['POST'])
def send_notification():
    # Get the email address from the form input
    recipient_email = request.form.get('email')

    # Set the email subject and body
    subject = "Bus Schedule Updates"
    body = "You have successfully subscribed to live updates for your bus schedule."

    # Call the email function
    send_email_notification(recipient_email, subject, body)

    flash("Notification sent successfully!", "success")  # Show a success message
    return redirect(url_for('home'))  # Redirect back to home page after sending the notification

if __name__ == "__main__":
    app.run(debug=True)
