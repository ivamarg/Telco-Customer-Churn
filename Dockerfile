# using the base image with python 3.7
FROM amd64/python:3.7-slim

# set working directory as app
WORKDIR /app

# copy files
COPY . .

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# run the application
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]