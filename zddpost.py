import requests,json
 
url = 'http://www.xj.com/api/Pmcreport/pythonCheck'
data = {'company_id':1,'member_id':16}
r =requests.post(url,data)
print(r)
print(r.text)
print(r.content)