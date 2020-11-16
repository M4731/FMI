
--1

DECLARE
    numar number(3):=100;
    mesaj1 varchar2(255):='text 1';
    mesaj2 varchar2(255):='text 2';
BEGIN
    DECLARE
        numar number(3):=1;
        mesaj1 varchar2(255):='text 2';
        mesaj2 varchar2(255):='text 3';
    BEGIN
        numar:=numar+1;
        mesaj2:=mesaj2||' adaugat in sub-bloc';
        DBMS_OUTPUT.PUT_LINE(numar);
        DBMS_OUTPUT.PUT_LINE(mesaj1);
        DBMS_OUTPUT.PUT_LINE(mesaj2);
    END;
    numar:=numar+1;
    mesaj1:=mesaj1||' adaugat un blocul principal';
    mesaj2:=mesaj2||' adaugat in blocul principal';
    DBMS_OUTPUT.PUT_LINE(numar);
    DBMS_OUTPUT.PUT_LINE(mesaj1);
    DBMS_OUTPUT.PUT_LINE(mesaj2);
END;
/
--a 2
--b text 2 
--c text 3  adaugat in sub-bloc
--d 101
--e text 1  adaugat un blocul principal
--f text 2  adaugat in blocul principal

--2

--a
SELECT '01' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='01'

UNION

SELECT '02' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='02'

UNION

SELECT '03' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='03'

UNION

SELECT '04' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='04'

UNION

SELECT '05' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='05'

UNION

SELECT '06' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='06'

UNION

SELECT '07' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='07'

UNION

SELECT '08' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='08'

UNION

SELECT '09' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='09'

UNION

SELECT '10' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='10'

UNION

SELECT '11' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='11'

UNION

SELECT '12' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='12'

UNION

SELECT '13' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='13'

UNION

SELECT '14' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='14'

UNION

SELECT '15' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='15'

UNION

SELECT '16' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='16'

UNION

SELECT '17' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='17'

UNION

SELECT '18' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='18'

UNION

SELECT '19' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='19'

UNION

SELECT '20' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='20'

UNION

SELECT '21' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='21'

UNION

SELECT '22' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='22'

UNION

SELECT '23' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='23'

UNION

SELECT '24' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='24'

UNION

SELECT '25' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='25'

UNION

SELECT '26' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='26'

UNION

SELECT '27' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='27'

UNION

SELECT '28' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='28'

UNION

SELECT '29' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='29'

UNION

SELECT '30' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='30'

UNION

SELECT '31' as day, count(*)
FROM rental
WHERE to_char(book_date, 'mm') LIKE '%10%' and to_char(book_date, 'dd')='31';


--b
 
CREATE TABLE octombrie_mmd (
    id NUMBER(5) PRIMARY KEY,
    data DATE
);

select * from octombrie_mmd;

select * from rental
WHERE book_date like '%OCT%';

DECLARE
    i_id POSITIVE := 1;
    i_data DATE := Last_Day(Add_Months('01-OCT-2020',-1))+1;
BEGIN
    LOOP
        INSERT INTO octombrie_mmd VALUES (
            i_id,
            i_data
         );
         i_id := i_id + 1;
         i_data := i_data +1;
         
         EXIT WHEN i_id > 31;    
     END LOOP;
END;
/

SELECT o.id as "Ziua", count(r.book_date) as "Nr_imprumuturi"
FROM rental r RIGHT JOIN octombrie_mmd o ON to_date(r.book_date,'dd-mm-yyyy') = to_date(o.data,'dd-mm-yyyy')
GROUP BY o.id
ORDER BY o.id;

--3

DECLARE 
    v_nume member.last_name%type := '&nume_dorit';
    v_nr number(5);
BEGIN
    SELECT count(r.title_id)
    INTO v_nr
    FROM member m JOIN rental r USING(member_id)
    WHERE lower(v_nume) like lower(last_name)
    GROUP BY last_name;
    DBMS_OUTPUT.PUT_LINE(v_nume || ' a imprumutat ' || v_nr || ' filme.');
EXCEPTION
    WHEN no_data_found THEN 
        DBMS_OUTPUT.PUT_LINE('acest membru nu a imprumutat niciun film.');
    WHEN too_many_rows THEN 
        DBMS_OUTPUT.PUT_LINE('exista mai multi membri cu acest nume.');
END;
/

--4
 
 
select * from member;
select * from title;
select * from title_copy;
select * from rental;

 
DECLARE 
    v_nume member.last_name%type := '&nume_dorit';
    v_nr number(5);
    v_contoar number(5);
BEGIN
    SELECT count(r.title_id)
    INTO v_nr
    FROM member m JOIN rental r USING(member_id)
    WHERE lower(v_nume) like lower(last_name)
    GROUP BY last_name;
    
    SELECT count(*)
    INTO v_contoar
    FROM title;
    
    IF (v_nr > 0.75 * v_contoar) THEN
        DBMS_OUTPUT.PUT_LINE(v_nume || ' a imprumutat ' || v_nr || ' filme si este categoria 1.');
    ELSIF (v_nr > 0.5 * v_contoar) THEN
        DBMS_OUTPUT.PUT_LINE(v_nume || ' a imprumutat ' || v_nr || ' filme si este categoria 2.');
    ELSIF (v_nr > 0.25 * v_contoar) THEN
        DBMS_OUTPUT.PUT_LINE(v_nume || ' a imprumutat ' || v_nr || ' filme si este categoria 3.');
    ELSE
        DBMS_OUTPUT.PUT_LINE(v_nume || ' a imprumutat ' || v_nr || ' filme si este categoria 4.');
    END IF;
    
EXCEPTION
    WHEN no_data_found THEN 
        DBMS_OUTPUT.PUT_LINE('acest membru nu a imprumutat niciun film.');
    WHEN too_many_rows THEN 
        DBMS_OUTPUT.PUT_LINE('exista mai multi membri cu acest nume.');
END;
/   
      
--5   

CREATE TABLE member_mmd AS 
                        SELECT * 
                        FROM member;
        
select * from member_mmd;     

ALTER TABLE member_mmd
ADD discount VARCHAR2(10);
            
DECLARE 
    v_nume member.member_id%type := &cod_dorit;
    v_nr number(5);
    v_contoar number(5);
BEGIN
    SELECT count(r.title_id)
    INTO v_nr
    FROM member m JOIN rental r USING(member_id)
    WHERE v_nume = member_id
    GROUP BY last_name;
    
    SELECT count(*)
    INTO v_contoar
    FROM title;
    
    IF (v_nr > 0.75 * v_contoar) THEN
        UPDATE member_mmd
        SET discount = '10%'
        WHERE v_nume = member_id;
        DBMS_OUTPUT.PUT_LINE('discountul a fost actualizat');
    ELSIF (v_nr > 0.5 * v_contoar) THEN
        UPDATE member_mmd
        SET discount = '5%'
        WHERE v_nume = member_id;
        DBMS_OUTPUT.PUT_LINE('discountul a fost actualizat');
    ELSIF (v_nr > 0.25 * v_contoar) THEN
        UPDATE member_mmd
        SET discount = '3%'
        WHERE v_nume = member_id;
        DBMS_OUTPUT.PUT_LINE('discountul a fost actualizat');
    ELSE
        UPDATE member_mmd
        SET discount = '0%'
        WHERE v_nume = member_id;
        DBMS_OUTPUT.PUT_LINE('discountul a fost actualizat');
    END IF;
    
EXCEPTION
    WHEN no_data_found THEN 
        DBMS_OUTPUT.PUT_LINE('acest membru nu a imprumutat niciun film.');
    WHEN too_many_rows THEN 
        DBMS_OUTPUT.PUT_LINE('exista mai multi membri cu acest nume.');
END;
/         

commit;
    
    
    













