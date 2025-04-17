# Write your MySQL query statement below

with cte as(select count(requester_id) as countofid, requester_id from RequestAccepted
group by requester_id
union all
select count(accepter_id),accepter_id from RequestAccepted
group by accepter_id)
,cte2 as(
select requester_id as id, sum(countofid) as final_count from cte 
group by requester_id
order by final_count desc )

select id, final_count as num from cte2 
where final_count = (select max(final_count) from cte2)


