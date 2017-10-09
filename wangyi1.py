import sys
import collections
if __name__ == '__main__':
    while(True):
        try:
            num = int(sys.stdin.readline().strip())
            for _ in range(num):
                data = map(int, raw_input().strip().split())
                n, k = data[0], data[1]
                nums = map(int, raw_input().strip().split())
                while(k>0):
                    k-=1
                    left = nums[:n ]
                    right = nums[n:]
                    nums = []
                    t=n

                    while t:
                        nums.append(right[t-1])
                        nums.append(left[t-1])
                        t-=1
                    nums = nums[::-1]
                for i in nums:
                    print i,
                print


        except:
            break