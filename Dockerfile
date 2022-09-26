# syntax=docker/dockerfile:1
FROM python:3
#set DockerHOME to where your Manage.py is for your Django project
ENV DockerHOME=.
#This creates the directory with the specified path assigned to the DockerHOME variable within the image.
Run mkdir -p $DockerHOME
#This explicitly tells Docker to set the provided directory as the location where the application will reside within the container
WORKDIR $DockerHOME
# set environment variables  
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#This updates the pip version that will be used to install the dependencies for the application
RUN pip install --upgrade pip
#
COPY . $DockerHOME
RUN ls -la MyPantry
#
RUN pip install -r MyPantry/requirements.txt
#
EXPOSE 8000
#
CMD python manage.py runserver

#refrence:
#	https://blog.logrocket.com/dockerizing-django-app/

