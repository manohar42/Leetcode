# Write your MySQL query statement below
with cte as(
select product_id,max(change_date) as max_date from Products 
where change_date <= '2019-08-16'
group by product_id)

select p.product_id,p.new_price as price from Products as p
inner join cte as c on c.product_id = p.product_id and p.change_date = c.max_date
union
select product_id, 10 from Products where product_id not in (select product_id from cte)