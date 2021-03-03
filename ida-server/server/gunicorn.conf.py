workers = 5    # 同时开启的处理请求的进程数量
worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:80"