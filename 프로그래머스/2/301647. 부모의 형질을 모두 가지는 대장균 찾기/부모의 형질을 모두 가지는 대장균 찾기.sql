-- 코드를 작성해주세요
select e.id as ID, e.genotype as GENOTYPE, p.genotype as PARENT_GENOTYPE
from ecoli_data as e
join ecoli_data as p on e.parent_id = p.id
where e.genotype & p.genotype = p.genotype
order by e.id
