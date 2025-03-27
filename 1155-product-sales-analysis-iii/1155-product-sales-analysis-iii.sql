# Write your MySQL query statement below

select p.product_id, s.year as first_year,s.quantity as quantity, s.price
from Product p join Sales s
on p.product_id = s.product_id
where (p.product_id,s.year)
in (select product_id,min(year) from Sales group by product_id )
order by p.product_id asc

-- with cte as(
--     select product_id,min(year) as min_year from Sales
--     group by product_id
-- )

-- select s.product_id, s.year as first_year,s.quantity as quantity, s.price
-- from sales s join
-- cte as c on c.product_id = s.product_id 
-- and c.min_year = s.year