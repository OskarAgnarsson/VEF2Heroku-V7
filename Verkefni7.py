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

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1610013090', passwd='mypassword')
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM 1610013090_verk7.users WHERE user=%s",(u))
    result = cur.fetchone()
    
##########################################
@error(404)
def villa(error):
    return "<h2>Error 404: Not Found</h2>"

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

run(host = "localhost", port = 8080, reloader = True)

#bottle.run(host="0.0.0.0", port=argv[1])
