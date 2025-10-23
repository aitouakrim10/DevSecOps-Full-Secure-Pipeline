FROM python:3.11-slim

# RUN useradd --create-home appuser
# i set working directory
WORKDIR /app
COPY app/ .
# i install dependencies
RUN pip install --no-cache-dir -r requirement.txt
# Now I execute the application
EXPOSE 5000 8000


CMD ["python", "app.py"]


# to build the docker image run : docker build -t app-test .

