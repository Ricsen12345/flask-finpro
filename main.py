from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
  return "Hello World"

@app.route('/test')
def test():
  return jsonify({"message": "JSON response"})

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
