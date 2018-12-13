##pyhon web Api
import sys
from bottle import Bottle, run, template,response ,get,post,request,route, static_file,error,auth_basic
import json
import mysql.connector
import datetime
sys.path.append('system/config/')
import appconfig 

conn = mysql.connector.connect(**appconfig.config['database'])
##intialize web server
app  = Bottle()
##define methods
def authUser(usr,pw):
    if appconfig.config['api_users']['username'] == usr and appconfig.config['api_users']['password']  == pw :
        if request.get_header("x-api-key",None) != None:
             apikey =  request.get_header("x-api-key",None)
             query = ("Select * From staff ")

             cursor = conn.cursor(buffered = True)
             try:
                 cursor.execute(query)
                 return True
             except mysql.connector.Error as error:
                 print("failed executing query",error)
    return False
@route("/")
def index():
    return "<h1> Welcome to my web Api </h1>"
@auth_basic(authUser)
@route("/userlogin")
def user_login():
     response.content_type = "application/json"
     if conn.is_connected:
         data = {}
         email  = request.json['email']
         password = request.json['password']
         connector = conn.cursor(buffered = True)
         query = ("Select * from staff where staff_email ='{}' ").format(email)
         connector.execute(query)
         count = connector.rowcount
         if count > 0:
             count = 0
             for (staff )in connector:
                 data[count] = {}
                 data[count]['staff_id'] =staff[0]
                 data[count]['dept_no'] =staff[1]
                 data[count]['staff_name'] = staff[2]
                 data[count]['staff_password'] = staff[3]
                 data[count]['staff_email'] = staff[4]
                 data[count]['staff_role'] =staff[5]
                 data[count]['staff_avatar'] = staff[6]
                 count +=1
         return (data)
     connector.close()
     conn.close()
     return ({'status':False,'Message':'Login failed' })
@error(code=401)
def restricted(error):
    response.body = None
    response.content_type = "application/json"
    return json.dumps({'status':False,'message':'Unauthorized Access'})
app.route("/",method="GET")(index)
app.route("/userlogin",method="POST")(user_login)

##error pages
app.error(401,restricted)

#And away we go run the App
run(app,**appconfig.config['server'])

