/*  
	Attendance{studentID, aDate, attendanceValue}
**attendance value will be either L or A (late or absent)
	Worksheets{id, title, difficultyRating, subjectID} 
**difficulty ratings will go from A1 to J9
	Assignments{worksheetID, studentID, dueDate, deliveredDate, grade} 
**grade and deliveredDate will be null if not completed yet
	Students{id, centerID, name, enrollmentDate}
	Parents{studentID, parentName, phoneNum, emailAddr}
**parents can be in DB multiple times if multiple children are enrolled
*/

drop table if exists Attendance;
drop table if exists Worksheets;
drop table if exists Assignments;
drop table if exists Students;
drop table if exists Parents;

create table Students(
	id int auto_increment primary key,
    centerID int, 
    name varchar(30), 
    enrollmentDate date
);

create table Parents(
	studentID int references Students(id) on delete cascade, 
    parentName varchar(30), 
    phoneNum int check (phoneNum >= 1000000000 and phoneNum <= 9999999999), 
    emailAddr varchar(30),
    primary key(studentID, parentName)
    
);

create table Worksheets(
	id int auto_increment primary key,
    title varchar(30), 
    difficultyRating varchar(5), 
    subjectID int
);

create table Assignments(
	worksheetID int references Worksheets(id), 
    studentID int references Students(id) on delete cascade, 
    dueDate date, 
    deliveredDate date, 
    grade int check (grade >= 0 and grade <= 100),
    primary key(worksheetID, studentID, dueDate)
);

/*only late/absent dates should be recorded to save space*/
create table Attendance(
	studentID int references Students(id) on delete cascade,
    attDate date,
    attVal varchar(30) check (attVal in ("L","A")),
    primary key(studentID, attDate)
);












    