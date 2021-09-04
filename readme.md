# Menucracy
A menu voting system for office

# Project Setup Guideline
Please follow the following guideline to set up this application

## System Requirements
* `Python Version >= 3.8`
* `PostgreSQL Version == 12.8 or Equivalent`

## Manual Virtualenv Setup Process
* **OS == LINUX**
  * `mkdir venvs`
  * `pip3 install virtualenv --user`
  * `virtualenv -p python3 venvs/venv`
  * `source venvs/venv/bin/activate`
* **OS == WINDOWS**
  * `mkdir \venvs`
  * `pip install virtualenv`
  * `virtualenv \venvs\venv`
  * `\venvs\venv\Scripts\activate`
Or, just use PyCharm Professional version 

## Create database and user
  * `sudo -u postgres psql`
  * `CREATE USER menu;`
  * `ALTER USER menu WITH SUPERUSER;`
  * `ALTER USER menu WITH PASSWORD 'menu';`
  * `CREATE DATABASE menucracy;`

## Project Setup
* `git clone https://github.com/MohiuddinSumon/menucracy.git`
* `cd mynews`
* `pip install -r requirements.txt`
* `python3 manage.py migrate`
* `python3 manage.py createsuperuser`

