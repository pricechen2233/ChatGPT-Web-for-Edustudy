# 使用GPT API创建的ChatGPT聊天页面，更换接口可以兼容其他大语言模型，主要用于教学科研
## 基于ChatGPT-Web项目进一步开发，源项目地址(https://github.com/LiangYang666/ChatGPT-Web)  
### 本项目适用于教学研究，学生可以基于大语言模型进行学习，对话内容将会存储在pkl文件中
### 本项目遵守源项目开源协议，仅用于学习

## 部署方法
### 1. 安装python3.9+
### 2.执行 pip install -r requirements.txt安装必要包
### 3.如使用OpenAI接口，请打开data/config.yaml文件，配置HTTPS_PROXY和OPENAI_API_KEY，相关细节已在配置文件中描述，如果在境外部署则无需代理，将HTTPS_PROXY行删除即可；同时如本地环境变量中有OPENAI_API_KEY，则也无需配置config文件，项目会优先读取环境变量中的OPENAI_API_KEY。对其他大语言模型接口的支持仍在开发中……
### 4.执行gunicorn main:app -c gunicorn.py启动项目，项目会运行在本地的8080端口，但此时项目不会暴露在局域网网，仅能本地使用，如需局域网访问，需要开启系统防火墙权限并修改配置为bind='0.0.0.0:8080'，此时可以在局域网访问"IP:8080"网址浏览本站
### 5.(本步骤可选，需要在服务器预先安装最新版nginx)使用nginx反向代理，阅读nginx.txt，修改nginx.conf文件，重启nginx，项目将会在公网（局域网）被nginx服务器代理运行，访问端口默认为443
### 6.gunicorn代理服务停止方式，Ubuntu系统下执行：bash stop_gunicorn.sh
### 7.本项目使用pkl数据格式记录用户数据，用户数据记录在data/all_user_dict_v3.pkl文件，数据经过加密无法直接读取。如需读取请调整并运行read_data.py文件读取pkl文件。