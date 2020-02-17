CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare M int;
  set M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      
      select
      ifnull((select distinct Salary
             from Employee
             order by Salary desc
             limit 1 offset M), null)
      
  );
END
