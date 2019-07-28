#!/usr/bin/env python3

import psycopg2
import sys


def db_connection():
    try:
        db = psycopg2.connect(dbname="news")
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        print("Wait a moment!")
        c = db.cursor()
        return db, c


def most_viewed_3_articles():
    db, c = db_connection()

    query = "SELECT * FROM most_viewed_articles LIMIT 3;"
    c.execute(query)
    most_viewed_3_articles = c.fetchall()
    db.close()

    print('\n'*1000)
    for most_viewed in most_viewed_3_articles:
        print('"{article}" - {count} views'.format(article=most_viewed[0], count=most_viewed[1]))
    input("\nPress enter to continue")


def most_popular_authors():
    db, c = db_connection()

    query = "SELECT * FROM most_popular_authors"
    c.execute(query)
    most_popular_authors = c.fetchall()
    db.close()

    print('\n'*1000)
    for most_popular in most_popular_authors:
        print(most_popular[0] + " -- " + str(most_popular[1]) + " views")
    input("\nPress enter to continue")


def days_with_more_than_1_per_errors():
    db, c = db_connection()

    query = "SELECT * FROM days_with_more_than_1_per_errors"
    c.execute(query)
    days_with_more_than_1_per_errors = c.fetchall()
    db.close()

    print('\n'*1000)
    for error in days_with_more_than_1_per_errors:
        print(error[0] + " -- " + str(error[1]) + "% errors")
    input("\nPress enter to continue")


if __name__ == '__main__':
    while 1:
        print('\n'*1000)
        print("1: Most Viewed 3 Articles")
        print("2: Most Popular Articles")
        print("3: Days With More Than 1% errors")
        print("4: Exit")
        print()

        option = input()
        if option == '1':
            most_viewed_3_articles()
        elif option == '2':
            most_popular_authors()
        elif option == '3':
            days_with_more_than_1_per_errors()
        elif option == '4':
            break
else:
    print('Importing ...')
