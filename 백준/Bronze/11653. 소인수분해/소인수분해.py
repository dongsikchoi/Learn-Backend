num=int(input())
div = 2 
while div <= num: 
    if num % div == 0: 
        print(div)
        num = int(num / div)
    else:
        div +=1 