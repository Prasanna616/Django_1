#Python official runtime image 
FROM python:3.7.16-slim-bullseye

#Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

#Set the working directory to /app
WORKDIR /app

#copy the requirement file into current directory
COPY requirement1.txt .

#Install needed packages specified in requirement
RUN pip install -r requirement1.txt

#Copy current working directory contents into the conatiner at /app
COPY . /app/

RUN apt-get update && apt-get install -y

#Run the Django migrations
RUN python manage.py migrate

#Expose port 8000 to outside world
EXPOSE 8000

#start the django development server
CMD ["python","manage.py","runserver","0.0.0.0:8000"]