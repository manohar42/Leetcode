# Write your MySQL query statement below
select if(id%2 = 0, id-1,id+1) as id,student from Seat
where id not in (select if(mod(id,2) != 0,id,-1) from Seat where id in (select max(id) from Seat))
union
select id,student from Seat where id in
(select if(mod(id,2) != 0,id,-1) from Seat where id in (select max(id) from Seat))
order by id asc
