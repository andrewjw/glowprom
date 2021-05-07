FROM python:3.9

ARG VERSION

RUN pip install glowprom==$VERSION

ENTRYPOINT ["glowprom"]
CMD []
