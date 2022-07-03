from crypt import methods
from unicodedata import name
from flask import Flask
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Hello Starting machine learning project"




if __name__ == "__main__":
    app.run(debug=True)

