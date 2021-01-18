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
### 2、如何获取企查查的cookie
![Image text](https://raw.githubusercontent.com/HUANGZHENJIE2/qcc_web_api/main/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20210118233422.png)
### 3、调用API
```
qcc.search_mind("阿里巴巴")
```
out[0]\n
{'list': [{'KeyNo': '8c9f7ddc1a7bcee3d1f7676773fe9404', 'QccCode': '65CTZ8D', 'Name': '<em>阿里</em><em>巴巴</em>（中国）有限公司', 'OperName': '张勇', 'ImageUrl': 'https://co-image.qichacha.com/CompanyImage/8c9f7ddc1a7bcee3d1f7676773fe9404.jpg?x-oss-process=style/qcc_cmp', 'IsAuth': False, 'AuthLevel': -1, 'IsHide': False, 'Reason': '名称匹配'}, {'KeyNo': 'c70a55cb048c8e4db7bca357a2c113e0', 'QccCode': '80RA8T0', 'Name': '<em>阿里</em><em>巴巴</em>（中国）网络技术有限公司', 'OperName': '戴珊', 'ImageUrl': 'https://co-image.qichacha.com/CompanyImage/c70a55cb048c8e4db7bca357a2c113e0.jpg?x-oss-process=style/qcc_cmp', 'IsAuth': False, 'AuthLevel': -1, 'IsHide': False, 'Reason': '名称匹配'}, {'KeyNo': 'h7a5a6c405fca1754b9ef13a6a174600', 'QccCode': '435XAKG', 'Name': '<em>阿里巴巴</em>集團控股有限公司', 'OperName': '张勇', 'ImageUrl': 'https://co-image.qichacha.com/CompanyImage/h7a5a6c405fca1754b9ef13a6a174600.jpg?x-oss-process=style/qcc_cmp', 'IsAuth': False, 'AuthLevel': -1, 'IsHide': False, 'Reason': '名称匹配'}, {'KeyNo': 'eaed3b907f21bd7842a29ed411a8ac76', 'QccCode': '60CMWR2', 'Name': '浙江<em>阿里</em><em>巴巴</em>机器人有限公司', 'OperName': '陈丽娟', 'ImageUrl': 'https://co-image.qichacha.com/CompanyImage/eaed3b907f21bd7842a29ed411a8ac76.jpg?x-oss-process=style/qcc_cmp', 'IsAuth': False, 'AuthLevel': -1, 'IsHide': False, 'Reason': '名称匹配'}, {'KeyNo': 'b0fa3d310df2c236415d638d18da195c', 'QccCode': '723J8LC', 'Name': '<em>阿里</em><em>巴巴</em>华南技术有限公司', 'OperName': '童文红', 'ImageUrl': 'https://co-image.qichacha.com/CompanyImage/b0fa3d310df2c236415d638d18da195c.jpg?x-oss-process=style/qcc_cmp', 'IsAuth': False, 'AuthLevel': -1, 'IsHide': False, 'Reason': '名称匹配'}], 'personCount': 6}



