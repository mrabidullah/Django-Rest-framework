# Django REST Framework API Project

## Overview

This project is a simple REST API built using Django and Django REST Framework.  
It provides CRUD (Create, Read, Update, Delete) operations with image upload support and authentication protection.

This project is created for learning and practicing backend development using Django REST Framework.

---

## Features

- Create new records (name, age, image)
- Retrieve all records
- Update full record using PUT
- Partial update using PATCH
- Delete records
- Image upload support
- Authentication protected endpoints

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite Database
- Pillow (for image handling)

---

## Project Structure

api/
 ├── models.py
 ├── serializers.py
 ├── views.py
 ├── urls.py
 └── migrations/

resframwork/
 ├── settings.py
 ├── urls.py
 ├── wsgi.py
 └── asgi.py

products/
 └── images/

manage.py

---

## Model

class Details(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

---

## API Endpoints

Method   | Endpoint            | Description
-------- | ------------------- | ----------------
GET      | /api/details/       | Get all records
POST     | /api/create/        | Create new record
PUT      | /api/update/<id>/   | Full update
PATCH    | /api/patch/<id>/    | Partial update
DELETE   | /api/delete/<id>/   | Delete record

---

## Authentication

All APIs are protected using:

IsAuthenticated

You must be logged in or provide valid credentials to access APIs.

---

## Example POST Request

{
  "name": "khan",
  "age": 24
}

For image upload use form-data:

image: file.jpg

---

## Example Response

{
  "message": "Data created successfully",
  "id": 1,
  "name": "khan",
  "age": 24,
  "image": "/media/images/file.jpg",
  "created_at": "2026-05-09T10:00:00Z"
}

---

## Setup Instructions

1. Clone project
git clone https://github.com/mrabidullah/Django-Rest-framework.git

2. Go to project folder
cd Django-Rest-framework

3. Install requirements
pip install -r requirements.txt

4. Run migrations
python manage.py makemigrations
python manage.py migrate

5. Run server
python manage.py runserver

---

## Requirements

Django
djangorestframework
Pillow

---

## Notes

- Images are stored in media/images/
- Default database is SQLite
- Tested using Postman
- Image upload must use form-data

---

## Author

GitHub: https://github.com/mrabidullah  
Project: Django REST Framework API Learning Project
