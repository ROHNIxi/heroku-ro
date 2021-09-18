import pickle
from flask import Flask, render_template, request


app = Flask(__name__)
MyModel = pickle.load(open('titanic.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    pclass = int(request.form['pclass'])
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = int(request.form['fare'])
    gender = request.form['gender']
    embarked = request.form['embarked']

    s = 0
    q = 0
    if gender =='M':
        gender = 1
    else:
        gender = 0
    if embarked == "S":
        s = 1
        q = 0
    elif embarked =="Q":
        s = 0
        q = 1
    else:
        s = 0
        q = 0
            
    prediction = MyModel.predict([[pclass,age,sibsp,parch,fare,gender,q,s]])[0]

    if prediction == 0:
        prediction = "They did not survive"
    else:
        prediction = "Yes survived"

    return render_template('index.html', output=prediction)

if __name__ == '__main__':
    app.run(debug=True)
    
