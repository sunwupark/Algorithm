-- 코드를 입력하세요
SELECT b.book_id as 'BOOK_ID', a.author_name as 'AUTHOR_NAME', DATE_FORMAT(b.published_date, '%Y-%m-%d') as 'PUBLISHED_DATE'
FROM BOOK as b
JOIN author as a on a.author_id = b.author_id
where b.category = '경제'
order by b.published_date

