FROM tensorflow/tensorflow:2.4.0
RUN pip install click
COPY ./src /pipelines/component/src
WORKDIR /pipelines/component/src
ENTRYPOINT ["python", "main.py"]