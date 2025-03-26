-- 코드를 입력하세요
SELECT o.animal_id as 'ANIMAL_ID', o.name as 'NAME'
from animal_outs as o
left outer join animal_ins as i on o.animal_id = i.animal_id
where i.animal_id is NULL
order by o.animal_id, o.name