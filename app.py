from flask import Flask


app = Flask(__name__)

@app.route("/") #localhost:portnumber


def home():
    return "this is Sample of the Ap0plication"



if __name__ == '__main__':
    app.run(debug = True)
