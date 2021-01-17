import re

'''
符号
literal     匹配文本字符串的字面值                     literal foo
re1|re2     匹配正则表达式 re1 或者 re2                foo|bar
.           匹配任何字符（除了\n 之外）                 b.b

^           匹配字符串起始部分                         ^Dear
$           匹配字符串终止部分                        /bin/*sh$

*           匹配 0 次或者多次前面出现的正则表达式        [A-Za-z0-9]*
+           匹配 1 次或者多次前面出现的正则表达式        [a-z]+\.com
?           匹配 0 次或者 1 次前面出现的正则表达式      goo?
{N}         匹配 N 次前面出现的正则表达式              [0-9]{3}
{M,N}       匹配 M～N 次前面出现的正则表达式            [0-9]{5,9}

[…]         匹配来自字符集的任意单一字符                  [aeiou]
[..x−y..]   匹配 x～y 范围中的任意单一字符               [0-9], [A-Za-z]
[^…]        不匹配此字符集中出现的任何一个字符，包括某一范围的字符（ 如果在此字符集中出现） [^aeiou], [^A-Za-z0-9]
(*|+|?|{})? 用于匹配上面频繁出现/重复出现符号的非贪婪版本（ *、 +、 ?、 {}） .*?[a-z]
(…)         匹配封闭的正则表达式，然后另存为子组 ([0-9]{3})?,f(oo|u)bar

特殊字符
\d 匹配任何十进制数字，与[0-9]一致（ \D 与\d 相反，不匹配任何非数值型的数字） data\d+.txt
\w 匹配任何字母数字字符，与[A-Za-z0-9_]相同（ \W 与之相反）               [A-Za-z_]\w+
\s 匹配任何空格字符，与[\n\t\r\v\f]相同（ \S 与之相反）                   of\sthe
\b 匹配任何单词边界（ \B 与之相反）                                     \bThe\b
\ N 匹配已保存的子组 N（ 参见上面的(…))                                  price: \16
\c 逐字匹配任何特殊字符 c（ 即，仅按照字面意义匹配，不匹配特殊含义）           \., \\, \*
\A(\Z) 匹配字符串的起始（结束）（另见上面介绍的^和$）                       \ADear

扩展表示法
(?iLmsux) 在正则表达式中嵌入一个或者多个特殊“标记” 参数（或者通过函数/方法） （?x），（？im）
(?:…) 表示一个匹配不用保存的分组                                       (?:\w+\.)*
(?P<name>…) 像一个仅由 name 标识而不是数字 ID 标识的正则分组匹配          (?P<data>)
(?P=name) 在同一字符串中匹配由(?P<name>)分组的之前文本                    (?P=data)
(?#…) 表示注释，所有内容都被忽略                                       (?#comment)
(?=…) 匹配条件是如果…出现在之后的位置，而不使用输入字符串；称作正向前视断言    (?=.com)
(?!…) 匹配条件是如果…不出现在之后的位置，而不使用输入字符串；称作负向前视断言   (?!.net)
(?<=…) 匹配条件是如果…出现在之前的位置，而不使用输入字符串；称作正向后视断言   (?<=800-)
(?<!…) 匹配条件是如果…不出现在之前的位置，而不使用输入字符串；称作负向后视断言  (?<!192\.168\.)
(?(id/name)Y|N) 如果分组所提供的 id 或者 name（名称）存在，就返回正则表达式的条件匹配 Y，如
                 果不存在，就返回 N； |N 是可选项                      (?(1)y|x)
'''

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   1.match & search                       #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# match(pattern， string， flags=0)
# search(pattern， string， flags=0)
# pattern: 正则表达式
# string: 目标字符串
# flags: 模块属性
'''
常用的模块属性
re.I、 re.IGNORECASE 不区分大小写的匹配
re.L、 re.LOCALE 根据所使用的本地语言环境通过\w、 \W、 \b、 \B、 \s、 \S 实现匹配
re.M、 re.MULTILINE ^和$分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个字符串本身的起始和结尾
re.S、 rer.DOTALL “.” （点号）通常匹配除了\n（换行符）之外的所有单个字符；该标记表示“.” （点号）能够匹配全部字符
re.X、 re.VERBOSE 通过反斜线转义， 否则所有空格加上#（以及在该行中所有后续文字）都被忽略，除非在一个字符类中或者允许注释并且提高可读性
'''

m = re.match('foo', 'gfoosssfoo')
# match 从开头匹配
if m is not None: print('match: ', m.group())  # None

m = re.search('foo', 'gfoosssfoo')
# search 从任意部位匹配
if m is not None: print('search: ', m.group())  # ==>search:  foo

# 匹配多个字符串--> re1|re2
m = re.match('(foo|goo)', 'foosssfoo')
if m is not None: print(m.group())  # ==>foo
m = re.match('foo|goo', 'goosssfoo')
if m is not None: print(m.group())  # ==>goo

# 匹配任何单个字符--> .
m = re.match('.end', 'aendsss')
if m is not None: print(m.group())  # ==>aend
m = re.match('.end', 'endsss')
if m is not None: print(m.group())  # None
m = re.match('.end', '\nendsss')
if m is not None: print(m.group())  # None

# 创建字符集--> [ ]
m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None: print(m.group())  # ==>c3po

# 分组
m = re.match('([cr][23])([dp][o2])', 'c3po')
if m is not None: print(m.group())  # ==>c3po
if m is not None: print(m.group(1))  # ==>c3
if m is not None: print(m.group(2))  # ==>po
if m is not None: print(m.groups())  # ==>('c3', 'po')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   2.findall & finditer                   #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表
# findall(pattern， string [, flags] )

# 与 findall()函数相同，但返回的不是一个列表，而是一个迭代器。 对于每一次匹配，迭代器都返回一个匹配对象
# finditer(pattern， string [, flags] )

l = re.findall('car', 'carry the barcardi to the car')
print(l)  # ==>['car', 'car', 'car']

l = re.findall('c(a)(r)', 'carry the barcardi to the car')
print(l)  # ==>[('a', 'r'), ('a', 'r'), ('a', 'r')]

it = re.finditer('car', 'carry the barcardi to the car')
for i in it:
    print(i.group())
# ==>car
# ==>car
# ==>car


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   3.sub & subn                           #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# sub(pattern， repl， string， count=0)
# repl: 一个函数
# count: 最大替换次数

print(re.sub('X', 'Mr.Smith', 'X\n\nDear X,\n'))
# ==>Mr.Smith
# ==>
# ==>Dear Mr.Smith,
# ==>

# 多返回一个参数，表示替换的个数
print(re.subn('X', 'Mr.Smith', 'X\n\nDear X,\n'))
# ==>('Mr.Smith\n\nDear Mr.Smith,\n', 2)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   4.split                                #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# split(pattern， string， max=0)

print(re.split(r'\s\s+|\t', 'hsernos  tty1         2019-04-28 20:27 (:0)'))
# ==>['hsernos', 'tty1', '2019-04-28 20:27 (:0)']


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                   5.扩展符号                               #
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# (?iLmsux)  在正则表达式中嵌入一个或者多个特殊“标记” 参数
print(re.findall(r'(?i)yes', 'yes? Yes. YES!!'))  # ==>['yes', 'Yes', 'YES']
# 等同于
print(re.findall(r'yes', 'yes? Yes. YES!!', re.I))  # ==>['yes', 'Yes', 'YES']


# (?:…)  表示一个匹配不用保存的分组
print(re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com'))
# ==>['google.com', 'google.com', 'google.com']

# 对比
print(re.findall(r'http://(\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com'))
# ==>[('', 'google.com'), ('www.', 'google.com'), ('code.', 'google.com')]


# (?P<name>…) 像一个仅由 name 标识而不是数字 ID 标识的正则分组匹配

print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212').groupdict())
# ==>{'areacode': '800', 'prefix': '555'}

print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212'))
# ==>(800) 555-xxxx


# (?P=name) 在同一字符串中匹配由(?P<name>)分组的之前文本
print(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number)',
               '(800) 555-1212 800-555-1212').group())
# ==>(800) 555-1212 800-555-1212


# (?=…) 匹配…表达式 返回前面
print(re.findall(r'\w(?=\d)', 'zhoujy20130628hangzhou'))
# ==>['y', '2', '0', '1', '3', '0', '6', '2']
print(re.findall(r'[A-Za-z]+(?=\d)', 'zhoujy20130628hangzhou432'))
# ==> ['zhoujy', 'hangzhou']

# (?!…) 不匹配…表达式 返回前面
print(re.findall(r'[A-Za-z]+(?!\d)', 'zhoujy20130628hangzhou432'))
# ==>['zhouj', 'hangzho']

# (?<=…) 匹配…表达式 返回后面
print(re.findall(r'(?<=\d)[A-Za-z]+', 'zhoujy20130628hangzhou432'))
# ==>['hangzhou']

# (?<!…) 不匹配…表达式 返回后面 (ps:字符串以^开头)
print(re.findall(r'(?<!\d)[A-Za-z]+', 'zhoujy20130628hangzhou432'))
# ==>['zhoujy', 'angzhou']

# (?(id/name)Y|N) 如果分组所提供的 id 或者 name（名称）存在，就返回正则表达式的条件匹配 Y，如果不存在，就返回 N； |N 是可选项
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))  # ==>True
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))  # ==>False

