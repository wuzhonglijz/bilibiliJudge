import requests as r

caseurl='http://api.bilibili.com/x/credit/jury/caseInfo'

def GetCase(cid):
    headers={
    'Host': 'api.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.0 Safari/537.36 Edg/92.0.874.0'
    }
    params={'cid': cid}
    info=r.get(caseurl,params=params,headers=headers)
    return info
