from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, We are Sunshine & Yu ~!\nP.S.任桀是胖子!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
