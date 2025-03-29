# Write your MySQL query statement below

select e.employee_id, e.name, t.reports_count,t.average_age
from Employees e join
(select reports_to, count(reports_to) as reports_count, round(avg(age)) as average_age from Employees
where reports_to is not null
group by reports_to) t
on e.employee_id = t.reports_to
order by e.employee_id asc
