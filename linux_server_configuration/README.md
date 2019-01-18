# Neighborhood map single page web app
Udacity fullstack nanodegree project #6
> In this project, the <a href="https://github.com/yuzheng38/udacity-fs/tree/master/catalog">Catalog</a> web application from project #4 is hosted by an Apache web server on an Amazon AWS Lightsail instance (Ubuntu OS).

Note: Google OAuth is not supported at the moment due to authorized redirect URI and authorized domain policies from Google. Steps I have taken to resolve this so far:
* In <a href="https://console.cloud.google.com/apis/credentials">Google Cloud Console > API & Services > Credentials page</a>, raised a domain verification request. Updated my router to handle the domain verification request from Google. Domain was added successfully after verification.
* OAuth consent screen is being verified at the moment, after adding a new Authorized redirect URI: http://ec2-3-86-117-144.compute-1.amazonaws.com/login
>



## Instructions
You can visit the project via:
* Url: <a href="http://ec2-3-86-117-144.compute-1.amazonaws.com/">http://ec2-3-86-117-144.compute-1.amazonaws.com/</a>
or 
* IP: <a href="3.86.117.144">3.86.117.144</a>

in Chrome. You will only be able to explore <i>public</i> pages of the app at the moment. 

## Summary of packages installed
* Ubuntu packages
    * apache2
    * libapache2-mod-wsgi
    * git
    * libpq-dev
    * python-dev
    * python-pip
    * postgresql
    * postgresql-contrib
* Python2 packages
    * flask
    * requests
    * passlib
    * sqlalchemy 
    * flask-sqlalchemy
    * psycopg2-binary

## Summary of configurations
* general
    * updated all currently installed packages
    * added new user `grader`
    * gave sudo access to `grader`

* ssh
    * Changed `ssh` port from 22 to 2200.
    * Disabled `root` login
    * In addition, key-based authentication is enforced. 
    * Key-based authentication for `grader` user. Private key shared in submission note. 

* Firewall
    * allow connections for SSH (port 2200), HTTP (port 80), and NTP (port 123)
* postgresql
    * created user and role `catalog` with permission to create db
* Local timezone
    * Changed to UTC timezone

## Reference
Linux server setup: 

https://help.ubuntu.com/lts/serverguide/serverguide.pdf

Apache2 web server:

https://httpd.apache.org/docs/2.4/getting-started.html

WSGI app configuration:

https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html

Google OAuth API:

https://console.cloud.google.com/apis/dashboard

Amazon LightSail:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
