# Write your MySQL query statement below
SELECT question_id AS survey_log
FROM (
    SELECT question_id,
            SUM(CASE WHEN action="show" THEN 1 ELSE 0 END) AS n_show,
           SUM(CASE WHEN action="answer" THEN 1 ELSE 0 END) AS n_ans
    FROM survey_log
    GROUP BY question_id
) as tb
ORDER BY (n_ans/n_show) DESC
limit 1 


