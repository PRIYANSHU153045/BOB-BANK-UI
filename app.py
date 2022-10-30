
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/callcenter')
def callcenter():
   return render_template('callcenter.html')
   
@app.route('/voice')
def voice():
   return render_template('voice.html')







if __name__ == '__main__':
   app.run(debug = True)