import json
import sys
import mysql.connector
sys.path.append("../config")
import appconfig

class ci_api_model:
    def __init__(self, config=None):
        self.config  = config
    def log(*args):
        if (appconfig.config['log']):
            print(*args)    
    def wrapper(self,*args):  
        con = mysql.connector.connect(**self.config)
        if(con.is_connected()):
            self.log("Connection succesful")
            return con
        self.log("Unable to connect")
   
model = ci_api_model
