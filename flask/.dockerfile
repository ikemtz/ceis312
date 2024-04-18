FROM bitnami/python:3.12
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install tensorflow &&\
    pip install pandas && \
    pip install flask
COPY . /app
ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000" ]