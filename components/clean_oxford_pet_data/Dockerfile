FROM tensorflow/tensorflow:2.3.0
RUN pip install pillow
COPY ./src /pipelines/component/src
ENTRYPOINT ["python", "/pipelines/component/src/convert_images.py"]