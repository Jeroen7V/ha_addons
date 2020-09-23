FROM python:alpine

LABEL maintainer="Jeroen Vermeylen <jeroen@vermeylen.org>"

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install --no-cache-dir uvicorn \
    && apk del .build-deps gcc libc-dev make
EXPOSE 8000

RUN pip install --no-cache-dir requests pydantic fastapi

WORKDIR /src
COPY ./src /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]