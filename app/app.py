from flask import Flask, redirect, url_for, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    pass
      
if __name__ == '__main__':
  app.run(host='0.0.0.0', port="8000", debug=True)