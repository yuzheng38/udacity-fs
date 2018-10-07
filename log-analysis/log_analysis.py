#!/usr/bin/env python
""" FSND Log Analysis

"""

import psycopg2


def print_top_three_articles():
    """ What are the most popular three articles of all time? """
    query = '''
            select articles.title, top_articles.slug_count
            from
                (select path, count(*) as slug_count
                 from log
                 where log.path like '/article/%'
                 group by path
                 order by slug_count desc) top_articles,
                articles
            where top_articles.path = '/article/' || articles.slug
            order by top_articles.slug_count desc
            limit 3;
            '''
    res = execute_query(query)

    if res:
        print('\nWhat are the most popular three articles of all time?')
        for r in res:
            print(r[0] + ' - ' + str(r[1]) + ' views')


def print_most_popular_authors():
    """ Who are the most popular article authors of all time? """
    query = '''
            select authors.id, authors.name,
                   sum(count_by_slug.cnt) as sum_by_author
            from authors, articles,
                 (select split_part(path, '/', 3) as slug, count(*) as cnt
                  from log
                  where path like '/article/%'
                  group by slug) count_by_slug
            where authors.id = articles.author and
                  count_by_slug.slug = articles.slug
            group by authors.id
            order by sum_by_author desc
            '''
    res = execute_query(query)

    if res:
        print('\nWho are the most popular article authors of all time? ')
        for r in res:
            print(r[1] + ' - ' + str(r[2]) + ' views')


def print_days_of_error():
    """ On which days did more than 1% of requests lead to errors? """
    query = '''
            select ok.day, not_ok.cnt/ok.cnt as error_percentage
            from
                (select date_trunc('day', time) as day, count(id) as cnt
                 from log
                 where status like '200%'
                 group by day) ok,
                (select date_trunc('day', time) as day,
                    cast(count(id) as decimal) as cnt
                 from log
                 where status not like '200%'
                group by day) not_ok
            where not_ok.day = ok.day and
                  not_ok.cnt / (ok.cnt + not_ok.cnt) > 0.01;
            '''
    res = execute_query(query)

    if res:
        print('\nOn which days did more than 1% of requests lead to errors?')
        for r in res:
            print('{:%Y-%m-%d} - {:1.3%}'.format(r[0], r[1]))


def execute_query(query):
    try:
        db = psycopg2.connect(dbname='news')
        c = db.cursor()
        c.execute(query)
        res = c.fetchall()
        return res
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        db.close()


if __name__ == '__main__':
    print_top_three_articles()
    print_most_popular_authors()
    print_days_of_error()
