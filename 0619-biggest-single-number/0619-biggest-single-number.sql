# Write your MySQL query statement below

select  if(Count(num)=1,num,null) as 'num' from MyNumbers 
group by num
order by num desc limit 1