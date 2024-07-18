FROM python:3.12

ARG VERSION

COPY dist/glowprom-$VERSION.tar.gz /

RUN apt-get update && apt-get install -y rustc

RUN . "$HOME/.cargo/env" && pip install /glowprom-$VERSION.tar.gz

RUN apt-get purge -y rustc && apt-get autoremove -y && apt-get clean

ENTRYPOINT ["glowprom"]
CMD []
