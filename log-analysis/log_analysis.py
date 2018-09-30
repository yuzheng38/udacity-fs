""" FSND Log Analysis

"""

import psycopg2

def task1():
    """ What are the most popular three articles of all time? """
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
    query = '''
            select articles.title, top_three.slug_count
            from
                (select split_part(path, '/', 3) as slug, count(*) as slug_count
                 from log
                 where log.path like '/article/%'
                 group by slug
                 order by slug_count desc
                 limit 3) top_three,
                articles
            where top_three.slug = articles.slug
            order by top_three.slug_count desc;
            '''
    c.execute(query)
    res = c.fetchall()
    db.close()

    for r in res:
        print(r[0] + ' - ' + str(r[1]) + ' views')

def task2():
    """ Who are the most popular article authors of all time? """
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
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
    c.execute(query)
    res = c.fetchall()
    db.close()

    for r in res:
        print(r[1] + ' - ' + str(r[2]) + ' views')

def task3():
    """ On which days did more than 1% of requests lead to errors? """
    db = psycopg2.connect(dbname='news')
    c = db.cursor()
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
                  not_ok.cnt / ok.cnt > 0.01;
            '''
    c.execute(query)
    res = c.fetchall()
    db.close()

    for r in res:
        print('{:%Y-%m-%d} - {:1.3%}'.format(r[0], r[1]))

if __name__ == '__main__':
    print('\n############## task 1 ###############')
    task1()
    print('\n############## task 2 ###############')
    task2()
    print('\n############## task 3 ###############')
    task3()
