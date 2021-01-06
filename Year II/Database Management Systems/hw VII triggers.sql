
--1

CREATE OR REPLACE TRIGGER tex1_MMD
BEFORE DELETE ON dep_MMD
BEGIN
    IF user NOT LIKE 'SCOTT'
        THEN RAISE_APPLICATION_ERROR(-20001,'Numai Scott poate sterge din tabelul emp_MMD');
    END IF;
END;
/

DELETE FROM dep_MMD
WHERE department_id = 270;

DROP TRIGGER tex1_MMD;

--2

CREATE OR REPLACE TRIGGER tex2_MMD
BEFORE UPDATE ON emp_MMD
FOR EACH ROW
BEGIN
    IF (:NEW.commission_pct > 0.5)
        THEN RAISE_APPLICATION_ERROR(-20001,'Comisionul nu poate depasi 50%');
    END IF;
END;
/

UPDATE emp_MMD
SET commission_pct = 0.51
WHERE employee_id = 1;

DROP TRIGGER tex2_MMD;

select * from emp_MMD;

--3

CREATE TABLE info_dept_MMD
AS SELECT * FROM info_dept_prof;

select * from info_dept_MMD;

ALTER TABLE info_dept_MMD
ADD numar NUMBER;

select * from dep_mmd;

DECLARE 
    v_nr NUMBER;
BEGIN
    FOR i IN (SELECT department_id
              FROM dep_MMD)
    LOOP
        UPDATE info_dept_MMD
        SET numar = 0
        WHERE id = i.department_id;
    
        SELECT count(employee_id) INTO v_nr
        FROM emp_mmd
        WHERE department_id = i.department_id;
        
        UPDATE info_dept_MMD
        SET numar = v_nr
        WHERE id = i.department_id;
    END LOOP;
END;
/

create table info_emp_MMD as select * from info_emp_prof;
select * from info_emp_MMD;

CREATE OR REPLACE TRIGGER tex3_MMD
AFTER DELETE OR UPDATE OR INSERT ON info_emp_MMD
FOR EACH ROW
BEGIN
  IF inserting 
  THEN
    UPDATE info_dept_MMD
       SET numar=numar+1
     WHERE id=:NEW.id_dept;
  ELSIF deleting 
  THEN
    UPDATE info_dept_MMD
       SET numar=numar-1
     WHERE id=:OLD.id_dept;
  ELSIF UPDATING 
  THEN
    IF(:NEW.id_dept != :OLD.id_dept) 
    THEN
    UPDATE info_dept_MMD
       SET numar=numar+1
     WHERE id=:NEW.id_dept;
     
    UPDATE info_dept_MMD
       SET numar=numar-1
     WHERE id=:OLD.id_dept;
    END IF; 
  END IF;
END;
/

--4

CREATE OR REPLACE PACKAGE pachetel_MMD
AS
    v_nr NUMBER;
END pachetel_mmd;
/


CREATE OR REPLACE TRIGGER tex4_MMD
BEFORE UPDATE OR INSERT ON emp_MMD
FOR EACH ROW
DECLARE 
BEGIN
    SELECT count(employee_id) INTO pachetel_MMD.v_nr
    FROM emp_MMD
    WHERE department_id = :NEW.department_id;

  IF pachetel_MMD.v_nr > 45
  THEN
    RAISE_APPLICATION_ERROR(-20001,'Intr-un departament nu pot lucra mai mult de 45 de angajati.');
  END IF;
END;
/

select * from emp_mmd;
select * from dep_mmd;

INSERT INTO emp_mmd
VALUES (60000,'a','b','ddmail','hhh22',sysdate,'SA_MAN',1,null,1,50);


--5

CREATE TABLE emp_test_MMD (employee_id NUMBER(5) PRIMARY KEY,
                           last_name VARCHAR2(50),
                           first_name VARCHAR2(50),
                           department_id NUMBER(5));

CREATE TABLE dept_test_MMD (department_id NUMBER(5) PRIMARY KEY,
                            department_name VARCHAR2(40));

INSERT INTO dept_test_MMD
VALUES(10,'manele_petreceri');

insert into emp_test_MMD
VALUES (100,'Matei','Sefu',10);

insert into emp_test_MMD
VALUES (101,'Dani','Mocanu',10);

select * from emp_test_MMD;
select * from dept_test_MMD;

CREATE OR REPLACE TRIGGER tex5_MMD
AFTER DELETE OR UPDATE ON dept_test_MMD
FOR EACH ROW
BEGIN
    IF deleting
    THEN
        DELETE FROM emp_test_MMD
        WHERE department_id = :OLD.department_id;
    ELSIF updating
    THEN
        UPDATE emp_test_MMD
        SET department_id = :NEW.department_id
        WHERE department_id = :OLD.department_id;
    END IF;
END;
/

DELETE FROM dept_test_MMD
WHERE department_id = 10;

UPDATE dept_test_MMD
SET department_id = 20
WHERE department_id = 10;

ALTER TABLE emp_test_MMD
ADD CONSTRAINT fk_1 FOREIGN KEY (department_id) REFERENCES dept_test_mmd(department_id);

ALTER TABLE emp_test_MMD
DROP CONSTRAINT fk_1;

ALTER TABLE emp_test_MMD
ADD CONSTRAINT fk_2 FOREIGN KEY (department_id) REFERENCES dept_test_mmd(department_id) ON DELETE CASCADE;

DROP TRIGGER tex5_MMD;

desc emp_test_mmd;

ALTER TABLE emp_test_MMD
DROP CONSTRAINT fk_2;

ALTER TABLE emp_test_MMD
ADD CONSTRAINT fk_3 FOREIGN KEY (department_id) REFERENCES dept_test_mmd(department_id) ON DELETE SET NULL;

select * from user_constraints
where table_name = 'EMP_TEST_MMD';



