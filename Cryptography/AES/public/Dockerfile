FROM python:3.10.4

RUN useradd -m ctf

RUN apt-get update && apt-get install -y \
    python3 \
    socat

WORKDIR /home/ctf

COPY ./* ./

USER ctf

RUN pip install --no-cache-dir pycryptodome
CMD ["socat", "TCP-L:13630,reuseaddr,fork", "EXEC:python3 /home/ctf/chall.py,stderr"]