#coding=utf-8
def make_shirt(size='L',text='I love Python'):
    print("Tshirt size is " + size +" Content "+text) 

print u"默认输出"
make_shirt()

print "输出默认字样的中号"
make_shirt(size='M')

print u"输出其它字样"
make_shirt(text='I love my family')
