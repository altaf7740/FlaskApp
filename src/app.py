from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
	altaf-altaf
	return "hello world"

if __name__ == "__main__":
	app.run()
