from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Here build the castle belong to YOURSELF!', name='Raphael',middle='NEXUS')

if __name__ == '__main__':
    app.run(debug=True)