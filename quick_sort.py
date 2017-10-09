a=[9,17,1,12,4,8,5,19,3,1]

#print(len(a))
i, j =0, 9
def parition(i,j,a):
    #if i==j:return
    while(j>i):
        while(j>i and a[j]>a[i]):
            j-=1
        t=a[i]
        a[i]=a[j]
        a[j]=t


        while (j > i and a[j] > a[i]):
            i+= 1
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return i

def quick_sort(i,j,a):
    if i==j:
        return
    index = parition(i,j,a)
    print(index)
    #print(index)
    quick_sort(i,index-1,a)
    quick_sort(index+1,j,a)

quick_sort(i,j,a)

print(a)