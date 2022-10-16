from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
def level_1():
    return render_template('index.html', num=3, color='rgb(159,197,248)')


@app.route('/play/<int:num>')
def level_2(num):
    return render_template('index.html', num=num, color='rgb(159,197,248)')

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template('index.html', num=num, color=color)


#ALWAYS INCLUDE!! 
if __name__=="__main__":
    app.run(debug=True)