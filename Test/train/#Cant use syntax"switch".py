#Cant use syntax"switch". Can use match
num=input("please number: ")
match num:
    case "1":
        print("one")
    case "2":
        print("two")
    case "3":
        print("three")
    case _:
        print("other")