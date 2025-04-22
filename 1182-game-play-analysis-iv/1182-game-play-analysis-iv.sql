# Write your MySQL query statement below
select
round((select count(*) from Activity
where (player_id,DATE_ADD(event_date, Interval -1 day)) in(select player_id, min(event_date) from Activity group by player_id)) /
(select count(distinct player_id) from Activity),2) as fraction