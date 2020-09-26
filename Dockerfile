FROM python:3.8

ARG VERSION

RUN pip install glowprom==$VERSION

ENTRYPOINT ["glowprom"]
CMD []
