SELECT 
    d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM 
    developers d
WHERE 
    (d.skill_code & (SELECT code FROM skillcodes WHERE name = 'Python')) = (SELECT code FROM skillcodes WHERE name = 'Python')
    OR
    (d.skill_code & (SELECT code FROM skillcodes WHERE name = 'C#')) = (SELECT code FROM skillcodes WHERE name = 'C#')
ORDER BY 
    d.ID