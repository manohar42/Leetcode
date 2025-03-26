# Write your MySQL query statement below

with tab as (select *, Row_Number() over(partition by customer_id order by order_date) as rn
from Delivery
order by customer_id asc,order_date asc)

select round(((select count(*) from tab where order_date = customer_pref_delivery_date and rn = 1 )*100/(
    select count(distinct customer_id) from Delivery)),2) as immediate_percentage
