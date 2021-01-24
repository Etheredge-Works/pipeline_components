FROM python:3.7
COPY ./src /pipelines/component/src
WORKDIR /pipelines/component/src
ENTRYPOINT ["python", "split_train_test.py"]