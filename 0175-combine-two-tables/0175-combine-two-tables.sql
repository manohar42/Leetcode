# Write your MySQL query statement below


select p.firstname, p.lastname, a.city, a.state 
from Person as p Left outer join Address as a  
on p.personId = a.personId