from ipwhois import IPWhois
import json

ip = '223.243.20.237'
obj = IPWhois(ip)
res = obj.lookup_rdap(depth=1)
print(json.dumps(res, indent=4))
