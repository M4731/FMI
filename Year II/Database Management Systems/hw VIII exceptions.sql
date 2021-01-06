CREATE TABLE error_MMD(x varchar2(255));

DECLARE
v_nr NUMBER:=&a;
BEGIN
DBMS_OUTPUT.PUT_Line(sqrt(v_nr));
EXCEPTION
      WHEN VALUE_ERROR 
      THEN
      INSERT INTO error_MMD VALUES ('negativ');
      
      commit;
      DBMS_OUTPUT.PUT_LINE('Numarul e negativ');
END;
/

select * from error_MMD;

--2

select * from emp_mmd;

DECLARE
v_nr NUMBER:=&a;
v_cox emp_MMD.last_name%TYPE;
BEGIN
    SELECT last_name INTO v_cox 
    FROM emp_MMD 
    WHERE salary=v_nr; 
    DBMS_OUTPUT.PUT_Line(v_cox);
EXCEPTION
    WHEN NO_DATA_FOUND
    THEN
      DBMS_OUTPUT.PUT_Line('Nu are nimeni acest saariu');
    WHEN  TOO_MANY_ROWS 
    THEN
       DBMS_OUTPUT.PUT_Line('Mai multi angajati au acest salariu');   
END;
/