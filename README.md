# Project Information

## Version: 0.1
Date: 2024/11/18 

## Feature
- 通过Python脚本来调用C++可执行文件，以达到核心任务原子化、部署实现便捷化的目的；
- 任务进度通知：1、将各个任务的执行情况通过落盘日志记录；2、通过邮件来知会总体执行情况。
- 设置任务在ubuntu启动的时候就默认运行一次，以任务进一步自动化；

## Usage Instruction
指定需要执行的可执行文件的位置

### Linux自启动
有多种方式来实现Linux启动之后运行指定任务，例如使用rc.local。
这里介绍的方法是使用Systemd服务。Systemd 是现代 Linux 系统中管理服务的标准工具，可以创建一个服务来启动脚本。
创建一个服务文件：
编辑文件 `/etc/systemd/system/main.service`：
```Bash
sudo nano /etc/systemd/system/main.service
```
添加以下内容：
```Bash
[Unit]
Description=Run main.py at startup
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/main.py
Restart=always
User=your-username
WorkingDirectory=/path/to/

[Install]
WantedBy=multi-user.target
```
替换 `/path/to/main.py` 为脚本的实际路径。
替换 `your-username` 为实际用户名。

xio 注意这里`Restart=always`的影响，将在该服务退出（无论正常退出还是异常退出）之后重新拉起该服务。针对需要类似daemon等需要一直运行的服务建议配置成always，若只是开机阶段运行一次则需要配置成no或者no-failure
上面`WantedBy=multi-user.target`指定了该服务属于`multi-user.target`的一部分，当系统进入`multi-user.target`时，该服务会自动运行。
常见target如下

启用并启动服务：
```Bash
sudo systemctl daemon-reload
sudo systemctl enable main.service
sudo systemctl start main.service
```
```Bash
验证服务是否正常运行：
sudo systemctl status main.service
```

## Feature Planning
1、通过微信小程序来知会总体进度和运行情况；
2、邮件内容进一步完善，包括运行的结果、时间、占用的平均资源、峰值资源。
