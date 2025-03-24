
select e1.name from Employee e1
join 
(select managerId, count(*)
from Employee 
group by managerId
having count(*)>=5) as e2
on e1.id = e2.managerId