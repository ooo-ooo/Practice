#coding:utf-8


def make_album(singername,albumname,num=''):
    if num:
        album={'Singer':singername,'Album':albumname,'Number':num}

    else:
        album={'Singer':singername,'Album':albumname}
    return album

#quit only when user input ''
while True:
    print("\n Please enter the singer's name:")
    print("enter 'q' if you wanna quit")
    input_name=raw_input("Singer's name is:")
    input_album=raw_input("Album is:")
    if input_name=='q' or input_album=='q':
        print("Exit for you press q")
        break
    #
    #else:
    #     formatted_info = make_album(input_name, input_album)
    #     print formatted_info

    #else可省略，但取消缩进，如下图.

    formatted_info=make_album(input_name,input_album)
    print formatted_info
    
