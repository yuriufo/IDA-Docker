FROM ida-base
LABEL maintainer="yuri"

RUN python3 -m pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    python3 -m pip install --no-cache-dir \
    pexpect \
    networkx \
    flask \
    gunicorn \
    gevent -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /home/idauser/ida-server

COPY . .

WORKDIR /home/idauser/ida-server/server

CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]
