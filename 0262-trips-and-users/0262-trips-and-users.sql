select t.request_at as "Day",round(
sum(case status when "completed" then 0
else 1
end)/count(u.banned),2) as "Cancellation Rate"
from Trips t join Users u on t.client_id = u.users_id and u.banned = "No"
where t.request_at between "2013-10-01" and "2013-10-03" and (t.driver_id) in (select users_id from Users where banned = "No" )
group by request_at