FROM python:3.9
WORKDIR /usr/src/app
ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0

# Install the requirements in a cache-friendly way
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Download the ML model in a cache-friendly way too
COPY ./Ml_model.py ./Ml_model.py
RUN python Ml_model.py

COPY *  ./

EXPOSE 5000
CMD ["flask","run"]