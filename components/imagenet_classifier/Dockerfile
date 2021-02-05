FROM tensorflow/tensorflow:latest-gpu
RUN pip install click
COPY ./src /pipelines/component/src
WORKDIR /pipelines/component/src
ENTRYPOINT ["python", "main.py"]