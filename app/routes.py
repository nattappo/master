from app import app
from flask import redirect,render_template,request,url_for
import sqlite3

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add')
def hello():
    return render_template('add.html')


@app.route('/delete/<string:id_data>',methods=["GET"])
def delete(id_data):
    con = sqlite3.connect('pusdu.sqlite3')
    with con:
        cursor = con.cursor()
        cursor.execute("delete from pasadu where ลำดับ = ? ",[id_data])
        con.commit()
        return redirect(url_for('Showfrom'))



@app.route("/show")   
def Showfrom():
    con = sqlite3.connect('pusdu.sqlite3')
    with con:
        cur = con.cursor()
        cur.execute('Select * from pasadu')
        rows = cur.fetchall()
        
    return render_template ('show.html',datas= rows)


@app.route("/insert",methods=["POST"])
def insert():
    if request.method=='POST':
        รายการ =request.form['รายการ']
        จำนวน =request.form['จำนวน']
        หน่วย =request.form['หน่วย']
    con = sqlite3.connect('pusdu.sqlite3')
    with con:
        cursor = con.cursor()
        sql = "Insert into pasadu (รายการ,จำนวน,หน่วย) values(?,?,?)"
        cursor.execute(sql,(รายการ,จำนวน,หน่วย))
        con.commit()
    return redirect(url_for('Showfrom'))


@app.route("/update",methods=["POST"])
def update():
    if request.method=='POST':
        ลำดับ =request.form['ลำดับ']
        รายการ =request.form['รายการ']
        จำนวน =request.form['จำนวน']
        หน่วย =request.form['หน่วย']
    con = sqlite3.connect('pusdu.sqlite3')
    with con:
        cursor = con.cursor()
        sql = "Update pasadu set รายการ=?,จำนวน=?,หน่วย=? Where ลำดับ=?"
        cursor.execute(sql,(รายการ,จำนวน,หน่วย,ลำดับ))
        con.commit()
    return redirect(url_for('Showfrom'))
    

    


if __name__ == "__main__":
    app.run(debug=True)