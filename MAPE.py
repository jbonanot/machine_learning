## Jacob Bonanotte
## ECE 8487 Advanced Machine Learning
## This program is an executable to compute the MAPE (Mean Absolute Percentage Error)

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
        diff = abs((price-model)/price)
        ySum = ySum + diff
        avg = (100/n) * ySum   
        i -= 1
        countInModel += 1
    count = 1 + count
    print("The MAPE of model "+str(count)+" is "+str(avg)+"%.")
    j -= 1