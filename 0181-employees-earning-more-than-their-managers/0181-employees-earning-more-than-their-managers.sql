# Write your MySQL query statement below

select e.name as Employee from Employee e join 
Employee e1 on e.managerId = e1.id and e.salary > e1.salary 