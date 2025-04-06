# Write your MySQL query statement below

select distinct p.email as Email from Person p join
Person p1 on p.id != p1.id and p.email = p1.email