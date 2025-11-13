# Project-Deployment-Team
SE-3200 Group project

# Movie Review App

A simple web application for managing movie reviews.

---

## Resource

**Resource Name:** Movie Review

**Attributes:**

- `name` (string)
- `movie` (string)
- `genre` (string)
- `rating` (float)
- `review` (string)

---

## Schema

```sql
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    name TEXT,
    movie TEXT,
    genre TEXT,
    rating FLOAT,
    review TEXT
);
```
## REST API Endpoints

| Name      | Method  | Path              |
|-----------|---------|-------------------|
| List the movie reviews      | GET     | `/movies`         |
| Retrieve the movie reviews   | GET     | `/movies/<id>`    |
| Create the movie reviews      | POST    | `/movies`         |
| Replace the movie reviews     | PUT     | `/movies/<id>`    |
| Delete the movie reviews      | DELETE  | `/movies/<id>`    |
| Preflight the movie reviews   | OPTIONS | `/movies/<id>`    |
