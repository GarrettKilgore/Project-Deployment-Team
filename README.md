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




Aaron's Instructions

---To deploy this app on a k8s cluster  (with dns and ingress enabled):
1.  Clone git repo
2. In the root of the new directory:
kubectl apply -f frontend.yaml -f backend.yaml -f ingress.yaml
3.  Webapp should be up and accessible on any of the cluster's node's IP addresses.

---The k8s yaml files will pull the images from my own dockerhub repo's.  
aaronstaheli/client-app:latest
aaronstaheli/backend-app:latest


---If you would like to make any changes to the app at this point, this is what you would need to do:
1. Make your changes to the code
2. In the directory of the image you want to build (this uses the Dockerfile, inspect that if you would like to know what it does):
docker build -t yourname/imagename:latest ./
3. Assuming your cli is logged into dockerhub:
docker push yourname/imagename:latest
4. Edit both the frontend and backend yaml files to reflect your dockerhub repository names you chose.
