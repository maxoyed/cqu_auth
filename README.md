# cqu_jwc
重庆大学统一认证模块

## 安装

```commandline
pip install cqu-auth
```

或者
```commandline

sudo pip install cqu-auth
```

## 使用

```python
from cqu_auth import cquauth
res = cquauth('学号', '密码')
```

认证成功返回`True`，失败返回`False`。


