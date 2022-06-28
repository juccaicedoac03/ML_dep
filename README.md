# ML_dep 
A deployed machine learning REST API using Django and Docker.
Python 3

## For development

1. Clone this repo.

    ```
    git clone https://github.com/juccaicedoac03/ML_dep.git
    ```

2. Create a virtual environment in **ML_dep** folder and install **requirements.txt**.

    ```
    mkdir mldep_env
    python -m venv mldep_env
    source ml_env/bin/activate
    pip install requirements.txt
    ```
3. Make API model migrations.

    ```
    cd Project_MLdep
    python manage.py migrate
    ```
4. Run server.

    ```
    python manage.py runserver
    ```

    And in our browser (or in postman), make a request GET a http://127.0.0.1:8000/api/test

## For deployment

You can create or donwload a Docker image:

### Creating a Docker image

Once our project is inside a github repository, and Docker is installed, We will create a directory in to make our Dockerfile.

```
mkdir MLdep_docker
cd MLdep_docker
```

We create a **Dockerfile** and write the steps for creating the image that contains everything we need.

```
  # syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN git clone https://github.com/juccaicedoac03/ML_dep
WORKDIR "ML_dep/"
RUN pip install gdown
RUN pip install -U git+https://github.com/juccaicedoac03/ML_dep.git >/dev/null
RUN pip install -r requirements.txt
WORKDIR "Project_MLdep/"
RUN gdown 1lWfMIZLNehFV65AgeJK_UjSToylPFiBi # Google drive link of ML model
RUN python manage.py migrate 
```

Also, we create a **docker-compose.yml** file with:

```
version: "3.9"
   
services:    
  web:
    build: .
    command:  python manage.py runserver 0.0.0.0:8000
    container_name: ML_dep_container
    ports:
      - "8000:8000"
```

Finally run compose

```
docker-compose up  
```

### Or using a predefined Docker image

```
docker pull juccaicedoac/mldep_docker_web:latest
docker-compose up  
```

# REST API

The ML REST API methods are described below.
HOST: http://0.0.0.0:8000/

## List of items

### Request

`GET`

```
/api/Orders/ 
```

### Success Reponse

```
{
  "message": "Success",
  "orders": [
    {
      "order_id": 15031281,
      "store_id": 900006856,
      "to_user_distance": 1.298663,
      "to_user_elevation": -19.70105,
      "total_earning": 5500,
      "created_at": "2017-09-19T15:36:49Z",
      "taken": false
    },
    {
      "order_id": 15213594,
      "store_id": 900011745,
      "to_user_distance": 0.750715,
      "to_user_elevation": -34.016602,
      "total_earning": 5700,
      "created_at": "2017-09-22T21:38:58Z",
      "taken": true
    }
  ]
}
```

### Error Reponse

```
{
  "message": "No orders found",
  
}
```

## Read Item

### Request

`GET`

```
/api/Orders/order_id
```

### URL Params

`order_id=[integer]`

### Success Reponse

```
{
  "message": "Success",
  "orders": [
    {
      "order_id": 15031281,
      "store_id": 900006856,
      "to_user_distance": 1.298663,
      "to_user_elevation": -19.70105,
      "total_earning": 5500,
      "created_at": "2017-09-19T15:36:49Z",
      "taken": false
    },
  ]
}
```

### Error Reponse

```
{
  "message": "No orders found",
}
```

## Make inference

### Request

`POST`

```
/api/Orders/
```

### Request Body: one by one or in bathc

```
{
  "orders": [
    {
      "order_id": 15031281,
      "store_id": 900006856,
      "to_user_distance": 1.298663,
      "to_user_elevation": -19.70105,
      "total_earning": 5500,
      "created_at": "2017-09-19T15:36:49Z",
      "taken": false
    },
    {
      "order_id": 15213594,
      "store_id": 900011745,
      "to_user_distance": 0.750715,
      "to_user_elevation": -34.016602,
      "total_earning": 5700,
      "created_at": "2017-09-22T21:38:58Z",
      "taken": true
    }
  ]
}
```

### Success Reponse

```
{
  "message": "Success",
}
```

### Error Reponse

```
{
  "message": "No orders found",
}
```

## Update Item

### Request

`PUT`

```
/api/Orders/order_id/
```

### URL Params

`order_id=[integer]`

### Request Body:

```
{
  "orders": [
    {
      "order_id": 15031281,
      "store_id": 900006856,
      "to_user_distance": 1.298663,
      "to_user_elevation": -19.70105,
      "total_earning": 5500,
      "created_at": "2017-09-19T15:36:49Z",
      "taken": false
    },
  ]
}
```

### Success Reponse

```
{
  "message": "Success",
}
```

### Error Reponse

```
{
  "message": "No orders found",
}
```

## Delete Item

### Request

`DELETE`

```
/api/Orders/order_id/
```

### URL Params

`order_id=[integer]`

### Success Reponse

```
{
  "message": "Success",
}
```

### Error Reponse

```
{
  "message": "No orders found",
  
}
```
