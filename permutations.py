'''
This file lists all the permutations
'''

def permutations(n, r):
    if (r > n):
        return [["Error"]]
    else:
        thel = list(range(1,n+1))
        templ = []
        for j in thel:
            templ.append([j])
        print(templ)
        while len(templ[0]) < r:
            anotherl = []
            for z in templ:
                for i in thel:
                    if (z.count(i) == 0):
                        tinyl = z[:]
                        tinyl.append(i)
                        anotherl.append(tinyl)
            templ = anotherl
        return templ
        
result = permutations(int(input("Total numbers: ")),int(input("Length of a single group: ")))
for line in result:
    print(line)
print("There are " + str(len(result)) + " permutations.")