# API Python FastAPI with MySQL

Run MySQL local (phpMyadmin), create database

```
sr_dps
```

Setup env (if error happen, let search and install virtualenv for python)

```
virtualenv venv
```

For Linux/Mac

```
source venv/bin/activate
```

For Windows

```
source venv/Scripts/activate
```

Install package

```
pip install fastapi pymongo uvicorn sqlalchemy python-dotenv pymysql bs4 openai newspaper3k
```

Start server

```
uvicorn index:app --reload (uvicorn index:app --host 0.0.0.0 --port 82)
```

View SwaggerUI

```
http://127.0.0.1:8000/docs
```

# © Copyright by Double N
