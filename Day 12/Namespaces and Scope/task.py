sum1=4+9  #global variable
def sum():   #global scope function
     def my_funct():# local scope function
        sum2=2+4  # local variable

        return  sum1+sum2


     print(my_funct())
sum()
