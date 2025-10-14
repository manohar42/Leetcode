# Write your MySQL query statement below

with cte as (
    select customer_id, min(order_date) as min_date from Delivery
    group by customer_id 
    order by customer_id
)

select round(avg(
    case 
    when datediff(c.min_date,d.customer_pref_delivery_date) = 0 then 1
    else 0
    end
)*100,2) as immediate_percentage from Delivery d join cte c
on d.customer_id = c.customer_id and d.order_date = c.min_date