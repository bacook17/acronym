FROM python:3.11.0-slim-bullseye

RUN pip install --no-cache-dir acronym

ENTRYPOINT [ "acronym" ]
