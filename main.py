from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Route 1: Initial Route
@app.route('/')
@app.route('/start')
def start():
    user_id = 42
    order_total = 79.99
    # Redirect to 'next_step' with parameters
    return redirect(url_for('next_step', user_id=user_id, order_total=order_total))

# Route 2: Receiving Route
@app.route('/next_step/<int:user_id>/<float:order_total>', methods=['GET', 'POST'])
def next_step(user_id, order_total):
    if request.method == 'POST':
        # Process form data if needed
        pass
    # Render a template and pass the parameters to it
    return render_template('next_step.html', user_id=user_id, order_total=order_total)


if __name__ == "__main__":
    #with app.app_context():
        #db.create_all()
    app.run(debug=True)
