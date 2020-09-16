FROM python:3.7.3-stretch

RUN useradd --create-home fibo
WORKDIR /home/fibo
USER fibo

ARG CI_COMMIT_SHA
ENV CI_COMMIT_SHA=${CI_COMMIT_SHA}
ADD ${CI_COMMIT_SHA}.tgz /home/fibo

ENTRYPOINT [ "python", "./app.py" ]
