from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/device_<name>.html')
def device(name):
    return render_template("device.html",device=name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
