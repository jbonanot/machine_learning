## Jacob Bonanotte
## ECE 8487 Advanced Machine Learning
## This program is an executable to compute the MAE (Root Mean Squared Error)
import math

countInModel = 1
ySum = 0
avg = 0
i = 0
j = 0
m = int(input("How many models?\nn = "))
j = m
while j > 0:
    n = int(input("How many cases?\n# = "))
    i = n
    count = 1
    while i > 0:
        print("What is the actual value of case "+str(countInModel)+"?")
        price = float(input("Value = "))
        print("What is the prediction of model "+str(count)+", case "+str(countInModel)+"?\n")
        model = float(input("Value = "))
        ##MATH BELOW
        diff = (price-model)**2
        ySum = ySum + diff
        avg = (1/n) * ySum
        avg = math.sqrt(avg)   
        i -= 1
        countInModel += 1
    count = 1 + count
    print("The RMSE of model "+str(count)+" is "+str(avg)+".")
    j -= 1