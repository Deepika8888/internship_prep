
USE school;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    grade INT
);

INSERT INTO students (name, age, grade) VALUES
('Alice', 20, 85),
('Bob', 22, 60),
('Charlie', 21, 78),
('Diana', 20, 92),
('Eve', 23, 45),
('Frank', 21, 88),
('Grace', 22, 55),
('Henry', 20, 95);

select * from students;

#Question1
select name, grade from students
where grade > 80;

#Question2
select count(name) as Students_above_80 from students 
where grade > 80;

#Question2
select avg(grade) as average_grade from students;

#Question3
select name, grade from students
order by grade desc;

#Question5
select grade, count(*) as total_students
from students
group by grade;

CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_name VARCHAR(50)
);

INSERT INTO courses (student_id, course_name) VALUES
(1, 'Python'),
(2, 'SQL'),
(3, 'Data Analysis'),
(4, 'Python'),
(5, 'Web Dev');

#Question6
select s.name, c.course_name from students s
inner join courses c on s.id = c.student_id;


