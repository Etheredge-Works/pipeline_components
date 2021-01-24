FROM alpine:latest
COPY ./src /pipelines/component/src
WORKDIR /pipelines/component/
ENTRYPOINT ["sh", "src/join.sh"]
