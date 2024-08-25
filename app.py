from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/riyaz', methods=['GET'])
def riyaz():
    return 'The goat is here babyyy!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Access form data using request.form
        try:
            maths = float(request.form.get('maths', 0))
            science = float(request.form.get('science', 0))
            history = float(request.form.get('history', 0))

            average = (maths + science + history) / 3
        except ValueError:
            # Handle the case where conversion to float fails
            average = None

        return render_template('form.html', score=average)
    
    return render_template('form.html', score=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
