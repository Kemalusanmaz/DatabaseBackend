# Base Image
FROM python:latest

ADD mainLVDB.py .

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY conf.py .
COPY databaseClass.py .
COPY influxDbClass.py .
COPY TCPServerClass.py .
COPY mainLVDB.py .
# RUN  python mainLVDB.py 

EXPOSE 9898

# Command to run the application
# CMD [ "/bin/bash" ]

CMD [ "python", "mainLVDB.py" ]