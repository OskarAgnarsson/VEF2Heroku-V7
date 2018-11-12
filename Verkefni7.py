from sys import argv
from bottle import *
import pymysql


@get("/")
def index():
    return template("index")

@route("/donyskra", method="POST")
def nyr():
    u = request.forms.get("user")
    p = request.forms.get("pass")
    n = request.forms.get("nafn")

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_verk7')
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM 1610013090_verk7.users WHERE user=%s",(u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("INSERT INTO 1610013090_verk7.users VALUES(%s,%s,%s)",(u,p,n))
        conn.commit()
        cur.close()
        conn.close()
        return u, "hefur verið skráður <br><a href='/'>Heim</a>"
    else:
        return u, "Er frátekið notandanafn, reyndu aftur <br> <a href='/'>Heim</a>"
    
@route("/doinnskra", method="POST")
def inn():
    u = request.forms.get("user")
    p = request.forms.get("pass")

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword', db='1610013090_verk7')
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM 1610013090_verk7.users WHERE user=%s AND pass=%s",(u,p))
    result = cur.fetchone()

    if result[0] == 1:
        cur.close()
        conn.close()
        return template("hallo",u=u)
    else:
        cur.close()
        conn.close()
        return "haha nice try <br> <a href='/'>Heim</a>"
    
##########################################
@error(404)
def villa(error):
    return "<h2>Error 404: Not Found</h2>"

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

run(host = "localhost", port = 8080, reloader = True)

#bottle.run(host="0.0.0.0", port=argv[1])
