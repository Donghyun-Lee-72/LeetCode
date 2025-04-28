# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary
FROM 
((SELECT salary
 FROM Employee
 GROUP BY salary
 ORDER BY salary DESC
 LIMIT 1,1)
UNION
(SELECT NULL
 FROM DUAL)) AS temp