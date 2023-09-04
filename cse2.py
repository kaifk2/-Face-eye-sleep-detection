def func1():
    print("I am a funtion")


def func2(agr1, arg2):
    print(agr1,"",arg2)


def cube(x):
    return x*x*x

def power(num,x=1):
    result = 1;
    for i in range(x):
        result = result * num 
    return  result

def multi_add(*args):
    result = 0
    for x in args:
        result =result + x
    return result




def main():
    x,y =10,100

    if x < y:
         result= "X IS less than y"


    else:
        result= "x is great than y" 


print(result)





func2 (10,20)
print(func2(10,20))
print(cube(3))


print(power(2))
print(power(2,3))
print(power(x=3, num=2))

print(multi_add(4,5,6,7))




