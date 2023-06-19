from flask import Flask,render_template
# from mtgsdk import Card  |  this is needed to display card set information

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/sets')
def sets():
    return render_template('sets.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/trade')
def trade():
    return render_template('trade.html')

if __name__=="__main__":
    app.run(debug=True)
