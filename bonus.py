


def RemoveZeros(num):
    i = int(num)
    if i % 10 == 0 :
         return RemoveZeros(i//10)
    else:
        return str(i)[::-1]
    


num = input("Please inter the required number :")
print("After removing zeros & reversing the number:" ,RemoveZeros(num))


        

