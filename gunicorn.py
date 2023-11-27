import os
import multiprocessing

# 预加载资源
# preload_app = True
# 设置守护进程
daemon=True
# 监听内网端口8080
bind='127.0.0.1:8080'
# 设置进程文件目录
pidfile='./gunicorn.pid'
chdir='./' # 工作目录
# 工作模式--协程
worker_class = "gevent"
# 并行工作进程数 核心数*2+1个
workers=1 #multiprocessing.cpu_count()*2+1
# 指定每个工作者的线程数
threads=2 #multiprocessing.cpu_count()*2
# 等待队列最大长度,超过这个长度的链接将被拒绝连接
backlog = 2048
# 设置最大并发量
worker_connections = 2000
loglevel='debug' # 错误日志的日志级别
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 设置访问日志和错误信息日志路径
log_dir = "./log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
accesslog = "./log/gunicorn_access.log"
errorlog = "./log/gunicorn_error.log"