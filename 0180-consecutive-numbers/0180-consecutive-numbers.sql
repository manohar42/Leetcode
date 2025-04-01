-- # Write your MySQL query statement below

-- select l1.num as ConsecutiveNums
-- from Logs l1 join
-- (select l.id, l.num from 
-- Logs l join
-- Logs l2
-- on (l.num = l2.num and l.id = l2.id+1)) l3

-- on(l1.num = l3.num and l1.id = l3.id-1)

select distinct l3.num as ConsecutiveNums
from Logs l
join
Logs l2
on (l.id = l2.id-1)
join Logs l3
on(l.id = l3.id+1)
where (l.num = l3.num and l.num = l2.num )
