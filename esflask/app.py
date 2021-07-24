from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["get"])
def get():
    return render_template("index.html")


@app.route("/co2", methods = ["get"])
def co2():
    return render_template("test.html")

@app.route("/sea_t", methods = ["get"])
def st():
    return render_template("test1.html")

@app.route("/atmo_t", methods = ["get"])
def at():
    return render_template("test2.html")

@app.route("/height", methods = ["get"])
def height():
    return render_template("test3.html")
    
@app.route("/total", methods = ["get"])
def total():
    return render_template("total.html")

if __name__ =="__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")