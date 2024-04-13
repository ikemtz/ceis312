FROM tensorflow/tensorflow:latest
RUN pip install tensorflowjs
RUN pip install TensorRT
COPY ./2x1.keras /models/