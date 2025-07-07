from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, session, flash
import hashlib, re, requests
from config import *  # Load configs

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)  # Initialize mail

# SQLAlchemy model
class RegistrationDetails(db.Model):
    __tablename__ = 'registration_details'
    registration_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    address = db.Column(db.Text, nullable=False)
    hobbies = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.Boolean, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        errors = []

        fname = data.get('first_name', '').strip()
        lname = data.get('last_name', '').strip()
        email = data.get('email', '').strip()
        pwd = data.get('password')
        cpwd = data.get('confirm_password')
        address = data.get('address', '').strip()
        hobbies = request.form.getlist('hobbies')
        gender = data.get('gender')
        terms = data.get('terms')

        if not all([fname, lname, email, pwd, cpwd, address, hobbies, gender, terms]):
            errors.append("All fields are required.")

        if len(fname) > 30 or len(lname) > 30:
            errors.append("Names must be less than 30 characters.")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")

        if len(pwd) < 6 or len(pwd) > 12 or pwd != cpwd:
            errors.append("Password must be 6‑12 characters and match.")

        if len(address.split()) < 15:
            errors.append("Address must contain at least 15 words.")

        if gender not in ('0', '1'):
            errors.append("Gender required.")

        if not terms:
            errors.append("You must accept the terms.")

        if RegistrationDetails.query.filter_by(email=email).first():
            errors.append("Email already exists.")

        if errors:
            return render_template('register.html', errors=errors, form=data, selected_hobbies=hobbies)

        hashed_pwd = hashlib.md5(pwd.encode()).hexdigest()
        hobby_csv = ','.join(hobbies)

        user = RegistrationDetails(
            first_name=fname,
            last_name=lname,
            email=email,
            password=hashed_pwd,
            address=address,
            hobbies=hobby_csv,
            gender=bool(int(gender))
        )
        db.session.add(user)
        db.session.commit()

        # Send confirmation email
        try:
            msg = Message(
                "Registration Successful",
                sender=app.config['MAIL_USERNAME'],
                recipients=[email]
            )
            msg.body = f"Hello {fname},\n\nThank you for registering. Your account has been successfully created!"
            mail.send(msg)
        except Exception as e:
            print(f"Error sending email: {e}")

        flash('Registration successful. Please log in.', 'success')
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
        user = RegistrationDetails.query.filter_by(email=email, password=pwd).first()
        if user:
            session['user_id'] = user.registration_id
            return redirect('/dashboard')
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    joke = response.json().get('joke', 'No joke found.')

    return render_template('dashboard.html', joke=joke)

@app.route('/new-joke')
def new_joke():
    headers = {'Accept': 'application/json'}
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    joke = response.json().get('joke', 'No joke found.')
    return jsonify({'joke': joke})

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Logged out successfully.", "info")
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
