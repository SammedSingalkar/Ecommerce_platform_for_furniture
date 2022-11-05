import re
from datetime import date
from pathlib import Path

from flask_mail import Mail
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os.path

app = Flask(__name__)
app.secret_key = 'i am sammed'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Iamsammed@12'
app.config['MYSQL_DB'] = 'ecommerce_platform'

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME='sammedsingalkar@gmail.com',
    MAIL_PASSWORD='yourmailapppass'
)
mail = Mail(app)
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data = cursor.fetchone()
        for i, j in data.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"

    else:
        img = "unnamed"
    return render_template('index.html', img=img)


@app.route('/product', methods=['GET', 'POST'])
def product():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data6 = cursor.fetchone()
        for i, j in data6.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"
    else:
        img = "unnamed"
    if request.method == 'POST':
        if request.form.get('couch') == 'couch':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from product where typed = 'couch' ")
            data = cursor.fetchall()
        elif request.form.get('teapoy') == 'teapoy':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from product where typed = 'teapoy' ")
            data = cursor.fetchall()
        elif request.form.get('bed') == 'bed':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from product where typed = 'bed' ")
            data = cursor.fetchall()
        elif request.form.get('dressing') == 'dressing table':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from product where typed = 'dressing table' ")
            data = cursor.fetchall()
        elif request.form.get('dinning') == 'dinning_table':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from product where typed = 'dinning table' ")
            data = cursor.fetchall()
        elif request.form.get('cuboard') == 'cuboard':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from product where typed = 'cuboard' ")
            data = cursor.fetchall()
    return render_template('product.html', data=data,img=img)


@app.route('/about')
def about():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data = cursor.fetchone()
        for i, j in data.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"
    else:
        img = "unnamed"
    return render_template('about.html', img=img)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    global data, count, total
    if session.get('loggedin') == True:
        if 'email' in session:
            email = session['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('select * from cart where email = %s', (email,))
            data = cursor.fetchall()
            count = cursor.execute('SELECT * FROM cart where email = %s',(email,))
            cursor.execute('select name from user where email = %s', (email,))
            data1 = cursor.fetchone()
            for i, j in data1.items():
                img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"
            cursor.execute('select sum(quantity * price) from cart where email = %s',(email,))
            total = cursor.fetchone()
            for k,v in total.items():
               total = v
            print(total)

            if request.method == 'POST' and 'Remove item' in request.form or 'wishlist' in request.form:
                try:
                    button = request.form['Remove item']
                    if request.form.get('Remove item') == button:
                        cursor.execute("DELETE FROM cart WHERE email = %s and srno = %s", (email, button,))
                        mysql.connection.commit()
                except:
                    button = request.form['wishlist']
                    if request.form.get('wishlist') == button:
                        cursor.execute('select product_name,no from cart where srno = %s', (button,))
                        productname = cursor.fetchone()
                        prod = productname['product_name']
                        number = productname['no']
                        cursor.execute('INSERT INTO wishlist VALUES (null,%s,%s,%s)', (number, email, prod,))
                        mysql.connection.commit()
            elif request.method == 'POST' and 'srno' in request.form:
                srno = request.form['srno']
                quantity = request.form['quantity']
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute(
                    "UPDATE cart SET quantity = %s WHERE email = %s and srno = %s",
                    (quantity,email,srno,))
                mysql.connection.commit()
                # print(srno)
                # print(quantity)


    else:
        img = "unnamed"
        return redirect('login')
    return render_template('cart.html', data=data, count=count, img=img,total=total)


@app.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    if session.get('loggedin') == True:
        if 'email' in session:
            email = session['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('select * from wishlist where email = %s', (email,))
            data = cursor.fetchall()
            today = date.today()
            Date = today.strftime("%B %d, %Y")
            cursor.execute('select name from user where email = %s', (email,))
            data1 = cursor.fetchone()
            for i, j in data1.items():
                img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"
        else:
            img = "unnamed"
            if request.method == 'POST':
                email = session['email']
                Delete = request.form['delete']
                if request.form.get('delete') == Delete:
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute("DELETE FROM wishlist WHERE email = %s and srno = %s", (email, Delete,))
                    mysql.connection.commit()
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('wishlist.html', data=data, Date=Date, img=img)


@app.route('/shop')
def shop():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from product where typed = 'couch' ")
    data = cursor.fetchall()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from product where typed = 'teapoy' ")
    data1 = cursor.fetchall()
    cursor.execute("select * from product where typed = 'bed' ")
    data2 = cursor.fetchall()
    cursor.execute("select * from product where typed = 'dressing table' ")
    data3 = cursor.fetchall()
    cursor.execute("select * from product where typed = 'dinning table' ")
    data4 = cursor.fetchall()
    cursor.execute("select * from product where typed = 'cuboard' ")
    data5 = cursor.fetchall()
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data6 = cursor.fetchone()
        for i, j in data6.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"
    else:
        img = "unnamed"

    return render_template('shop.html', data=data, data1=data1, data2=data2, data3=data3, data4=data4, data5=data5,
                           img=img)


@app.route("/product_detail<int:srno>", methods=['GET', 'POST'])
def product_detail(srno):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select * from product where srno = %s', (srno,))
    data = cursor.fetchone()
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data6 = cursor.fetchone()
        for i, j in data6.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"
    else:
        img = "unnamed"

    if request.method == 'POST':
        if session.get('loggedin') == True:
            if 'email' in session:
                email = session['email']
                if request.form.get('wishlist') == 'Add to Wishlist':
                    cursor.execute('select name from product where srno = %s', (srno,))
                    productname = cursor.fetchone()
                    prod = productname['name']
                    cursor.execute('INSERT INTO wishlist VALUES (null,%s, %s, %s)', (srno, email, prod,))
                    mysql.connection.commit()
                elif request.form.get('cart') == 'Add to cart':
                    cursor.execute('select name,color,price from product where srno = %s', (srno,))
                    product = cursor.fetchone()
                    name = product['name']
                    color = product['color']
                    price = product['price']
                    quantity = 1
                    cursor.execute('INSERT INTO cart VALUES (null, %s, %s, %s, %s, %s, %s)',
                                   (srno, email, name, color, price,quantity,))
                    mysql.connection.commit()
                elif request.form.get('buynow') == 'Buy Now':
                    q = request.form['quantity']
                    session['srno'] = srno
                    session['quauntity'] = q
                    return redirect('/payment_gateway')
        else:
            return redirect('/login')

    return render_template('product_detail.html', data=data, img=img)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if session.get('loggedin') == True:
        return redirect('/dashboard')
    elif request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()

        # If account exists in accounts table in out database
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            session['password'] = account['password']
            return redirect('/dashboard')
        else:
            msg = 'Incorrect email/password!'
    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form and 'mobile-number' in request.form:
        # Create variables for easy access
        username = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        email = request.form['email']
        number = request.form['mobile-number']
        memebership = "NO"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        # If account exists show error and validation checks

        if account:
            msg = 'Account already exists!'
        elif confirm_password != password:
            msg = "Password doesn't match"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not number:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO user VALUES (%s, %s, %s, %s, %s)',
                           (username, email, password, number, memebership,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data = cursor.fetchone()
        for i, j in data.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('dashboard.html', img=img)


@app.route('/login/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('email', None)
    return redirect('/')


@app.route('/seller/logout')
def seller_logput():
    # Remove session data, this will log the user out
    session.pop('login', None)
    session.pop('email', None)
    return redirect('/')


@app.route('/profile')
def profile():
    if session.get('loggedin') == True:
        if 'email' in session:
            email = session['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
            data = cursor.fetchone()

            cursor.execute('select name from user where email = %s', (email,))
            data1 = cursor.fetchone()
            for i, j in data1.items():
                img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('profile.html', data=data)


@app.route('/addresses', methods=['GET', 'POST'])
def addresses():
    if session.get('loggedin') == True:
        if 'email' in session:
            email = session['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM addresses WHERE email = %s', (email,))
            data = cursor.fetchall()
            cursor.execute('select name from user where email = %s', (email,))
            data1 = cursor.fetchone()
            for i, j in data1.items():
                img = j
                path_to_file = f'static\img\profile\{img}.jpg'
                path = Path(path_to_file)

                if path.is_file():
                    print(f'The file {path_to_file} exists')
                else:
                   print(f'The file {path_to_file} does not exist')
                   img = "unnamed"

            if request.method == 'POST':
                try:
                    number = request.form['remove']
                    if request.form.get('remove') == number:
                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                        cursor.execute("DELETE FROM addresses where srno = %s and email = %s", (number, email,))
                        mysql.connection.commit()
                        # flash('Deleted successful')
                except:
                    pass
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('addresses.html', data=data, img=img)


@app.route('/add_address', methods=['GET', 'POST'])
def add_address():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data = cursor.fetchone()
        for i, j in data.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"

        if request.method == 'POST' and 'name' in request.form and 'mn' in request.form and 'pin' in request.form and 'state' in request.form and 'landmark' in request.form and 'city' in request.form:
            email = session['email']
            # print(email)
            username = request.form['name']
            # print(username)
            number = request.form['mn']
            pin = request.form['pin']
            state = request.form['state']
            landmark = request.form['landmark']
            city = request.form['city']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO addresses VALUES (null,%s, %s, %s, %s, %s, %s, %s)',
                           [username, number, pin, state, email, landmark, city, ])
            mysql.connection.commit()
            msg = 'You have successfully registered!'
        elif request.method == 'POST':
            msg = 'Please fill out the form!'
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('add_address.html', msg=msg, img=img)


@app.route('/edit_address<int:srno>', methods=['GET', 'POST'])
def edit_addresss(srno):
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addresses WHERE email = %s', (email,))
        data = cursor.fetchone()
        cursor.execute('select name from user where email = %s', (email,))
        data1 = cursor.fetchone()
        for i, j in data1.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"

        if request.method == 'POST' and 'name' in request.form and 'mobile' in request.form and 'pincode' in request.form and 'state' in request.form and 'landmark' in request.form and 'city' in request.form:
            name = request.form['name']
            email = session['email']
            phone = request.form['mobile']
            pincode = request.form['pincode']
            state = request.form['state']
            landmark = request.form['landmark']
            city = request.form['city']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE addresses SET name = %s, mobile_number  = %s, pincode = %s, state = %s, Landmark = "
                           "%s, city = %s WHERE email = %s and srno = %s",
                           (name, phone, pincode, state, landmark, city, email, srno,))
            mysql.connection.commit()
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('edit_address.html', data=data, img=img)


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM orders WHERE email = %s order by order_date DESC', (email,))
        data = cursor.fetchall()
        cursor.execute('select name from user where email = %s', (email,))
        data1 = cursor.fetchone()
        for i, j in data1.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('orders.html', data=data, img=img)


@app.route('/pricing')
def pricing():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select membership from user where email = %s', (email,))
        prime = cursor.fetchone()
        prime = prime['membership']
        if (prime == "NO"):
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('select name from user where email = %s', (email,))
                data6 = cursor.fetchone()
                for i, j in data6.items():
                    img = j
                path_to_file = f'static\img\profile\{img}.jpg'
                path = Path(path_to_file)

                if path.is_file():
                    print(f'The file {path_to_file} exists')
                else:
                    print(f'The file {path_to_file} does not exist')
                    img = "unnamed"
                return render_template('pricing.html',img=img)
        else:
            return redirect('/benefit')
    else:
        return redirect('/login')


@app.route('/benefit')
def benefit():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data = cursor.fetchone()
        for i, j in data.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('benefit.html', data=data)


@app.route("/invoice<int:order_no>", methods=['GET', 'POST'])
def invoice(order_no):
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM orders WHERE order_no = %s and email = %s', (order_no, email,))
        data = cursor.fetchone()
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        data1 = cursor.fetchone()
        cursor.execute('SELECT * FROM addresses WHERE email = %s', (email,))
        data2 = cursor.fetchone()
        # download = pdfkit.from_file("/invoice<int:order_no>", 'out.pdf')
        cursor.execute('select name from user where email = %s', (email,))
        data3 = cursor.fetchone()
        for i, j in data3.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"

    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('invoice_order.html', data=data, data1=data1, data2=data2,img=img)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select name from user where email = %s', (email,))
        data6 = cursor.fetchone()
        for i, j in data6.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"
    else:
        img = "unnamed"
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'subject' in request.form and 'message' in request.form:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO contact VALUES (null,%s, %s, %s, %s)', [name, email, subject, message, ])
        mysql.connection.commit()
        mymail = "sammedsingalkar@gmail.com"
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[mymail],
                          body=subject + "\n" + message
                          )
    return render_template('contact.html',img=img)


@app.route('/seller_login', methods=['GET', 'POST'])
def seller_login():
    msg = ''
    if session.get('login') == True:
        return redirect('/seller_dashboard')
    elif request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM seller WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()

        # If account exists in accounts table in out database
        if account:
            session['login'] = True
            session['email'] = account['email']
            session['password'] = account['password']
            return redirect('/seller_dashboard')
        else:
            msg = 'Incorrect email/password!'
    return render_template('seller/seller_login.html', msg=msg)


@app.route('/seller_dashboard')
def seller_dashboard():
    if session.get('login') == True:
        email = session['email']
        # seller_orders
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        orders = cursor.execute('SELECT * FROM seller_orders WHERE email = %s', (email,))
        customer = cursor.execute('SELECT distinct(user_email) FROM seller_orders WHERE email = %s', (email,))
        cursor.execute('SELECT sum(quantity * amount) FROM seller_orders WHERE email = %s', (email,))
        revenue = cursor.fetchone()
        cursor.execute('SELECT sum(quantity) FROM seller_orders WHERE email = %s', (email,))
        quantity = cursor.fetchone()

        for k, v in revenue.items():
            revenue = v

        for i, j in quantity.items():
            quantity = j
    else:
        return redirect('seller_login')
    return render_template('seller/dashboard.html', orders=orders, customer=customer, revenue=revenue,
                           quantity=quantity)


@app.route('/seller_register', methods=['GET', 'POST'])
def seller_register():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form and 'mobile-number' in request.form and 'gst_no' in request.form:
        # Create variables for easy access
        username = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        email = request.form['email']
        number = request.form['mobile-number']
        gst = request.form['gst_no']
        shop = request.form['shop_name']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM seller WHERE email = %s', (email,))
        account = cursor.fetchone()
        cursor.execute('SELECT * FROM seller WHERE GST_NO = %s', (gst,))
        gst_no = cursor.fetchone()
        # If account exists show error and validation checks

        if account:
            msg = 'Account already exists!'
        elif gst_no:
            msg = 'GST NO already registered'
        elif confirm_password != password:
            msg = "Password doesn't match"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not number:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO seller VALUES (null, %s, %s, %s, %s, %s, %s)',
                           (username, shop, email, password, number, gst,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('seller/seller_register.html', msg=msg)


@app.route('/seller_profile')
def seller_profile():
    if session.get('login') == True:
        if 'email' in session:
            email = session['email']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM seller WHERE email = %s', (email,))
            data = cursor.fetchone()
        return render_template('seller/profile.html', data=data)
    return redirect('/seller_login')


@app.route('/seller_orders', methods=['GET', 'POST'])
def seller_orders():
    if session.get('login') == True:
        email = session['email']
        status = 'pending'
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM seller_orders WHERE email = %s and status = %s', (email, status,))
        data = cursor.fetchall()
        cursor.execute('SELECT * FROM seller_orders WHERE email = %s and status != %s', (email, status,))
        data1 = cursor.fetchall()
        # cursor.execute('SELECT name FROM user WHERE email = %s', (email,))
        # name = cursor.fetchall()

        if (request.method == 'POST'):
            try:
                button = request.form['approved']
                if request.form.get('approved') == button:
                    status = "Approved"
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute("UPDATE seller_orders SET status = %s WHERE order_no = %s", (status, button,))
                    mysql.connection.commit()
            except:
                button = request.form['rejected']
                if request.form.get('rejected') == button:
                    status = "Rejected"
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute("UPDATE seller_orders SET status = %s WHERE order_no = %s", (status, button,))
                    mysql.connection.commit()

    else:
        return redirect('/seller_login')
    return render_template('seller/orders.html', data=data, data1=data1)


@app.route('/payment_methods', methods=['POST', 'GET'])
def payment_methods():
    global data, data1
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        data = cursor.fetchone()

        cursor.execute('select name from user where email = %s', (email,))
        data2 = cursor.fetchone()
        for i, j in data2.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"

        cursor.execute('SELECT * FROM payment WHERE email = %s', (email,))
        data1 = cursor.fetchall()

        if request.method == 'POST':
            try:
                number = request.form['delete']
                if request.form.get('delete') == number:
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute("DELETE FROM payment where srno = %s", (number,))
                    mysql.connection.commit()
            except:
                pass
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('payment.html', data=data, data1=data1,img=img)


@app.route('/payment_gateway', methods=['POST', 'GET'])
def payment_gateway():
    global data, data1, quantity
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM payment WHERE email = %s', (email,))
        data = cursor.fetchall()

        quantity = session['quauntity']
        quantity = int(quantity)
        srno = session['srno']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM product WHERE srno = %s', (srno,))
        data1 = cursor.fetchone()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM payment WHERE email  = %s', (email,))
        detail = cursor.fetchone()
        # print(data1)

        cursor.execute('select name from user where email = %s', (email,))
        data4 = cursor.fetchone()
        for i, j in data4.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"

        if request.method == 'POST' and 'card' in request.form:
            id = request.form['card']
            if request.form.get('card') == id:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM payment WHERE email  = %s and srno = %s', (email, id,))
                detail = cursor.fetchone()
                return render_template('payment_gateway.html', data=data, data1=data1, quantity=quantity, detail=detail)
        elif request.method == 'POST' and 'order' in request.form:
            if request.form.get('order') == 'confirm':
                product = request.form['product']
                quant = request.form['quan']
                amount = request.form['amount']
                today = date.today()
                status = "pending"
                method = "COD/POD"
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('INSERT INTO orders VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s)',
                               (srno, email, product, today, status, amount, quant, method,))
                mysql.connection.commit()
                cursor.execute('SELECT seller_id  FROM product WHERE name = %s ', (product,))
                ID = cursor.fetchone()
                for k, v in ID.items():
                    id = v
                # print(type(id))
                cursor.execute('select email from seller where id = %s', (id,) )
                u_email = cursor.fetchone()
                for i, j in u_email.items():
                    user_email = j
                # print(email)
                # print(id)
                cursor.execute('INSERT INTO seller_orders VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s)',
                               (srno, email, user_email, product, today, status, amount, quant,))
                mysql.connection.commit()
                 # = cursor.fetchone()

    else:
        img="unnamed"
        return redirect('/login')
    return render_template('payment_gateway.html', data=data, data1=data1, quantity=quantity, detail=detail,img=img)


@app.route('/edit_details', methods=['POST', 'GET'])
def edit_details():
    global data
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        data = cursor.fetchone()
        cursor.execute('select name from user where email = %s', (email,))
        data2 = cursor.fetchone()
        for i, j in data2.items():
            img = j
            path_to_file = f'static\img\profile\{img}.jpg'
            path = Path(path_to_file)

            if path.is_file():
                print(f'The file {path_to_file} exists')
            else:
                print(f'The file {path_to_file} does not exist')
                img = "unnamed"
        if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'phone' in request.form and 'password' in request.form:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            password = request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("UPDATE user SET name = %s, mobile_no = %s, password = %s WHERE email = %s",
                           (name, phone, password, email,))
            mysql.connection.commit()
    else:
        img = "unnamed"
        return redirect('/login')
    return render_template('edit_details.html', data=data,img=img)


@app.route('/return', methods=['POST', 'GET'])
def ret():
    return render_template('return.html')


@app.route('/add_products', methods=['POST', 'GET'])
def add_products():
    msg = ''
    if session.get('login') == True:
        # email = session['email']
        if request.method == 'POST':
            # Create variables for easy access
            email = session['email']

            model = request.form['model']
            name = request.form['name']
            type = request.form['type']
            brand = request.form['company']
            style = request.form['style']
            room_type = request.form['room_type']
            fabric_type = request.form['fab']
            color = request.form['color']
            capacity = request.form['capacity']
            shape = request.form['shape']
            frame_material = request.form['material']
            special_feature = request.form['feature']
            about = request.form['about']
            product_type = request.form['product']
            price = request.form['price']
            mrp = request.form['mrp']

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute('SELECT ID FROM seller WHERE email = %s', (email,))
            # account = cursor.fetchone()
            cursor.execute('INSERT INTO product VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '
                           '%s, %s)',
                           (model, name, type, brand, style, room_type, fabric_type, color, capacity, shape,
                            frame_material, special_feature, about, product_type, price, mrp,))
            mysql.connection.commit()
            # msg = 'You have successfully registered!'
    else:
        return redirect('/seller_login')
    return render_template('seller/add_product.html')


@app.route('/seller_product', methods=['POST', 'GET'])
def seller_product():
    if session.get('login') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT ID FROM seller WHERE email = %s', (email,))
        data = cursor.fetchone()
        for k, v in data.items():
            data = v
        # print(data)
        cursor.execute('SELECT * FROM product WHERE seller_id = %s', (data,))
        data = cursor.fetchall()

        # if request.method == 'POST':
        #     number = request.form['delete']
        #     if request.form.get('delete') == number:
        #         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #         cursor.execute("DELETE FROM product where srno = %s", (number,))
        #         mysql.connection.commit()

    else:
        return render_template('/seller_login')
    return render_template('seller/seller_product.html', data=data)


@app.route('/edit_product<int:srno>', methods=['POST', 'GET'])
def edit_product(srno):
    print(srno)
    if session.get('login') == True:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM product WHERE seller_id = %s', (srno,))
        data = cursor.fetchone()
        if request.method == 'POST':
            # Create variables for easy access
            email = session['email']

            model = request.form['model']
            name = request.form['name']
            type = request.form['type']
            brand = request.form['company']
            style = request.form['style']
            room_type = request.form['room_type']
            fabric_type = request.form['fab']
            color = request.form['color']
            capacity = request.form['capacity']
            shape = request.form['shape']
            frame_material = request.form['material']
            special_feature = request.form['feature']
            about = request.form['about']
            product_type = request.form['product']
            price = request.form['price']
            mrp = request.form['mrp'],
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                "UPDATE product SET name = %s, type = %s, brand = %s, style = %s, Room_type = %s, fabric_type "
                "= %s, color = %s, seating_capacity = %s, shape = %s, frame_material = %s, "
                "speacial_feature = %s, about = %s, price = %s, original_price = %s  WHERE "
                "srno = %s",
                (name, type, brand, style, room_type, fabric_type, color, capacity, shape,
                 frame_material, special_feature, about, price, mrp, srno,))
        mysql.connection.commit()

    return render_template('seller/edit_product.html', data=data)


@app.route('/product_payment', methods=['POST', 'GET'])
def product_payment():
    if session.get('loggedin') == True:
        email = session['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM payment WHERE email = %s', (email,))
        data = cursor.fetchall()

        cursor.execute('SELECT * FROM cart WHERE email = %s', (email,))
        data1 = cursor.fetchall()

        cursor.execute('select name from user where email = %s', (email,))
        data2 = cursor.fetchone()
        for i, j in data2.items():
            img = j
        path_to_file = f'static\img\profile\{img}.jpg'
        path = Path(path_to_file)
        if path.is_file():
            print(f'The file {path_to_file} exists')
        else:
            print(f'The file {path_to_file} does not exist')
            img = "unnamed"

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM payment WHERE email  = %s', (email,))
        detail = cursor.fetchone()


        cursor.execute('select sum(quantity * price) from cart where email = %s', (email,))
        total = cursor.fetchone()
        for k, v in total.items():
            total = v
        # print(total)
        if request.method == 'POST' and 'card' in request.form:
            id = request.form['card']
            if request.form.get('card') == id:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM payment WHERE email  = %s and srno = %s', (email, id,))
                detail = cursor.fetchone()
                return render_template('product_payment.html', data=data, data1=data1,detail=detail,total=total,img=img)
        # elif request.method == 'POST':
        #     if request.form.get('order') == 'confirm':
                # product = request.form['product']
                # quant = request.form['quan']
                # amount = request.form['amount']
                # today = date.today()
                # status = "pending"
                # method = "COD/POD"
                # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                # cursor.execute('INSERT INTO orders VALUES (null,srno,email,product_name,quantity,amount,today,status,payment_method,) select srno,email,product_name,quantity,price from cart where email = %s',(today,status,method,email,))

                # cursor.execute('INSERT INTO orders VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s)',
                #                (srno, email, product, today, status, amount, quant, method,))
                # mysql.connection.commit()


    else:
        return redirect('/login')
    return render_template('product_payment.html', data=data, data1=data1,total=total,detail=detail,img=img)


if __name__ == '__main__':
    app.run(debug=True)
