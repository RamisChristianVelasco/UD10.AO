x = input("Intro la paraula: ")
sum_a=0
sum_m=0
sum_altres=0
for c in x:
    if (c=="a" or c=="A"):
        sum_a=sum_a+1
    elif (c=="m" or c=="M"):
        sum_m=sum_m+1
    else:
        sum_altres=sum_altres+1
print("La paraula '{}' té {}'as, {}'ms i {} d'altres caràcters".format(x, str(sum_a), str(sum_m), str(sum_altres)))





