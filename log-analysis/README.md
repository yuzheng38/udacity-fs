# Log analysis project
Udacity fullstack nanodegree project #3
> This is a Python program that uses psycopg2 to query a mock PostgreSQL database for a fictional news website. The news database includes the following
tables:
> * articles
> * authors
> * log - log of web requests
>
> The queries in the program answer the following questions:
> * What are the most popular three articles of all time?
> * Who are the most popular article authors of all time?
> * On which days did more than 1% of requests lead to errors?

## Design
* Created one function for each of the 3 tasks.
* Avoided correlated subqueries.
* No views were created.

## Development setup
* Python 2.7
* PostgreSQL

## Environment setup
* Set up the `news` database

  * Follow the instructions in <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0">this</a> Udacity lesson to set up a VM to run the PostgreSQL server and support software, using Vagrant.

  * The `news` database is included in the Vagrant configuration.

* Populate the `news` database with schema and data.
  * To download the data, visit <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">here</a> and place the downloaded `newsdata.sql` file in the `vagrant` directory.

  * To create the tables and load the data into the PostgreSQL database, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`


## Instruction
In the project directory, run
```py
python log_analysis.py
```
