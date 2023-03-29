# def main (**kwargs):
#     print(kwargs)
#     for k,w in kwargs.items():
#         print(k,w)
#     return kwargs

# print(main(name='Olzhas', age = '20', i = 123, a = 123.123, b ={'name': 'Alima'}))

# rekursiya 
# def rec():
#     return rec()
# rec() 

# def rec_num(number: int): 
#     if number ==0:
#         return 1  #for stop rekursiys
#     return number * rec_num(number -1)
# # #10*9*8*7*6*5*4*3*2*1*0 -> 1 
# # print(rec_num(5))
# num = int(input('Input number: '))
# factorial = rec_num(5)
# print("factorial number", num, 'equal', factorial) 

def max_find_num(lists: list,n):
    # n = len(lists)

    if n ==0:
        return 'Sumashedshiy'
    
    if n == 1:
        return lists[0]
    
    return max(lists[n-1],max_find_num(lists,n-1))

arr = [1,2,3]
n = len(arr)
print(max_find_num(arr,n))

    