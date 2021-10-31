import pymysql
from flask_login import UserMixin
from __init__ import login
from werkzeug.security import generate_password_hash, check_password_hash
from .student import Student
from .assignment import Assignment
from datetime import date, datetime

@login.user_loader
def load_user(user_id):
    conn = DBConnector()
    return conn.queryUserID(int(user_id))

class User(UserMixin):
    def __init__(self, id, username, password, centerID):
        self.id = id
        self.username = username
        self.password_hash = password
        self.centerID = centerID

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

    def connectAdmin(self):
        self.conn = pymysql.connect(
            host='tutorial-db.cmimggwftooj.us-east-2.rds.amazonaws.com',
            port=3306,
            user='172user1', 
            password = "user1pwd",
            db='172AdminDB',
            )
    
    def connectStudent(self):
        self.conn = pymysql.connect(
            host='tutorial-db.cmimggwftooj.us-east-2.rds.amazonaws.com',
            port=3306,
            user='172user1', 
            password = "user1pwd",
            db='172StudentDB',
            )
    
    def close(self):
        self.conn.close()

    def queryUser(self, username):
        self.connectAdmin()
        cur = self.conn.cursor()
        cur.execute("select * from Users where username='"+str(username)+"';")
        row = cur.fetchall()
        if(len(row) == 0):
            self.close()
            return None
        col = row[0]
        user = User(col[0],col[1],col[2],col[3])
        self.close()
        return user

    def queryUserID(self, id):
        self.connectAdmin()
        cur = self.conn.cursor()
        cur.execute("select * from Users where id="+str(id)+";")
        row = cur.fetchall()
        if(len(row) == 0):
            self.close()
            return None
        col = row[0]
        user = User(col[0],col[1],col[2],col[3])
        self.close()
        return user

    def registerUser(self, uName, pwd, centerID):
        user = User(None,uName, pwd, centerID)
        user.set_password()
        self.connectAdmin()
        cur = self.conn.cursor()
        cur.execute("select * from Users where centerID = "+str(centerID)+";")
        row = cur.fetchall()
        if(len(row) == 0):
            cur.execute("insert into TutorCenters (id) values ("+str(centerID)+");")
        cur.execute("insert into Users (username, password, centerID) values ('"+str(user.username)+"','"+str(user.password_hash)+"',"+str(user.centerID)+");")
        self.conn.commit()
        self.close()
        user = self.queryUser(uName)
        if(user is not None):
            return user
        else:
            return None

    def insertStudent(self, student):
        self.connectStudent()
        cur = self.conn.cursor()
        cur.execute("insert into Students (name, enrollmentDate, centerID) values ('"+student.name+"','"+student.enrollDate.strftime("%Y-%m-%d")+"',"+str(student.centerID)+");")
        self.conn.commit()
        self.close()

    def queryStudents(self):
        self.connectStudent()
        cur = self.conn.cursor()
        cur.execute("select * from Students;")
        rows = cur.fetchall()
        self.close()
        students = []
        for row in rows:
            student = Student(row[1],row[2],row[3])
            student.id = row[0]
            students.append(student)
        return students

    def queryAssignments(self, studentID):
        self.connectStudent()
        cur = self.conn.cursor()
        cur.execute("select * from Assignments where studentID="+str(studentID)+";")
        rows = cur.fetchall()
        
        assignments = []
        for row in rows:
            cur.execute("select title from Worksheets where id="+str(row[1])+";")
            rows2 = cur.fetchall()
            wkst = rows2[0]
            assignment = Assignment(wkst[0],None,None,row[3],row[4],row[5])
            assignment.id = row[0]
            assignments.append(assignment)
        self.close()
        return assignments

    def queryWorksheetTitles(self):
        self.connectStudent()
        cur = self.conn.cursor()
        cur.execute("select id, title from Worksheets;")
        rows = cur.fetchall()
        self.close()
        titles = []
        for row in rows:
            titles.append((row[0],row[1]))
        return titles