# Write your MySQL query statement below

select SUBSTR(trans_date,1,7) as month,country, Count(id) as trans_count,
Sum(Case when state = 'approved' then 1 else 0 END) as approved_count, 
sum(amount) as trans_total_amount,  
sum(case when state = 'approved' then amount else 0 End) as approved_total_amount 
from Transactions
group by month, country