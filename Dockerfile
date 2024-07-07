FROM python:3.12

ARG VERSION

COPY dist/glowprom-$VERSION.tar.gz /

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

RUN . "$HOME/.cargo/env" && pip install /glowprom-$VERSION.tar.gz

ENTRYPOINT ["glowprom"]
CMD []
