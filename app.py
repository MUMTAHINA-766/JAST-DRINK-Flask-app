from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)
 ######################Mysql###############################
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'menglv766'
app.config['MYSQL_DB'] = 'jast_drink'
 
mysql = MySQL(app)
 
@app.route('/justDrink/', methods = ['POST'])
def reserve():
     
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phoneNumber']
        address = request.form['address']
        # date = request.form['date']
        # time = request.form['time']
        # message = request.form['message']
        cursor = mysql.connection.cursor()
        cursor.execute(' INSERT INTO reservation VALUES(%s,%s,%s,%s)',(name,email,phone,address))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

##################page link#############
@app.get("/")
def index_get():
    return render_template("base.html")

@app.route('/about/')
def about():
    return render_template('about.html')


@app.get("/index")
def new_index():
    return render_template("index.html")

@app.route('/justDrink/')
def coffeeStore():
    return render_template('justDrink.html')
@app.route('/specialDishes')
def specialDishes():
    return render_template('special-dishes.html')
@app.route('/reservation',methods=['GET','POST'])
def reservation():
       if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phoneNumber']
            address = request.form['address']
            # date = request.form['date']
            # time = request.form['time']
            # message = request.form['message']
            cursor = mysql.connection.cursor()
            cursor.execute(' INSERT INTO reservation VALUES(%s,%s,%s,%s)',(name,email,phone,address))
            mysql.connection.commit()
            cursor.close()
            return render_template('reservation.html')

       else:
        return render_template('reservation.html')
    
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/menulist')
def menulist():
    return render_template('menulist.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)