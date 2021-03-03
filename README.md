# IDA-docker
Use Docker to apply IDA Pro (7.5) and Python3 for automated malware analysis.

## Image

* username: `idauser`
* password: `pwmd`
* OS: `Ubuntu 20.04`

## Build

### ida-base

* 根据自身条件，自行编写`install.sh`安装`IDA Pro`

### ida-server

* `From ida-base`
* 修改需要自动化自行的IDAPython脚本`script.py`

## Run

`$ sudo docker run -d --rm --name ida -p 7777:80 ida-server`
