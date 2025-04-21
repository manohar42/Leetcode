-- select student_id,subject, score, min(exam_date)
-- from Scores
-- group by student_id,subject

with cte as (select student_id, subject, 
First_value(score) over(partition by student_id,subject order by exam_date asc) as first_score,
First_value(score) over(partition by student_id,subject order by exam_date desc) as latest_score
from Scores
)

select distinct * from cte where latest_score > first_score
order by student_id asc, subject asc