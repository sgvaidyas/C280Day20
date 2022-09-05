from DLL_Lib import *
ob = DLL()
while True:
    print("1 INSERT BEGIN")
    print("2 INSERT END")
    print("3 INSERT POS")
    print("4 DELETE BEGIN")
    print("5 DELETE END")
    print("6 DELETE POS")
    print("7 DISPLAY")
    print("8 EXIT")
    ch= int(input("Enter the choice = "))
    if ch==1:
        ele=int(input("Enter ele = "))
        ob.insertBegin(ele)
    if ch==2:
        ele=int(input("Enter ele = "))
        ob.insertEnd(ele)

    if ch==3:
        pos=int(input("Enter pos = "))
        ele=int(input("Enter ele = "))
        ob.insertPos(pos,ele)
    elif ch==4:
        ob.deleteBegin()
    elif ch==5:
        ob.deleteEnd()
    elif ch==6:
        pos=int(input("Enter pos = "))
        ob.deletePos(pos)
    elif ch==7:
        ob.display()
    elif ch==8:
        break
    else:
        print("Invalid choice")


