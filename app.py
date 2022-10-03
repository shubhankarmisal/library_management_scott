from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='library'

mysql=MySQL(app)

@app.route("/home")
def home():
    cursor=mysql.connection.cursor()
    q='select * from library_table'
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('home.html',card=res)

@app.route("/header1")
def header_1():
    return render_template('header1.html')

@app.route("/header2")
def header_2():
    return render_template('header2.html')    

@app.route("/about")
def about():
    return render_template('about.html') 

@app.route("/admin")
def admin():
    return render_template('admin.html') 

@app.route("/dashboard")
def dashboard():
    cursor=mysql.connection.cursor()
    q='select * from library_table'
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('dashboard.html',user=res) 

@app.route("/add_books",methods=['GET','POST'])
def add_books():
    if request.method=='POST':
        fm=request.form
        a=fm['add_bookstxt']
        b=fm['authortxt']
        c=fm['datetxt']
        d=fm['descriptiontxt']
        e=fm['imgtxt']
        
        q="insert into library_table(book_name,author_name,date,image,description) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"')"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        print('Inserted Sucessfully')
        return redirect('/add_books')
    return render_template('add_books.html') 

@app.route("/add_books")
def f_books():
    cursor=mysql.connection.cursor()
    q='select * from library_table'
    cursor.execute(q)
    res=cursor.fetchall()
    return redirect('/add_books')
    return render_template('add_books.html',user=res)
    

@app.route("/search_books")
def search_books():
    cursor=mysql.connection.cursor()
    q="select * from library_table"
    if(q == 'library_table'):
        print('valid')
    else:
        print('Invalid')    
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('search_books.html',search=res)

@app.route("/orders/<string:id>")
def orders(id):
    cursor=mysql.connection.cursor()
    q="select * from library_table where id='"+id+"'"
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('orders.html',user=res)

@app.route("/feedback")
def feedback():
    cursor=mysql.connection.cursor()
    q='select * from feedback'
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('feedback.html',feed=res)  

@app.route("/add_user")
def add_user():
    return render_template('add_user.html')     

@app.route("/place_order")
def place_order():
    cursor=mysql.connection.cursor()
    q='select * from library_table'
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('place_order.html',order=res) 

@app.route("/contact",methods=['GET','POST'])
def contact():
    if request.method=='POST':
        fm=request.form
        a=fm['nametxt']
        b=fm['emailtxt']
        c=fm['descriptiontxt']
        
        q="insert into feedback(name,email,description) values('"+a+"','"+b+"','"+c+"')"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        print('Inserted Sucessfully')
        return redirect('/contact')

    return render_template('contact.html')     

@app.route("/delete/<string:id>")
def delete(id):
    q="delete from library_table where id='"+id+"'"
    cursor=mysql.connection.cursor()
    cursor.execute(q)
    mysql.connection.commit()
    return render_template('add_books.html')

@app.route('/edit/<string:eid>')
def edit(eid):
    cursor=mysql.connection.cursor()
    q="select * from library_table where id='"+eid+"'"
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('edit.html',user=res)    

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST' :
        fm=request.form
        a=fm['add_bookstxt']
        b=fm['authortxt']
        c=fm['datetxt']
        d=fm['descriptiontxt']
        e=fm['imgtxt']
        f=fm['id']
        q="update library_table set book_name='"+a+"',author_name='"+b+"',date='"+c+"',description='"+d+"',image='"+e+"' where id='"+f+"'"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        print("Save success")
        return redirect('/add_books')

            

app.run(debug=True)    