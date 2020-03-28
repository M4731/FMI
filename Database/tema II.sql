--LAB 4

--ex 8

select employee_id, first_name, last_name 
from employees  
where salary > (select avg(salary)                               
                from employees) 
order by salary desc;

--ex 9

select distinct e.manager_id, e.salary                             
from employees e
where e.salary = ( select min(salary)
                 from employees 
                 where e.manager_id = manager_id
                 having min(salary) > 1000 )
order by e.salary desc;

--ex 10

select distinct j.job_id, j.job_title, e.salary                         
from employees e, jobs j
where e.salary = ( select max(salary)
                   from employees 
                   where j.job_id = job_id
                   having max(salary) > 3000 );

--ex 11

select min ( avg ( salary ) )
from employees
group by job_id;

--ex 12

select max ( avg ( salary ) ) 
from employees
group by job_id;

--ex 13

select job_id, job_title, avg (salary) 
from jobs join employees using (job_id)
group by job_id, job_title
having avg(salary) = ( select min (avg(salary))
                        from employees d
                        group by d.job_id );

--ex 14

select avg (salary)
from employees
having avg(salary) > 2500;

--LAB 3

--ex 18
select  concat (first_name, last_name), department_id, job_id
from employees join departments using (department_id) join locations using (location_id)
where city = 'Toronto';

