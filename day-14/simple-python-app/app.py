from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this project is implemented to brush up on the AWS managed CI/CD services!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

