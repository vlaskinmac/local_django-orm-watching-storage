# Generates tables.

**The code generates tables by employees of storage.**


This script is written as part of the task of the courses [Devman](https://dvmn.org).


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Python Version

Python 3.6 and later.

### Installing

To install the software, you need to install the dependency packages from the file: **requirements.txt**.

Perform the command:

```

pip3 install -r requirements.txt

```

## Environment variables

Request access to the database from an employee.

- `ALLOWED_HOSTS` - list of allowed hosts
- `SECRET_KEY` - secret key of the your site
- `DATABASES` - accepts the parameter: `DATABASE_URL`
- `DATABASE_URL` - declared in the config file with parameters specified your db in format: 
`DATABASE_URL=postgres://user:password@host:port/dbname`


## Launch code


```python
$  python manage.py runserver 0.0.0.0:8000
```

- Open the link http://0.0.0.0:8000 / in the browser



## Authors

**vlaskinmac**  - [GitHub-vlaskinmac](https://github.com/vlaskinmac/)
