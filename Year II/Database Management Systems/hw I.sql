
--6

SELECT t.title, tc.copy_id, tc.status, CASE
                                       WHEN (tc.copy_id, tc.title_id) IN (SELECT copy_id, title_id
                                                                          FROM rental
                                                                          WHERE act_ret_date IS NULL)
                                            THEN 'RENTED'
                                        ELSE
                                            'AVAILABLE'
                                        END AS "status corect"
FROM title t JOIN title_copy tc ON t.title_id = tc.title_id;


--10

SELECT t.last_name, t.first_name, t.title_id, t.copy_id, COUNT(r.copy_id)
FROM rental r, (SELECT* FROM member m, title_copy t) t
WHERE t.title_id = r.title_id (+) AND t.member_id = r.member_id (+) AND t.copy_id = r.copy_id (+)
GROUP BY t.last_name, t.first_name, t.copy_id, t.title_id
ORDER BY t.last_name, t.first_name;


--12 b

SELECT to_char(book_date, 'dd') ziua, COUNT(*)
FROM rental
WHERE to_char(book_date, 'mm yyyy') = to_char(sysdate, 'mm yyyy')
GROUP BY to_char(book_date, 'dd')
ORDER BY 1;

