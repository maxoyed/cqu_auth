def verify(username, password):
    import requests
    from lxml import etree
    s = requests.session()
    res = s.get("http://authserver.cqu.edu.cn/authserver/login?service=http://i.cqu.edu.cn/ehome/index.do")
    html = etree.HTML(res.content)
    lt = html.xpath("//input[@name='lt']/@value")[0]
    dllt = html.xpath("//input[@name='dllt']/@value")[0]
    execution = html.xpath("//input[@name='execution']/@value")[0]
    _eventId = html.xpath("//input[@name='_eventId']/@value")[0]
    rmShown = html.xpath("//input[@name='rmShown']/@value")[0]
    payload = {
        "username": username,
        "password": password,
        "lt": lt,
        "dllt": dllt,
        "execution": execution,
        "_eventId": _eventId,
        "rmShown": rmShown,
    }
    res = s.post("http://authserver.cqu.edu.cn/authserver/login?service=http://i.cqu.edu.cn/ehome/index.do", data=payload)
    html = etree.HTML(res.content)
    mc_left = html.xpath("//div[@class='mc-left']//text()")
    kick_table = html.xpath("//table[@class='kick_table']//text()")
    if mc_left or kick_table:
        return True
    else:
        return False
