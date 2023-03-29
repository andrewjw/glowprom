FROM python:3.11

ARG VERSION

RUN pip install glowprom==$VERSION

ENTRYPOINT ["glowprom"]
CMD []
