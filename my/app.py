from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

from data import data

# Context Processor to inject common data if needed (e.g., current year)
@app.context_processor
def inject_year():
    from datetime import datetime
    return {'year': datetime.now().year, 'data': data}

@app.route('/')
def index():
    return render_template('index.html', title="Home", data=data)

@app.route('/about')
def about():
    return render_template('about.html', title="About Me", data=data)

@app.route('/skills')
def skills():
    return render_template('skills.html', title="Skills", data=data)

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", data=data)

@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience", data=data)

@app.route('/certifications')
def certifications():
    return render_template('certifications.html', title="Certifications", data=data)

@app.route('/achievements')
def achievements():
    return render_template('achievements.html', title="Achievements", data=data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to a database
        # For this portfolio, we'll just flash a success message
        print(f"New Message from {name} ({email}): {message}") # Log to console
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', title="Contact Me")

if __name__ == '__main__':
    app.run(debug=True)
