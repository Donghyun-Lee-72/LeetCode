# Write your MySQL query statement below
SELECT name as Employee
FROM Employee a
WHERE salary > (SELECT salary
                FROM Employee b
                WHERE a.managerId = b.id)