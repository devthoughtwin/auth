##User Login Auth Demo

##With Docker

## Run the application With Docker
    docker-compose up --build

## Entering the postgres container
    docker exec -it my_postgres_container psql -U postgres

##Without Docker

## Clone the project
Clone the project from Bitbucket:

## Create Environment file

    Go to the settings folder then create .env file

    Note : Like see the .example_env file in project root folder, same veriable copy and paste in .env file in settings folder then update env varible .

## Install Python
    
    sudo apt-get update && sudo apt-get install python3.6 python3.5 virtualenv

# OS Dependencies
    sudo apt-get update &&  sudo apt-get install python3-dev python3.7-dev python3.6-dev build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

## Install PostgreSQL

If we need postgress
    
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'
    
    sudo apt-get update
    
    sudo apt-get install postgresql-latest

If we need postgress with postgis
    
    sudo apt-get install binutils libproj-dev gdal-bin
    sudo apt-get install postgis
    https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/postgis/

## Create environment & Install Dependencies

    virtualenv --python=python3.7 /home/username/Env Folder/env_name

    source /home/username/Env Folder/env_name/bin/activate

    pip install -r requirements.txt

## Alternative
Create virtual env:

    virtualenv -p python3 directory/env_name

Activate the environment:

    source directory/env/bin/activate

## Database
    
Create empty database for the application (e.g. demo_login ):

    sudo -u postgresql psql

    CREATE DATABASE dev;


## Settings

Edit Django settings file according to the requirements

## Migrate Database
    ./manage.py makemigrations

    ./manage.py migrate

## Run Management command for create defualt permissions


## Load base data

Load fixtures:


## Install Apache Web Server
    sudo apt-get update && sudo apt-get install apache2 

Enable modules:
    sudo a2enmod rewrite

If We need ssl:

    sudo a2enmod ssl

## Install WSGI Dependencies
    sudo apt-get update && sudo apt-get install libapache2-mod-wsgi-py3

> **Note:** More information [here](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/) and [here](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8)

