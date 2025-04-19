# Write your MySQL query statement below
with cte as
(select u.name as results from Users u inner join
MovieRating mr
on u.user_id = mr.user_id
group by u.user_id
order by count(*) desc, u.name asc
limit 1)
,cte2 as (select m.title from 
Movies m inner join MovieRating mv 
on m.movie_id = mv.movie_id
where month(created_at) = 2 and year(created_at) = 2020
group by m.title
order by avg(mv.rating) desc,m.title asc
limit 1)

select * from cte
union all
select * from cte2