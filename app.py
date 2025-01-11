from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from forms import CalculatorForm
from slovom_converter import input_split, cents_convert

app = Flask(__name__)

app.config["SECRET_KEY"] = "de1b186fd8549aec065f0bd98f2d5d28"


@app.route('/')
@app.route('/home')
def home():
	return render_template("index.html")


@app.route('/calculator', methods=["GET", "POST"])
def calculator():
	form = CalculatorForm()
	if request.method == "POST":
		amount = request.form["amount"]
		return render_template("calculator.html", amount=input_split(amount), form=form)
	else:
		return render_template("calculator.html", title="calculator", form=form)
	
#@app.route('/.well-known/pki-validation/<filename>')
#def serve_validation_file(filename):
#    return send_from_directory('.well-known/pki-validation', filename)


if __name__ == '__main__':
	app.run(debug=True)
