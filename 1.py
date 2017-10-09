while(True):
    try:
        array = map(int,raw_input().strip().split())
        array=sorted(array)
        for i in array:
            print i
    except:
        break