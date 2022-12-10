f = open("input", "r")
# f = open("test", "r")
max_three=[0,0,0]
current_sum=0

def max(a,b):
    if(a>b):
        return a
    return b


for x in f:
    if(x=="\n"):
        max_three.append(current_sum)
        max_three.sort(reverse=True)
        max_three.pop()
        current_sum=0
        continue
    current_sum+=int(x)

max_three.append(current_sum)
max_three.sort(reverse=True)
max_three.pop()

print(sum(max_three))