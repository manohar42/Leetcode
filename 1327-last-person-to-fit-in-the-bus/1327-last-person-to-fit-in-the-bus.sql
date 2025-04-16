# Write your MySQL query statement below

with cte as (select person_name,
sum(weight) over(ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW) as weight_sum
from Queue
order by turn)

select person_name from cte where weight_sum <= 1000
order by weight_sum desc
limit 1

