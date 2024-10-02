from flask_mysqldb import MySQL
from flask import Flask, render_template, request

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='chiku@123'
app.config['MYSQL_DB']='mi'

dp=MySQL(app)


@app.route('/')
def fub():
    return render_template('Home_Restau.html')

@app.route('/g')
def fuv():
    return render_template('Menu.html')

@app.route('/i')
def cub():
    return render_template('Projects.html')

@app.route('/j')
def duv():
    return render_template('About.html')

@app.route('/k')
def fux():
    return render_template('Contact.html')

@app.route('/l')
def cun():
    return render_template('Book.html')

@app.route('/m')
def sun():
    return render_template('All.html')

@app.route('/n')
def syb():
    return render_template('Gas.html')

@app.route('/o')
def rub():
    return render_template('Farm.html')

@app.route('/p')
def suc():
    return render_template('GJ.html')

@app.route('/q')
def sy():
    return render_template('Services.html')

@app.route('/r')
def sv():
    return render_template('Team.html')


@app.route('/a',methods=['POST'])
def fua():
    emh=request.form['email_home']
    nac=request.form['name_c']
    emc=request.form['email_c']
    mec=request.form['message_c']
    dab = request.form['date_b']
    tib = request.form['time_b']
    nub = request.form['number_b']
    reb = request.form['request_b']
    conn=dp.connection.cursor()
    conn.execute('insert into student(email_home,name_co,email_co,mes_co,datee_bo,timee_bo,num_bo,req_bo) values(%s,%s,%s,%s,%s,%s,%s,%s)',(emh,nac,emc,mec,dab,tib,nub,reb))
    dp.connection.commit()
    conn.close()
    return render_template('Thanks.html')

app.run(debug=True,port=48849)