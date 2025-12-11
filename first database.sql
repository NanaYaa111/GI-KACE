CREATE TABLE teacher(
teacher_id int,
teacher_qualification varchar,
teacher_name char(50),
course_id varchar(5)
);

SELECT teacher_id,teacher_qualification,teacher_name,course_id
FROM teacher;

CREATE TABLE course(
course_name varchar(100),
course_id varchar(5),
course_duration_hr int
);

SELECT course_name,course_duration_hr,course_id
FROM course;

SELECT * FROM teacher;

INSERT INTO course(course_name,course_id,course_duration_hr)
VALUES ('javascript',160, 'JS');

INSERT INTO teacher(teacher_id,teacher_qualification,teacher_name,course_id)
VALUES(223434,'PHD','Ama','SB'),
(220459,'PHD','kojo','JS'),
(2204572, 'PHD','Ama','SE');

CREATE TABLE  teacher_updated(
teacher_id int PRIMARY KEY,
teacher_qualification varchar,
teacher_name char(50),
course_id varchar(5)
);

SELECT * FROM teacher_updated;

INSERT INTO teacher_updated
(teacher_id, teacher_qualification,
teacher_name,course_id)VALUES
(2002, 'MSC Data Science', 'Michelle','1234'),
(2003, 'MSC Javascript', 'Wilson','2357'),=
(2004, 'MSC Software Engineering', 'PK','4523'),
(2005,' MSC Database', 'Wilson','5678');

SELECT * FROM teacher_updated;

UPDATE teacher_updated
SET teacher_name= 'Wilson'
WHERE teacher_id=2002;

SELECT * FROM teacher_updated 
WHERE teacher_qualification= 'MSC Data Science'

























