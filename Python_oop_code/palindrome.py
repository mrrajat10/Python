def palin():
    list1 = [1, 3, 3, 6, 3, 1]
    copy_list = list1.copy()
    copy_list.reverse()
    if (copy_list == list1):
        return print("It is a palindrome")
    else:
        return print("It is not a palindrome!!")


palin()
