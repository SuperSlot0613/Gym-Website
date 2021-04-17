from flask import Flask, redirect, render_template, request
import mysql.connector
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/contact',methods=['POST','GET'])
def contact():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="esd_sem4"
    )
    mycursor = mydb.cursor()
    if request.method=='POST':
        singup=request.form
        name=singup['name']
        email=singup['email']
        subject=singup['subject']
        message=singup['message']
        mycursor.execute("INSERT INTO `contact`(`name`, `email`, `subject`, `message`) VALUES (%s,%s,%s,%s)",(name,email,subject,message))
        mydb.commit()
        mycursor.close()
        return "YOUR QUESTION ENTER OUR DATABASE"


@app.route("/login")
def Login():
    return render_template('Login1.html')
@app.route('/logindb',methods=['POST','GET'])
def Loginpage():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="esd_sem4"
    )
    mycursor=mydb.cursor()
    mylogin=mydb.cursor()
    if request.method=='POST':
        singup=request.form
        username=singup['username']
        password=singup['password']
        mylogin.execute("INSERT INTO `logininfo`(`username`, `password`) VALUES (%s,%s)", (username, password))
        mycursor.execute("select *from register where username='"+username+"' and password='"+password+"'")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        if(count==1):
            return render_template('login-ecommerce.html')
        else:
            return render_template('Login1.html')
    mydb.commit()
    mycursor.close()
    mylogin.close()


@app.route("/register")
def Register():
    return render_template('register.html')

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="esd_sem4"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        singup=request.form
        fname=singup['fname']
        lname=singup['lname']
        email=singup['email']
        phone=singup['phone']
        date=singup['date']
        gender=singup['gender']
        username=singup['username']
        password=singup['password']
        mycursor.execute("INSERT INTO `register`(`fname`, `lname`, `email`, `phone`, `date`, `gender`, `username`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(fname,lname,email,phone,date,gender,username,password))
        mydb.commit()
        mycursor.close()
        return render_template('sucessful.html')


@app.route("/Emaded")
def Emadeb():
    return render_template('Emaded.html')

@app.route("/ecommerce")
def ecommerce():
    return render_template('ecommerce.html')

@app.route("/login-ecommerce")
def login_ecomm():
    return render_template('login-ecommerce.html')

@app.route("/Logged_in_product_page")
def login_product():
    return render_template('Logged_in_product_page.html')

@app.route("/logged_in_about_us")
def about():
    return render_template('logged_in_about_us.html')

@app.route("/logged_in_all_top_container")
def logged_in_all():
    return render_template('logged_in_all_top_container.html')

@app.route("/logged_in_for-each-image")
def logged_in_for_each():
    return render_template('logged_in_for-each-image.html')

@app.route("/payment")
def Payment():
    return render_template('payment.html')

@app.route('/DeviInfo',methods=['POST','GET'])
def DeviInfo():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="esd_sem4"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        singup=request.form
        name=singup['name']
        phone=singup['phone']
        pincode=singup['pincode']
        locality=singup['Locality']
        address=singup['Add']
        city=singup['city']
        state=singup['state']
        landmark=singup['landmarks']
        phone2=singup['phone2']
        mycursor.execute("INSERT INTO `deviinfo`(`name`, `phone`, `pincode`, `locality`, `address`, `city`, `state`, `landmark`, `phone2`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,phone,pincode,locality,address,city,state,landmark,phone2))
        mydb.commit()
        mycursor.close()
        return "YOUR ORDER IS RECIEVED"


if(__name__=="__main__"):
    app.run(debug=True)
