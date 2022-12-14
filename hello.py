
import  flask
app  = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def hello_word():


    return{"HELLO":"mlind"}

if __name__ == '__main__':
        app.run()

