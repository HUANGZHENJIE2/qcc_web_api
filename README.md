![Image text](https://raw.githubusercontent.com/HUANGZHENJIE2/qcc_web_api/main/logo4.png)
# qcc_web_api
## Introduction - 介绍
这是一个通过模拟企查查网页请求来调用企查查网页api Python 包，只需简单的配置即可使用企查查的api。使用前需要注册个企查查账户。有部分功能还是需要企查查会员。[传送门](https://www.qcc.com/)
## Requirements - 必要条件
```
Python =< 3.9.0
企查查账户一枚
部分功能可能需要企查查会员
```

## Quick start - 快速开始
### 1、将qcc.py复制到你的项目中，并导入QccWebApi
```
from qcc import QccWebApi
qcc = qcc = QccWebApi("[您的企查查cookie]")
```
### 2、安装依赖
```
pip install requests
```
### 3、如何获取企查查的cookie
![Image text](https://raw.githubusercontent.com/HUANGZHENJIE2/qcc_web_api/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20210118233422.png)
### 4、调用API
```
qcc.search_mind("阿里巴巴")
```



