--Exercitiul 1

CREATE TABLE emp_mmd AS 
SELECT * 
FROM employees;

select * from emp_mmd
where commission_pct is null
order by salary;

DECLARE
    TYPE tablou_imbricat IS TABLE OF employees.employee_id%type;
    t tablou_imbricat := tablou_imbricat();
    sal employees.salary%type;
BEGIN
    SELECT employee_id
    BULK COLLECT INTO t
    FROM employees 
    WHERE commission_pct is null
    ORDER BY salary;
    
    FOR i IN (t.FIRST + 5)..t.LAST LOOP
        t.DELETE(i);
    END LOOP;
    
    FOR i IN t.FIRST..t.LAST LOOP
        DBMS_OUTPUT.PUT(t(i) || ' : ');
        
        SELECT salary
        INTO sal
        FROM employees
        WHERE employee_id = t(i);
        
        DBMS_OUTPUT.PUT(sal || ' -> ');
        DBMS_OUTPUT.PUT(sal*1.05);
        
        UPDATE emp_mmd
        SET salary = 1.05*salary
        WHERE employee_id = t(i);
        
        DBMS_OUTPUT.NEW_LINE;
    END LOOP;
    
END;
/

commit;

--Exercitiul 2

--a

CREATE OR REPLACE TYPE tip_orase_mmd IS TABLE OF VARCHAR2(20);
/

CREATE TABLE excursie_mmd (cod_excursie NUMBER(4),
                           denumire VARCHAR2(20),
                           status VARCHAR2(20)
                            );

ALTER TABLE excursie_mmd
ADD (orase tip_orase_mmd)
NESTED TABLE orase STORE AS tabel_tip_orase_mmd;

INSERT INTO excursie_mmd
VALUES(100,'Moonte','disponibil',tip_orase_mmd('Brasov','Clooj'));

INSERT INTO excursie_mmd
VALUES(101,'Mare','disponibil',tip_orase_mmd('Constanta'));

INSERT INTO excursie_mmd
VALUES(102,'Spania','disponibil',tip_orase_mmd('Madrid','Barcelona','Valencia'));

INSERT INTO excursie_mmd
VALUES(103,'Pescooit','anulata',tip_orase_mmd('Baikal'));

INSERT INTO excursie_mmd
VALUES(104,'Ierusalim','disponibil',tip_orase_mmd('Ierusalim'));

ALTER TABLE excursie_mmd
ADD PRIMARY KEY (cod_excursie);

--b

DECLARE
    t excursie_mmd.cod_excursie%type := &excursie;
    a tip_orase_mmd := tip_orase_mmd();
    cerere_oras VARCHAR2(20) := '&oras';
BEGIN
    SELECT orase
    INTO a
    FROM excursie_mmd
    WHERE cod_excursie = t;
    
    a.EXTEND;
    a(a.LAST) := cerere_oras;
    
    UPDATE excursie_mmd
    SET orase = a
    WHERE cod_excursie = t;
    
END;
/
commit;

DECLARE
    t excursie_mmd.cod_excursie%type := &excursie;
    a tip_orase_mmd := tip_orase_mmd();
    cerere_oras VARCHAR2(20) := '&oras';
    aux cerere_oras%type;
    aux2 cerere_oras%type;
BEGIN
    SELECT orase
    INTO a
    FROM excursie_mmd
    WHERE cod_excursie = t;
    
    a.EXTEND;
    aux := a(2);
    a(2) := cerere_oras;
    FOR i IN a.FIRST+2..a.LAST LOOP
        aux2 := a(i);
        a(i) := aux;
        aux := aux2;
    END LOOP;
    
    UPDATE excursie_mmd
    SET orase = a
    WHERE cod_excursie = t;
    
END;
/
commit;

DECLARE
    t excursie_mmd.cod_excursie%type := &excursie;
    a tip_orase_mmd := tip_orase_mmd();
    cerere_oras1 VARCHAR2(20) := '&oras1';
    cerere_oras2 VARCHAR2(20) := '&oras2';
    aux cerere_oras1%type;
    y1 NUMBER(5);
    y2 y1%type;
BEGIN
    SELECT orase
    INTO a
    FROM excursie_mmd
    WHERE cod_excursie = t;
    
    FOR i IN (a.FIRST)..(a.LAST) LOOP
        IF a(i) LIKE cerere_oras1
            THEN y1 := i;
        END IF;
        IF a(i) LIKE cerere_oras2
            THEN y2 := i;
        END IF;
    END LOOP;
    
    aux := a(y1);
    a(y1) := a(y2);
    a(y2) := aux;
    
    UPDATE excursie_mmd
    SET orase = a
    WHERE cod_excursie = t;
    
END;
/
commit;

DECLARE
    t excursie_mmd.cod_excursie%type := &excursie;
    a tip_orase_mmd := tip_orase_mmd();
    cerere_oras VARCHAR2(20) := '&oras';
BEGIN
    SELECT orase
    INTO a
    FROM excursie_mmd
    WHERE cod_excursie = t;
    
    FOR i IN (a.FIRST)..(a.LAST) LOOP
        IF a(i) LIKE cerere_oras
            THEN a.DELETE(i);
        END IF;
    END LOOP;
    
    UPDATE excursie_mmd
    SET orase = a
    WHERE cod_excursie = t;
    
END;
/
commit;

--c

DECLARE
    t excursie_mmd.cod_excursie%type := &excursie;
    a tip_orase_mmd := tip_orase_mmd();
BEGIN
    SELECT orase
    INTO a
    FROM excursie_mmd
    WHERE cod_excursie = t;
    
    DBMS_OUTPUT.PUT(t || ' | ' || a.count || ' | ' );
    
    FOR i IN (a.FIRST)..(a.LAST-1) LOOP
       DBMS_OUTPUT.PUT(a(i) || ', ');
    END LOOP;
    DBMS_OUTPUT.PUT(a(a.LAST) ||'.');
    
    DBMS_OUTPUT.NEW_LINE;
END;
/
--d

DECLARE
    a tip_orase_mmd := tip_orase_mmd();
    nr NUMBER(6);
    TYPE tablou_imbricat IS TABLE OF excursie_mmd%rowtype;
    v tablou_imbricat := tablou_imbricat();
BEGIN
    SELECT *
    BULK COLLECT INTO v
    FROM excursie_mmd;
    
    FOR i IN v.FIRST..v.LAST LOOP
        DBMS_OUTPUT.PUT(v(i).cod_excursie || ' | ' );
        
        a := v(i).orase;
        FOR i IN (a.FIRST)..(a.LAST-1) LOOP
            DBMS_OUTPUT.PUT(a(i) || ', ');
        END LOOP;
        DBMS_OUTPUT.PUT(a(a.LAST) ||'.');
        
        DBMS_OUTPUT.NEW_LINE;
    END LOOP;
END;
/

--e

desc excursie_mmd;
select * from excursie_mmd;

DECLARE
    a tip_orase_mmd := tip_orase_mmd();
    nr NUMBER(6) := 999999;
    TYPE tablou_imbricat IS TABLE OF excursie_mmd%rowtype;
    v tablou_imbricat := tablou_imbricat();
BEGIN
    SELECT *
    BULK COLLECT INTO v
    FROM excursie_mmd;
    
    FOR i IN v.FIRST..v.LAST LOOP
        a := v(i).orase;
        IF a.count < nr
            THEN nr := a.count;
        END IF;
    END LOOP;
    
    FOR i IN v.FIRST..v.LAST LOOP
        a := v(i).orase;
        IF a.count = nr
            THEN UPDATE excursie_mmd
                 SET status = 'anulata'
                 WHERE cod_excursie = v(i).cod_excursie;
        END IF;
    END LOOP;
    
END;
/
commit;


