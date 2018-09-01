import sys

# ++++++++++++++++++
# 1.python3编码
# ++++++++++++++++++


# 默认编码
print(sys.getdefaultencoding())  # ==>utf-8


# str.encode(编码)，将Unicode转化成相应编码
s = u"中文"
print(s)  # ==>中文
print(s.encode('utf8'))  # ==>b'\xe4\xb8\xad\xe6\x96\x87'
print(s.encode('gbk'))  # ==>b'\xd6\xd0\xce\xc4'


# str.decode(编码)，将相应编码转化成Unicode
print(b"\xe4\xb8\xad\xe6\x96\x87".decode('utf8'))  # ==>中文
print(b"\xd6\xd0\xce\xc4".decode('gbk'))  # ==>中文


