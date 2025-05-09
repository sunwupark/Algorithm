-- 코드를 작성해주세요
select concat(cast(q.QUARTER as char(1)), "Q") as QUARTER, q.ECOLI_COUNT
from (select quarter(differentiation_date) as QUARTER, count(*) as ECOLI_COUNT
    from ecoli_data
    group by quarter(differentiation_date)
    order by quarter(differentiation_date)) as q