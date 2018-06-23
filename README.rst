cquauth
=======

重庆大学统一认证模块

安装
----

.. code:: bash

    pip install cquauth

或者

.. code:: bash

    sudo pip install cquauth

使用
----

.. code:: python

    from cquauth import verify
    res = verify('统一认证号', '统一认证密码')

认证成功返回\ ``True``\ ，失败返回\ ``False``\ 。
