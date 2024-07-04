FROM python:3.12

ARG VERSION

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh && rustup toolchain install -y stable

RUN pip install glowprom==$VERSION

ENTRYPOINT ["glowprom"]
CMD []
