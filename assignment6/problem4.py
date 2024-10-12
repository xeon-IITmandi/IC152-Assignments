def prefRevCapStr(s):
    if len(s)==0:
        return s
    else:
        return  (s[-1] + prefRevCapStr(s[:-1])).upper()
    


print((prefRevCapStr("Diwali-to-come")),"-> Holi-to-come")




