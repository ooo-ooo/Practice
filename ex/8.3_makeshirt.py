#coding=utf-8
def make_shirt(size,color):
    print("Tshirt size is " + size +" and color is "+color) 

print u"位置实参调用"
make_shirt('M','Yellow')

print "关键字实参调用"
make_shirt(color='Red',size='L')

