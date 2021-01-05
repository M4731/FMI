--1

CREATE SEQUENCE "GRUPA243"."SEC_MMD"  MINVALUE 1 MAXVALUE 999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE;

CREATE OR REPLACE PACKAGE pachetbengos_MMD
AS
                           
    FUNCTION f_salariu_mic(dep emp_MMD.department_id%TYPE,
                           jep emp_MMD.job_id%TYPE)
    RETURN emp_MMD.salary%TYPE;
    
    FUNCTION f_sefu(n1 emp_MMD.last_name%TYPE,
                    n2 emp_MMD.first_name%TYPE)
    RETURN emp_MMD.employee_id%TYPE;
    
    FUNCTION f_dep(n1 dep_MMD.department_name%TYPE)
    RETURN emp_MMD.department_id%TYPE;   
    
    FUNCTION f_job(n1 jobs_MMD.job_title%TYPE)
    RETURN jobs_MMD.job_id%TYPE; 

    PROCEDURE adaugare(nume emp_MMD.first_name%TYPE,
                       prenume emp_MMD.last_name%TYPE,
                       email emp_MMD.email%TYPE,
                       nr_telefon emp_MMD.phone_number%TYPE,
                       nume_sefu emp_MMD.last_name%TYPE,
                       prenume_sefu emp_MMD.first_name%TYPE,
                       numdep dep_MMD.department_name%TYPE,
                       numejob jobs_MMD.job_title%TYPE); 
                       
    FUNCTION f_salar(v_ang emp_MMD.employee_id%TYPE,
                     v_dep emp_MMD.department_id%TYPE,
                     v_job emp_MMD.job_id%TYPE)
    RETURN emp_MMD.salary%TYPE;
    
    FUNCTION f_comis(v_dep emp_MMD.department_id%TYPE,
                     v_job emp_MMD.job_id%TYPE)
    RETURN emp_MMD.commission_pct%TYPE;
    
    FUNCTION f_end(v_id emp_MMD.employee_id%TYPE)
    RETURN emp_MMD.hire_date%TYPE;
                       
    PROCEDURE mutare(nume emp_MMD.first_name%TYPE,
                     prenume emp_MMD.last_name%TYPE,
                     nume_sefu emp_MMD.last_name%TYPE,
                     prenume_sefu emp_MMD.first_name%TYPE,
                     numdep dep_MMD.department_name%TYPE,
                     numejob jobs_MMD.job_title%TYPE); 
             
    FUNCTION f_subalterni(nume emp_MMD.first_name%TYPE,
                          prenume emp_MMD.last_name%TYPE)    
    RETURN NUMBER;
    
    PROCEDURE p_promovare(v_id emp_MMD.employee_id%TYPE);
              
    PROCEDURE p_salmare(nume emp_MMD.first_name%TYPE,
                        prenume emp_MMD.last_name%TYPE,
                        salariu emp_MMD.salary%TYPE);
        
    CURSOR lista_job(c_id jobs_MMD.job_id%TYPE)
    IS
        SELECT * 
        FROM emp_MMD
        WHERE job_id = c_id;
        
    CURSOR lista_joburi
    IS
        SELECT *
        FROM jobs_MMD;
        
    PROCEDURE p_h;
        
END pachetbengos_MMD;
/

CREATE OR REPLACE PACKAGE BODY pachetbengos_MMD
AS
    FUNCTION f_salariu_mic(dep emp_MMD.department_id%TYPE,
                           jep emp_MMD.job_id%TYPE)
    RETURN emp_MMD.salary%TYPE 
    AS
        v_nr emp_MMD.salary%TYPE;     
    BEGIN
        SELECT min(salary) INTO v_nr
        FROM emp_MMD
        WHERE  department_id = dep AND job_id = jep;
        
        RETURN v_nr;
    END f_salariu_mic;
    
    
    FUNCTION f_sefu(n1 emp_MMD.last_name%TYPE,
                    n2 emp_MMD.first_name%TYPE)
    RETURN emp_MMD.employee_id%TYPE
    AS
        v_nr emp_MMD.employee_id%TYPE;  
    BEGIN
        SELECT employee_id INTO v_nr
        FROM emp_MMD
        WHERE last_name = INITCAP(n1) AND first_name = INITCAP(n2);
        
        RETURN v_nr;
    EXCEPTION
     WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Exista mai multi angajati cu numele dat');
    
    END f_sefu;
    
    FUNCTION f_dep(n1 dep_MMD.department_name%TYPE)
    RETURN emp_MMD.department_id%TYPE
    AS
        v_nr emp_MMD.department_id%TYPE;  
    BEGIN
        SELECT department_id INTO v_nr
        FROM dep_MMD
        WHERE department_name = n1;
        
        RETURN v_nr;
    END f_dep;     
    
    FUNCTION f_job(n1 jobs_MMD.job_title%TYPE)
    RETURN jobs_MMD.job_id%TYPE
    AS
        v_nr jobs_MMD.job_id%TYPE;  
    BEGIN
        SELECT job_id INTO v_nr
        FROM jobs_MMD
        WHERE job_title = n1;
        
        RETURN v_nr;
    END f_job;  
    

    PROCEDURE adaugare(nume emp_MMD.first_name%TYPE,
                       prenume emp_MMD.last_name%TYPE,
                       email emp_MMD.email%TYPE,
                       nr_telefon emp_MMD.phone_number%TYPE,
                       nume_sefu emp_MMD.last_name%TYPE,
                       prenume_sefu emp_MMD.first_name%TYPE,
                       numdep dep_MMD.department_name%TYPE,
                       numejob jobs_MMD.job_title%TYPE) IS
    BEGIN
    
        INSERT INTO emp_MMD
        VALUES (SEC_MMD.nextval, nume, prenume, email, nr_telefon, sysdate, f_job(numejob), f_salariu_mic(f_dep(numdep), f_job(numejob)), null, f_sefu(nume_sefu, prenume_sefu), f_dep(numdep));
    END adaugare;
    
    FUNCTION f_salar(v_ang emp_MMD.employee_id%TYPE,
                     v_dep emp_MMD.department_id%TYPE,
                     v_job emp_MMD.job_id%TYPE)
    RETURN emp_MMD.salary%TYPE
    IS
        v_nr emp_MMD.salary%TYPE;
        v_nw emp_MMD.salary%TYPE;
    BEGIN
        DBMS_OUTPUT.PUT_LINE('salarin');

        SELECT salary INTO v_nr
        FROM emp_MMD
        WHERE employee_id = v_ang;
        
        SELECT min(salary) INTO v_nw
        FROM emp_MMD
        WHERE department_id = v_dep AND job_id = v_job;
        
        DBMS_OUTPUT.PUT_LINE('salarout');
        IF v_nr < v_nw
        THEN 
            RETURN v_nw;
        ELSE 
            RETURN v_nr;
        END IF;
    END f_salar;
    
    FUNCTION f_comis(v_dep emp_MMD.department_id%TYPE,
                     v_job emp_MMD.job_id%TYPE)
    RETURN emp_MMD.commission_pct%TYPE
    IS
        v_nr emp_MMD.commission_pct%TYPE;
        vvvv BOOLEAN := false;
    BEGIN
        
        FOR i IN (SELECT *
                  FROM emp_MMD
                  WHERE department_id = v_dep AND job_id = v_job)
        LOOP
            IF i.commission_pct is null
            THEN 
                vvvv := true;
            END IF;
        END LOOP;
        
        SELECT min(commission_pct) INTO v_nr
        FROM emp_MMD
        WHERE department_id = v_dep AND job_id = v_job;
        
        IF vvvv = true
        THEN
            RETURN null;
        ELSE
            RETURN v_nr;
        END IF;
    END f_comis;
    
    FUNCTION f_end(v_id emp_MMD.employee_id%TYPE)
    RETURN emp_MMD.hire_date%TYPE
    IS
        v_data1 emp_MMD.hire_date%TYPE;
        v_data2 BOOLEAN := false;
        v_data3 emp_MMD.hire_date%TYPE;
    BEGIN
        SELECT hire_date INTO v_data1
        FROM emp_MMD 
        WHERE employee_id = v_id;
        
        FOR i IN (SELECT employee_id
                  FROM jh_MMD)
        LOOP
            IF i.employee_id = v_id
            THEN 
                v_data2 := true;
                SELECT max(end_date) INTO v_data3
                FROM jh_MMD 
                WHERE i.employee_id = v_id;
            END IF;
        END LOOP;
        
        IF v_data2 = true
        THEN    
            RETURN v_data3;
        ELSE 
            RETURN v_data1;
        END IF;
        
    END f_end;
    
    PROCEDURE mutare(nume emp_MMD.first_name%TYPE,
                     prenume emp_MMD.last_name%TYPE,
                     nume_sefu emp_MMD.last_name%TYPE,
                     prenume_sefu emp_MMD.first_name%TYPE,
                     numdep dep_MMD.department_name%TYPE,
                     numejob jobs_MMD.job_title%TYPE) IS
    v_id emp_MMD.employee_id%TYPE:= f_sefu(prenume, nume);
    v_idsefu emp_MMD.employee_id%TYPE := f_sefu(prenume_sefu, nume_sefu);
    v_iddep dep_MMD.department_id%TYPE := f_dep(numdep);
    v_idjob jobs_MMD.job_id%TYPE := f_job(numejob);
    v_nr emp_MMD.salary%TYPE := f_salar(v_id, v_iddep, v_idjob);
    v_comis emp_MMD.commission_pct%TYPE := f_comis(v_iddep, v_idjob);
    v_data emp_MMD.hire_date%TYPE := f_end(v_id);
    v_job emp_MMD.job_id%TYPE;
    v_dep emp_MMD.department_id%TYPE;
    BEGIN
        SELECT job_id, department_id INTO v_job, v_dep
        FROM emp_MMD
        WHERE employee_id = v_id;
    
        INSERT INTO jh_MMD
        VALUES(v_id, v_data, sysdate, v_job, v_dep);
    
        UPDATE emp_MMD
        SET department_id = v_iddep, 
            job_id = v_idjob,
            manager_id = v_idsefu,
            salary = v_nr,
            commission_pct = v_comis
        WHERE employee_id = v_id;
        
    END mutare;
                     
    FUNCTION f_subalterni(nume emp_MMD.first_name%TYPE,
                          prenume emp_MMD.last_name%TYPE)    
    RETURN NUMBER
    IS
        v_cont NUMBER := 0;
        v_man emp_MMD.employee_id%TYPE := f_sefu(prenume, nume);
    BEGIN
        SELECT count(*) INTO v_cont
        FROM emp_MMD e
        WHERE v_man IN (SELECT manager_id
                        FROM  emp_MMD 
                        START WITH employee_id = e.employee_id
                        CONNECT BY PRIOR manager_id = employee_id);
                    
        RETURN v_cont;
    EXCEPTION
    
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu exista manager cu numele dat');
        return 0;
    
    END;
    
    PROCEDURE p_promovare(v_id emp_MMD.employee_id%TYPE)
    IS
        v_nr emp_MMD.employee_id%TYPE;
        v_nw emp_MMD.employee_id%TYPE;
    BEGIN
        SELECT manager_id INTO v_nr
        FROM emp_MMD
        WHERE employee_id = v_id;
        
        IF v_nr is not null
        THEN 
            SELECT manager_id INTO v_nw
            FROM emp_MMD
            WHERE employee_id = v_nr;
                    
            IF v_nw is not null
            THEN 
                UPDATE emp_mmd
                SET manager_id = v_nw
                WHERE employee_id = v_id;
            ELSE
                UPDATE emp_mmd
                SET manager_id = null
                WHERE employee_id = v_id;
            END IF;
        END IF;
    EXCEPTION
    
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu exista manager cu numele dat');
    END;
    
    PROCEDURE p_salmare(nume emp_MMD.first_name%TYPE,
                        prenume emp_MMD.last_name%TYPE,
                        salariu emp_MMD.salary%TYPE)
    IS
        v_nr emp_MMD.employee_id%TYPE := f_sefu(prenume, nume);
        v_min emp_MMD.salary%TYPE;
        v_max emp_MMD.salary%TYPE;
    BEGIN
        
        SELECT min_salary INTO v_min
        FROM jobs
        WHERE job_id = (SELECT job_id
                        FROM emp_MMD
                        WHERE employee_id = v_nr);
                    
        SELECT max_salary INTO v_max
        FROM jobs
        WHERE job_id = (SELECT job_id
                        FROM emp_MMD
                        WHERE employee_id = v_nr);    
                    
        IF salariu between v_min and v_max
        THEN 
            UPDATE emp_mmd
            SET salary = salariu
            WHERE employee_id = v_nr;  
        ELSE
            DBMS_OUTPUT.PUT_LINE('Salariul nu respecta limitele pentru jobul ales');
        END IF;
    
    EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Nu exista manager cu numele dat');

    END;
    
    PROCEDURE p_h
    IS
    BEGIN
        FOR i IN lista_joburi
        LOOP
            DBMS_OUTPUT.PUT_LINE(i.job_title);
            FOR j IN lista_job(i.job_id)
            LOOP
                DBMS_OUTPUT.PUT(j.employee_id || ' ' || j.first_name  || ' ' || j.last_name);
                FOR k IN (SELECT *
                          FROM jh_MMD
                          WHERE employee_id = j.employee_id)
                LOOP
                    IF k.job_id = j.job_id
                    THEN
                        DBMS_OUTPUT.PUT(' da');
                    END IF;
                END LOOP;
                DBMS_OUTPUT.NEW_LINE;
            END LOOP;
        DBMS_OUTPUT.PUT_LINE(' -----------------');
        END LOOP;
    END;
    
END pachetbengos_MMD;
/

EXECUTE pachetbengos_MMD.adaugare('Matei','Sefu','matyboss','0735235235','Kochhar','Neena','IT Support','Programmer');
EXECUTE pachetbengos_MMD.adaugare('Dani','Preafericitu','DANIELTANC','0735236969','Matei','Sefu','IT Support','Programmer');

EXECUTE pachetbengos_MMD.mutare('Eleni','Zlotkey','Matei','Sefu','IT Support','Programmer');
EXECUTE pachetbengos_MMD.mutare('Irene','Mikkilineni','Matei','Sefu','IT Support','Programmer');
EXECUTE pachetbengos_MMD.mutare('Jean','Fleaur','Matei','Sefu','IT Support','Programmer');
EXECUTE pachetbengos_MMD.mutare('Sarah','Bell','Matei','Sefu','IT Support','Programmer');

EXECUTE pachetbengos_MMD.p_h();
EXECUTE pachetbengos_MMD.p_salmare('Den','Raphaely',11500);
EXECUTE pachetbengos_MMD.p_promovare(2);

DECLARE 
    x NUMBER;
    xx NUMBER;
BEGIN
    x := pachetbengos_MMD.f_subalterni('Matei','Sefu');
    xx := pachetbengos_MMD.f_subalterni('Steven','King');
    DBMS_OUTPUT.PUT_LINE(xx);
    DBMS_OUTPUT.PUT_LINE(x);
END;
/











