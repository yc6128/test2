from flask import Flask 	#1
app = Flask(__name__) 		#2

@app.route("/") 		#3
def hello():			#4
    return "Hello World!"

if __name__ == "__main__": 	#5
    app.run()