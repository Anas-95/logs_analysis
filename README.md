## Logs Analysis
This project is to analysing logs from a dataset to answer 3 questions:
###### [1. What are the most popular three articles of all time?](#first-question)
###### [2. Who are the most popular article authors of all time?](#first-question)
###### [3. On which days did more than 1% of requests lead to errors?](#first-question)

### Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
To use this project you need to install some software:
    1. [python3](https://www.python.org/downloads/).
    2. [psycopg2](http://initd.org/psycopg/download/).

After installing the software, you need to download the database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
After downloading the database file newsdata.zip, you need to set up the database prior to
add the VIEWs and prior to running the program. You can set up the database by using this command:
`psql news -f newsdata.sql`

Then add the views to the database by processing the create_views file:
`psql news -f newsdata.sql`

    #first-question
    CREATE VIEW most_viewed_articles AS
        SELECT title, count(path) as views 
        FROM articles 
        LEFT JOIN log ON path like CONCAT('%', slug) 
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
        
Finally, you need to run main.py python file by using this command:
`python3 main.py`

This python file will ask you to choose between 3 different analysis please choose the one you need and test it out. Got a new one? please send a pull request. ^_^

### Authors
Anas Almohsen - Anas95A
See also the list of contributors who participated in this project.

### Acknowledgments
Hat tip to anyone whose code was used
