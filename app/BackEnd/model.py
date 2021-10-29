import pymysql
from flask_login import UserMixin
from __init__ import login
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    conn = DBConnector()
    return conn.queryUserID(int(id))

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password_hash = password


    def __repr__(self):
        return '<User {}>'.format(self.username)
       
    def set_password(self):
        #self.password_hash = generate_password_hash(self.password_hash, method='pbkdf2:sha1')
        self.password_hash = self.hash(self.password_hash)
 
    def check_password(self, password):
        #return check_password_hash(self.password_hash, password)
        return self.password_hash == self.hash(password)

    def hash(self, password):
        hashWord = 0
        for char in list(password):
            hashWord += ord(char)
        print(password + ": "+str(hashWord))
        return str(hashWord)

class DBConnector:

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host='tutorial-db.cmimggwftooj.us-east-2.rds.amazonaws.com',
            port=3306,
            user='172user1', 
            password = "user1pwd",
            db='172AdminDB',
            )
    
    def close(self):
        self.conn.close()

    def queryUser(self, username):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("select * from Users where username='"+username+"'")
        row = cur.fetchall()
        if(len(row) == 0):
            self.close()
            return None
        col = row[0]
        user = User(col[0],col[1],col[2])
        self.close()
        return user

    def queryUserID(self, id):
        self.connect()
        cur = self.conn.cursor()
        cur.execute("select * from Users where id="+str(id))
        row = cur.fetchall()
        if(len(row) == 0):
            self.close()
            return None
        col = row[0]
        user = User(col[0],col[1],col[2])
        self.close()
        return user

    def registerUser(self, uName, pwd):
        user = User(None,uName, pwd)
        user.set_password()
        self.connect()
        cur = self.conn.cursor()
        cur.execute("insert into Users (username, password) values ('"+str(user.username)+"','"+str(user.password_hash)+"')")
        self.conn.commit()
        self.close()
        user = self.queryUser(uName)
        if(user is not None):
            return user
        else:
            return None
        
