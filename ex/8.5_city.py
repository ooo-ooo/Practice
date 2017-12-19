#coding=utf-8
def city(name,nation='China'):
    print(name + ' is in the country of ' + nation) 

print u"默认输出"
city('Beijing')

print "输出上海属于的国家"
city("Shanghai")

print u"输出其它国家城市"
city('Newyork','USA')
