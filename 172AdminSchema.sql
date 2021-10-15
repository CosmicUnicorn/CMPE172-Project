/*
	Subjects{id, title} 
**to maintain student records, no need to delete worksheets that are from legacy subjects, therefore, subjects doesn’t need to be referenced by worksheets table and can be in admin db
	Employees{id, name, jobTitle, centerID}
	TutorCenters{id, city, state, zip, addr}
*/

drop table if exists Subjects;
drop table if exists Employees;
drop table if exists TutorCenters;

create table Subjects(
	id int auto_increment primary key,
    title varchar(30)
);

create table Employees(
	id int auto_increment primary key,
    name varchar(30),
    jobTitle varchar(20),
    centerID int references TutorCenters(id)
);

create table TutorCenters(
	id int auto_increment primary key,
    city varchar(5),
    state varchar(30),
    zip int,
    addr varchar(30)
);




