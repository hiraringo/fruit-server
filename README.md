# What's this
- lang: Python, framework: FastAPI, DB: PostgresSQL 
- Easy way to make local env
- For server-side developers
- YOU NEED DOCKER on your PC

# How to Use
1. Confirm "docker" and "docker-compose" command are avairable
2. Move to directory "/fruit-server" on your local PC terminal
3. RUN docker-compose up
```
$ docker-compose up -d --build
```
4. access localhost in browser (Google Chrome etc..)
```
$ localhost:8000
```
5. try GET, POST, PUT, DELETE Request
6. to finish, RUN docker-compose down
```
$ docker-compose down
```

# About logic
request > FastAPI > main.py > db.py > PostgreSQL > db.py > fruit.py > encoder.py > main.py > FastAPI > response