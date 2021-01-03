

--1

--a

DECLARE 
    v_id employees.employee_id%TYPE;
    v_nume employees.last_name%TYPE;
    v_salariu employees.salary%TYPE;
    CURSOR emp (par jobs.job_title%TYPE) IS
        SELECT employee_id, last_name, salary
        FROM employees e join jobs j ON e.job_id = j.job_id
        WHERE j.job_title = par;
BEGIN

    FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            DBMS_OUTPUT.PUT_LINE('La jobul '|| i.job_title || ' lucreaza angajatii ');
            OPEN emp(i.job_title);
            LOOP
                    FETCH emp INTO v_id, v_nume, v_salariu;
                    EXIT WHEN emp%NOTFOUND;
                    DBMS_OUTPUT.PUT_LINE(v_id || ' | ' ||  v_nume || ' | ' || v_salariu);
            END LOOP;
            CLOSE emp;
        DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
        END LOOP;
END;
/
   
--b

DECLARE 
    CURSOR emp (par jobs.job_title%TYPE) IS
        SELECT employee_id, last_name, salary
        FROM employees e join jobs j ON e.job_id = j.job_id
        WHERE j.job_title = par;
BEGIN

    FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            DBMS_OUTPUT.PUT_LINE('La jobul '|| i.job_title || ' lucreaza angajatii ');
            FOR j in emp(i.job_title)
            LOOP
                    DBMS_OUTPUT.PUT_LINE(j.employee_id || ' | ' || j.last_name || ' | ' || j.salary);
            END LOOP;
        DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
        END LOOP;
END;
/     
    
--c

BEGIN

    FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            DBMS_OUTPUT.PUT_LINE('La jobul '|| i.job_title || ' lucreaza angajatii ');
            FOR j in (SELECT employee_id, last_name, salary
                      FROM employees e join jobs jo ON e.job_id = jo.job_id
                      WHERE jo.job_title = i.job_title)
            LOOP
                    DBMS_OUTPUT.PUT_LINE(j.employee_id || ' | ' || j.last_name || ' | ' || j.salary);
            END LOOP;
        DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
        END LOOP;
END;
/   

--d

DECLARE 
    v_id employees.employee_id%TYPE;
    v_nume employees.last_name%TYPE;
    v_salariu employees.salary%TYPE;
    v_iobtitle jobs.job_title%TYPE;
    TYPE refcursor IS REF CURSOR;
    CURSOR iob IS
        SELECT job_title, CURSOR (SELECT employee_id, last_name, salary
                                  FROM employees e join jobs j ON e.job_id = j.job_id
                                  WHERE j.job_title = jo.job_title)
        FROM jobs jo;
    v_refcursor refcursor;
BEGIN
    OPEN iob;
    LOOP
        FETCH iob INTO v_iobtitle,v_refcursor;
        EXIT WHEN iob%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE('La jobul '|| v_iobtitle || ' lucreaza angajatii ');
        LOOP
                FETCH v_refcursor INTO v_id, v_nume, v_salariu;
                EXIT WHEN v_refcursor%NOTFOUND;
                DBMS_OUTPUT.PUT_LINE(v_id || ' | ' ||  v_nume || ' | ' || v_salariu);
        END LOOP;
    DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
    END LOOP;
    CLOSE iob;
        
END;
/  
     
--2

DECLARE 
    v_numar NUMBER(4);
    v_numartotal NUMBER(4) :=0;
    v_totsal NUMBER(8);
    v_totsaltotal NUMBER(10):= 0;
    CURSOR emp (par jobs.job_title%TYPE) IS
        SELECT employee_id, last_name, salary
        FROM employees e join jobs j ON e.job_id = j.job_id
        WHERE j.job_title = par;
BEGIN
    FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            v_numar := 0;
            v_totsal := 0;
            DBMS_OUTPUT.PUT_LINE('La jobul '|| i.job_title || ' lucreaza angajatii ');
            FOR j in emp(i.job_title)
            LOOP
                    v_totsal := v_totsal + j.salary;
                    v_numar := v_numar +1;
                    DBMS_OUTPUT.PUT_LINE( '(' || v_numar || ') ' || j.employee_id || ' | ' || j.last_name || ' | ' || j.salary);
            END LOOP;
        v_numartotal := v_numartotal + v_numar;
        v_totsaltotal := v_totsaltotal + v_totsal;
        DBMS_OUTPUT.PUT_LINE('Total angajati job: ' || v_numar);
        DBMS_OUTPUT.PUT_LINE('Total venituri job: ' || v_totsal);
        DBMS_OUTPUT.PUT_LINE('Medie venituri job: ' || (v_totsal/v_numar) );
        DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
        END LOOP;
    DBMS_OUTPUT.PUT_LINE('Total angajati firma: ' || v_numartotal);
    DBMS_OUTPUT.PUT_LINE('Total venituri firma: ' || v_totsaltotal);
    DBMS_OUTPUT.PUT_LINE('Medie venituri firma: ' || (v_totsaltotal/v_numartotal) );
END;
/   
        
--3
SELECT * FROM jobs;
SELECT * FROM employees;

DECLARE 
    v_numar NUMBER(4);
    v_ajutor NUMBER(10);
    v_numartotal NUMBER(4) :=0;
    v_totsal NUMBER(8);
    v_totsaltotal NUMBER(10):= 0;
    CURSOR emp (par jobs.job_title%TYPE) IS
        SELECT employee_id, last_name, salary, commission_pct
        FROM employees e join jobs j ON e.job_id = j.job_id
        WHERE j.job_title = par;
BEGIN
    FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            v_numar := 0;
            v_totsal := 0;
            FOR j in emp(i.job_title)
            LOOP
                    IF j.commission_pct IS NOT NULL 
                        THEN    
                            v_totsal := v_totsal + j.salary + j.salary*j.commission_pct;
                            --DBMS_OUTPUT.PUT_LINE( j.commission_pct);
                    ELSE
                        v_totsal := v_totsal + j.salary;
                    END IF;
                    v_numar := v_numar +1;
            END LOOP;
        v_numartotal := v_numartotal + v_numar;
        v_totsaltotal := v_totsaltotal + v_totsal;
        END LOOP;
    
        FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            v_numar := 0;
            v_totsal := 0;
            DBMS_OUTPUT.PUT_LINE('La jobul '|| i.job_title || ' lucreaza angajatii ');
            FOR j in emp(i.job_title)
            LOOP
                    IF j.commission_pct IS NOT NULL 
                        THEN    
                            v_ajutor := (100*(j.salary+j.salary*j.commission_pct))/v_totsaltotal;
                            v_totsal := v_totsal + j.salary + j.salary*j.commission_pct;
                            --DBMS_OUTPUT.PUT_LINE( j.commission_pct);
                    ELSE
                        v_ajutor := (100*j.salary)/v_totsaltotal;
                        v_totsal := v_totsal + j.salary;
                    END IF;
                    v_numar := v_numar +1;
                    DBMS_OUTPUT.PUT_LINE( '(' || v_numar || ') ' || j.employee_id || ' | ' || j.last_name || ' | ' || j.salary || ' | ' || v_ajutor || '%');
            END LOOP;
        DBMS_OUTPUT.PUT_LINE('Total angajati job: ' || v_numar);
        DBMS_OUTPUT.PUT_LINE('Total venituri job: ' || v_totsal);
        DBMS_OUTPUT.PUT_LINE('Medie venituri job: ' || (v_totsal/v_numar) );
        DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
        END LOOP;
    DBMS_OUTPUT.PUT_LINE('Total angajati firma: ' || v_numartotal);
    DBMS_OUTPUT.PUT_LINE('Total venituri firma: ' || v_totsaltotal);
    DBMS_OUTPUT.PUT_LINE('Medie venituri firma: ' || (v_totsaltotal/v_numartotal) );
END;
/   
   
--4

DECLARE 
    v_numar NUMBER(4);
    v_numartotal NUMBER(4) :=0;
    v_totsal NUMBER(8);
    v_totsaltotal NUMBER(10):= 0;
    CURSOR emp (par jobs.job_title%TYPE) IS
        SELECT employee_id, last_name, salary
        FROM employees e join jobs j ON e.job_id = j.job_id
        WHERE j.job_title = par
        ORDER BY salary DESC;
BEGIN
    FOR i in (SELECT job_id, job_title
              FROM jobs)
        LOOP
            v_numar := 0;
            v_totsal := 0;
            DBMS_OUTPUT.PUT_LINE('La jobul '|| i.job_title || ' lucreaza angajatii ');
            FOR j in emp(i.job_title)
            LOOP
                    EXIT WHEN emp%ROWCOUNT > 5 OR emp%NOTFOUND;
                    v_totsal := v_totsal + j.salary;
                    v_numar := v_numar +1;
                    DBMS_OUTPUT.PUT_LINE( '(' || v_numar || ') ' || j.employee_id || ' | ' || j.last_name || ' | ' || j.salary);
            END LOOP;
        v_numartotal := v_numartotal + v_numar;
        v_totsaltotal := v_totsaltotal + v_totsal;
        IF v_numar <5 
            THEN  DBMS_OUTPUT.PUT_LINE('La job lucreaza mai putin de 5 angajati.');
        END IF;
        DBMS_OUTPUT.PUT_LINE(' ------------------------- ');
        END LOOP;
END;
/   