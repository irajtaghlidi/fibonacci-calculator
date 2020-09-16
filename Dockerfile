FROM python:3.7.3-stretch

RUN useradd --create-home fibo
WORKDIR /home/fibo
USER fibo

COPY fibonacci.py .
COPY start.py .
COPY test.py .

ENTRYPOINT [ "python", "./start.py" ]
