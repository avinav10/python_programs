###reverse string

string= "avinav"

s = len(string)


empty_string=""


for i in range(s-1,-1,-1):
    empty_string = empty_string + string[i]
print(empty_string)

##########################for each

print("#####################")

string1 = "manoj"

collect = ""

for i in string1:
    collect =  i + collect

print(collect)



