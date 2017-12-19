#coding:utf-8
#让实参变可选参数，放最后，if 判定.
def make_album(singername,albumname,num=''):
    if num:
        album={'Singer':singername,'Album':albumname,'Number':num}

    else:
        album={'Singer':singername,'Album':albumname}
    return album 


A=make_album('MayDay','WenRou','10')
print A

B=make_album('WangFeng','BeijingBeijing')
print B
