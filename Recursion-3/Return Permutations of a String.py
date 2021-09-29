
def stringPermutation(string):
    #base case:
    if len(string)==1:
        return [string[0]]
    op=[]
    for i in range(0,len(string)):
        
        smallString=[ele for ele in string]
        smallString.pop(i)
        smallString=''.join(smallString)
        firstLetter=string[i]
        smallPermutation=stringPermutation(smallString)
        for k in smallPermutation:
            op.append(firstLetter+k)
        
    return op

#main
string=input()
result=stringPermutation(string)
for i in result:
    print(i)
