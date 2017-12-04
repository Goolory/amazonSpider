# print(b'\28014;\29983;\20845;\35760;(\20840;\26032;\31934;\35793;\26412;)'.decode("utf-8"))
# import re
# from html.parser import HTMLParser
# from book import Book
# # print(hex(28014))
#
# # print(chr(28014))
#
# # print(b'\28014;\29983;\20845;\35760;')
#
# str = "&#28014;&#29983;&#20845;&#35760;(&#20840;&#26032;&#31934;&#35793;&#26412;)"
#
# #print(str)
#
# def de_code(str):
#     rstr = re.compile(r'\d+')
#     result = rstr.findall(str)
#     print(result)
#     for i in result:
#         print(chr(int(i)))
#
# # de_code(str)
# s = '&#28014;&#29983;&#20845;&#35760;(&#20840;&#26032;&#31934;&#35793;&#26412;)'
# t = '你好)'
# # print(s.decode('utf8')+"\n")
# # print(t.encode('utf8'))
# print(HTMLParser().unescape(s))
#
# book = Book()
# book.name = s
# print(book.name)

import time
print(int(time.time()))