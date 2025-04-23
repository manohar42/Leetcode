# Write your MySQL query statement below

with cte as (
    select stock_name, sum(price) as buy_price from Stocks where operation = "Buy"
    group by stock_name
), cte2 as (
    select stock_name,sum(price) as sell_price from Stocks where operation = "Sell"
    group by stock_name
)

select s.stock_name, o.sell_price-s.buy_price as capital_gain_loss
from cte s join cte2 o 
on s.stock_name = o.stock_name