FROM python:3.11

ARG VERSION

COPY dist/glowprom-$VERSION.tar.gz /

RUN pip install /glowprom-$VERSION.tar.gz --extra-index-url https://www.piwheels.org/simple

ENTRYPOINT ["glowprom"]
CMD []
