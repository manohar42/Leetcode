# Write your MySQL query statement below
with cte as (
select player_id, min(event_date) as first_login from Activity
group by player_id)
select round(count(a.player_id)/ (select count(distinct player_id) from Activity),2) as fraction
from Activity a inner join cte c
on a.player_id = c.player_id and datediff(a.event_date, first_login) = 1
-- group by a.player_id

-- select distinct count(player_id) form Activity