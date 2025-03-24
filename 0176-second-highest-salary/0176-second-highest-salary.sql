# Write your MySQL query statement below

-- select max(salary) as SecondHighestSalary from Employee 
-- where salary != (select max(salary) from employee)

-- Select (select distinct salary from Employee order by salary desc limit 1 offset 1) as SecondHighestSalary 

Select Ifnull((select distinct salary from Employee order by salary desc limit 1 offset 1),null) as SecondHighestSalary 