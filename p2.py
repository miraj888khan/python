# def my(*args):
#     for i in args:
#         print(args[1])



# my("hi","miraj")
# def my1(*numbers):
#     for i in numbers:
#         print(numbers)



# my("hi","miraj")
# my1(1,2,3,4)


# # maxmium
# def maximum(*numbers):
#     max_number =0
#     max_number= numbers[0]
#     for num in numbers:
#         if num>max_number:
#             max_number=num
#         else:
#             continue
#     print(max_number)        

# maximum(1,2,3,4,5,3,9)
def my_function(srgu,*args,**Kwargs):
    print("argument",srgu)
    print(args)
    print("kwargs",Kwargs)
    print("age",Kwargs["age"])


my_function("this","email,phoneno",city="islamabad")    
# def my_function(username, **details):
#   print("Username:", username)
#   print("Additional details:")
#   for key, value in details.items():
#     print(" ", key + ":", value)

# my_function("emil123", city = "Oslo", hobby = "coding")
