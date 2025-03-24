# Write your MySQL query statement below

select w.id from Weather w join Weather w2 on
Datediff(w.recordDate,w2.recordDate) = 1 
where w.recordDate > w2.recordDate and w.temperature > w2.temperature 