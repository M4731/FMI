-- 23

select last_name, e.job_id, job_title, department_name, salary
from employees e, jobs j, departments d
where e.job_id = j.job_id and e.department_id = d.department_id;

-- 25

select ang.last_name Angajat, ang.hire_date Data_ang, sef.last_name Manager, sef.hire_date Data_mgr
from employees ang, employees sef
where ang.hire_date < sef.hire_date and ang.manager_id = sef.employee_id;