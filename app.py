from flask import Flask, render_template

app = Flask(__name__)

# Startsidan
@app.route('/')
def home():
    return render_template('index.html')

# Om-sidan
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)