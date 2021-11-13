import pymysql
from flask_login import UserMixin
from __init__ import login
from werkzeug.security import generate_password_hash, check_password_hash

from .employee import Employee
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
        cur.execute("select * from TutorCenters where id = "+str(centerID)+";")
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

    def queryAssignment(self, assignmentID):
        self.connectStudent()
        cur = self.conn.cursor()
        cur.execute("select * from Assignments where id="+str(assignmentID)+";")
        rows = cur.fetchall()
        row = rows[0]
        cur.execute("select title from Worksheets where id="+str(row[1])+";")
        rows2 = cur.fetchall()
        wkst = rows2[0]
        self.close()
        
        assignment = Assignment(wkst[0],None,None,row[3],row[4],row[5])
        assignment.id = row[0]
        return assignment

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

    def insertAssignment(self, assignment, studentID):
        self.connectStudent()
        cur = self.conn.cursor()
        delivered = "null"
        due = "null"
        if assignment.due != None:
            due = assignment.due.strftime("%Y-%m-%d")
        if assignment.delivered != None:
            delivered = assignment.delivered.strftime("%Y-%m-%d")
        if assignment.score == None:
            assignment.score = "null"
        cur.execute("insert into Assignments (worksheetID, studentID, dueDate, deliveredDate, grade) values ("+str(assignment.id)+","+str(studentID)+",'"+str(due)+"','"+str(delivered)+"',"+str(assignment.score)+");")
        self.conn.commit()
        self.close()

    def updateAssignment(self, assignment, studentID, assignmentID):
        self.connectStudent()
        cur = self.conn.cursor()
        delivered = "null"
        due = "null"
        if assignment.due != None:
            due = assignment.due.strftime("%Y-%m-%d")
        if assignment.delivered != None:
            delivered = assignment.delivered.strftime("%Y-%m-%d")
        if assignment.score == None:
            assignment.score = "null"
        cur.execute("update Assignments set worksheetID="+str(assignment.id)+", studentID="+str(studentID)+",dueDate='"+str(due)+"',deliveredDate='"+str(delivered)+"',grade="+str(assignment.score)+" where id="+str(assignmentID)+";")
        self.conn.commit()
        self.close()

    def insertEmployee(self, employee):
        self.connectAdmin()
        cur = self.conn.cursor()
        cur.execute("insert into Employees (name, jobTitle) values ('" + employee.name + "','" + employee.jobTitle + "');")
        self.conn.commit()
        self.close()

    def deleteEmployee(self, id):
        self.connectAdmin()
        cur = self.conn.cursor()
        cur.execute("delete from Employees where 'id' = " + id + "');")
        self.conn.commit()
        self.close()

    def queryEmployees(self):
        self.connectAdmin()
        cur = self.conn.cursor()
        cur.execute("select * from Employees;")
        rows = cur.fetchall()
        self.close()
        employees = []
        for row in rows:
            employee = Employee(row[1], row[2])
            employees.append(employee)
        return employees
