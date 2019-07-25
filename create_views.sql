CREATE VIEW most_viewed_articles AS
    SELECT title, count(path) as views 
    FROM articles 
    LEFT JOIN log ON path like CONCAT('%/article/', slug) 
    GROUP BY title 
    ORDER BY views DESC;

CREATE VIEW most_popular_authors AS
    SELECT au.name, sum(m.views) AS views 
    FROM authors AS au 
    LEFT JOIN articles AS ar ON au.id = ar.author 
    JOIN most_viewed_articles AS m on m.title = ar.title 
    GROUP BY au.name 
    ORDER BY views DESC;

CREATE VIEW days_with_more_than_1_per_errors AS
    SELECT to_char(log.time, 'FMMonth DD, YYYY') AS date, TO_CHAR((count(status_4))::FLOAT / COUNT(*) * 100, '9.0') AS status_4_percent 
    FROM log 
    LEFT JOIN (SELECT id, time::DATE AS date, status FROM log WHERE status LIKE '4__ %') AS status_4
    ON status_4.id = log.id
    GROUP BY TO_CHAR(log.time, 'FMMonth DD, YYYY')
    HAVING COUNT(status_4) >= ((COUNT(*)-COUNT(status_4)) * .01);