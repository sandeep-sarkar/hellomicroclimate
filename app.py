
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! \n'

@app.route('/anotherhello')
def anotherhello():
    return 'Another Hello !! \n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
