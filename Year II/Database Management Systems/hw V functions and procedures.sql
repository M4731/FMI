select * 
from employees;

--1

CREATE TABLE info_MMD
(
    utilizator VARCHAR2(50),
    data       DATE,
    comanda    VARCHAR2(50),
    nr_linii   INTEGER,
    eroare     VARCHAR2(50)
);

--2

CREATE OR REPLACE FUNCTION f2_MMD
    (v_nume employees.last_name%TYPE)
RETURN NUMBER IS
    salariu employees.salary%TYPE;
BEGIN
    INSERT INTO info_MMD VALUES(user, sysdate, 'f2_MMD', 1, null);
    
    SELECT salary INTO salariu
    FROM employees
    WHERE last_name = v_nume;
    
    RETURN salariu;
    
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Nu exista angajati cu numele dat'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f2_MMD';
        DBMS_OUTPUT.PUT_LINE('Nu exista angajati cu numele dat');
        return 0;
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('1');
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Exista mai multi angajati cu numele dat'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f2_MMD';
        DBMS_OUTPUT.PUT_LINE('Exista mai multi angajati cu numele dat');
        return 0;
    WHEN OTHERS THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Eroare random'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f2_MMD';
        DBMS_OUTPUT.PUT_LINE('Eroare random');
        return 0;
END f2_MMD;
/

DECLARE 
    v_test NUMBER;
BEGIN 
    v_test := f2_MMD('Grasssssnt');
END;
/

DECLARE 
    v_test NUMBER;
BEGIN 
    v_test := f2_MMD('Grant');
END;
/

DECLARE 
    v_test NUMBER;
BEGIN 
    v_test := f2_MMD('Abel');
END;
/

--3

CREATE OR REPLACE FUNCTION help_MMD
    (yd employees.employee_id%TYPE)
RETURN NUMBER IS
    numar NUMBER;
BEGIN
    SELECT COUNT(employee_id) INTO numar
    FROM job_history
    WHERE employee_id = yd;
    
    RETURN numar;
END;
/

CREATE OR REPLACE FUNCTION f3_MMD
    (v_oras locations.city%TYPE)
RETURN NUMBER IS
    numar NUMBER;
    no_city_found EXCEPTION;
BEGIN
    INSERT INTO info_MMD VALUES(user, sysdate, 'f3_MMD', 1, null);
    
    SELECT count(*) INTO numar
    FROM locations
    WHERE city = v_oras;
    
    IF numar = 0
    THEN    
        RAISE no_city_found;
    END IF;

    
    SELECT count(employee_id) INTO numar
    FROM departments d JOIN employees e ON e.department_id = d.department_id
                       JOIN locations l ON d.location_id = l.location_id
    WHERE v_oras = city AND help_MMD(employee_id) > 1;
    
    IF numar = 0
    THEN    
        RAISE NO_DATA_FOUND;
    END IF;
    
    RETURN numar;
    
EXCEPTION    
    WHEN no_city_found THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Nu exista orasul'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f3_MMD';
        DBMS_OUTPUT.PUT_LINE('Nu exista orasul');
        return 0;
    WHEN NO_DATA_FOUND THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'In orasul dat nu lucreaza niciun angajat'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f3_MMD';
        DBMS_OUTPUT.PUT_LINE('In orasul dat nu lucreaza niciun angajat');
        return 0;
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('1');
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Exista mai multi angajati in orasul cu numele dat'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f3_MMD';
        DBMS_OUTPUT.PUT_LINE('Exista mai multi angajati in orasul cu numele dat');
        return 0;
    WHEN OTHERS THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Eroare random'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'f3_MMD';
        DBMS_OUTPUT.PUT_LINE('Eroare random');
        return 0;
END f3_MMD;
/

DECLARE
    n NUMBER;
BEGIN
    n := help_MMD(101);
    DBMS_OUTPUT.PUT_LINE(n);
END;
/

DECLARE
    n NUMBER;
BEGIN
    n := f3_MMD('Roma');
    DBMS_OUTPUT.PUT_LINE(n);
END;
/

DECLARE
    n NUMBER;
BEGIN
    n := f3_MMD('Ro00ma');
    DBMS_OUTPUT.PUT_LINE(n);
END;
/

DECLARE
    n NUMBER;
BEGIN
    n := f3_MMD('Seattle');
    DBMS_OUTPUT.PUT_LINE(n);
END;
/

--4

CREATE OR REPLACE PROCEDURE p4_MMD
    (v_man employees.employee_id%TYPE)
IS
    numar NUMBER;
    no_manager_found EXCEPTION;
BEGIN
    INSERT INTO info_MMD VALUES(user, sysdate, 'p4_MMD', 0, null);
    
    SELECT count(*) INTO numar
    FROM employees
    WHERE manager_id = v_man;
    
    IF numar = 0
    THEN    
        RAISE no_manager_found;
    END IF;
    
    SELECT count(*) INTO numar
    FROM employees e
    WHERE v_man IN (SELECT manager_id
                    FROM  employees 
                    START WITH employee_id = e.employee_id
                    CONNECT BY PRIOR manager_id = employee_id);
    
    UPDATE emp_SMECHER e
    SET salary = salary + 0.1*salary
    WHERE v_man IN (SELECT manager_id
                    FROM  employees 
                    START WITH employee_id = e.employee_id
                    CONNECT BY PRIOR manager_id = employee_id);
                    
    dbms_output.put_line(numar);
    IF numar > 0
    THEN 
        UPDATE info_MMD
        SET
            nr_linii = numar
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'p4_MMD'; 
    END IF;
    
EXCEPTION    
    WHEN no_manager_found THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Nu exista managerul cu codul dat'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'p4_MMD';
        DBMS_OUTPUT.PUT_LINE('Nu exista managerul cu codul dat');
    WHEN OTHERS THEN
        UPDATE info_MMD
        SET
            nr_linii = 0,
            eroare = 'Eroare random'
        WHERE
            utilizator = user AND data = sysdate AND comanda = 'p4_MMD';
        DBMS_OUTPUT.PUT_LINE('Eroare random');
END p4_MMD;
/

BEGIN
    p4_MMD(108);  
END;
/

BEGIN
    p4_MMD(1066668);  
END;
/

select * from emp_SMECHER;
select * from info_MMD;

--5&6

CREATE OR REPLACE FUNCTION helper2_MMD
    (dep employees.department_id%TYPE)
RETURN VARCHAR2
IS
    TYPE vector IS ARRAY(7) OF employees.department_id%TYPE;
    d vector := vector();
BEGIN
    SELECT to_char(hire_date,'d') BULK COLLECT INTO d
    FROM employees
    WHERE department_id = dep 
    GROUP BY to_char(hire_date,'d')
    HAVING count(to_char(hire_date,'d')) = (SELECT max(count(to_char(hire_date,'d')))
                                            FROM employees
                                            WHERE department_id = dep
                                            GROUP BY to_char(hire_date,'d'));
    
    RETURN d(d.first);
END helper2_MMD;
/

CREATE OR REPLACE PROCEDURE p5_MMD
IS
    v_r      NUMBER;
    v_numar  NUMBER;
    v_zi     VARCHAR2(15);
BEGIN
    
    FOR i IN (SELECT department_id, department_name
              FROM departments)
    LOOP
        DBMS_OUTPUT.PUT_LINE('DEPARTAMENTUL : ' || i.department_name);
        
        SELECT count(employee_id) INTO v_r
        FROM employees
        WHERE department_id = i.department_id;
        
        IF v_r > 0
        THEN    
            SELECT UNIQUE to_char(hire_date,'d') INTO v_zi
            FROM employees
            WHERE helper2_MMD(i.department_id) = to_char(hire_date,'d');
        
            DBMS_OUTPUT.PUT_LINE('ZIUA : ' || v_zi);
            DBMS_OUTPUT.PUT_LINE('ANGAJATII : ');
            
            FOR j IN (SELECT last_name, round(to_char(sysdate - hire_date)) AS n, salary 
                      FROM employees
                      WHERE department_id = i.department_id AND to_char(hire_date, 'd') = v_zi)
            LOOP
            DBMS_OUTPUT.PUT_LINE(j.last_name || ' |  vechimea: ' || j.n || ' zile | venitul: ' || j.salary );
            END LOOP;
            
        ELSE
            DBMS_OUTPUT.PUT_LINE('In acest departament nu lucreaza nimeni');
        END IF;
        
        DBMS_OUTPUT.PUT_LINE('------------------------');
    END LOOP; 
END p5_MMD;
/


BEGIN
    p5_MMD;
END;
/

BEGIN
    helper2_MMD(30);
END;
/



















