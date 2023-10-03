FROM python:3.12

ARG VERSION

RUN pip install glowprom==$VERSION

ENTRYPOINT ["glowprom"]
CMD []
