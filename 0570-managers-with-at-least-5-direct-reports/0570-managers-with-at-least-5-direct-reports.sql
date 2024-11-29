# Write your MySQL query statement below

select E1.name from Employee E1 Join
(select managerId, count(*) from Employee 
Group By managerId 
having count(*)>=5) 
E2 on E1.id = E2.managerId;