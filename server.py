from flask import Flask
app = Flask (__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"
    
@app.route("/say/<name>")
def say(name):
    return "Hi " + name+"!"

@app.route("/repeat/<b>/<a>")
def repeat(b, a):
    
    return (a +" ")* int(b) +' '+ b +' '+ "times"
    

if __name__ == "__main__":
    app.run(debug=True)