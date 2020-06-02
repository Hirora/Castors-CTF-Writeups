import codecs

encoded = ["63617374","6f72734354","467b723178","54795f","6d316e","757433735f6774","5f73317874795f6d","316e757433","737d"]


string = ""

for i in encoded:
    string = string + codecs.decode(codecs.decode(i,"hex"),"utf-8")
    
print(string)
