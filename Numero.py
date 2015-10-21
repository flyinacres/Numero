__author__ = 'rfischer'

N = int(raw_input())
A = [int(x) for x in raw_input().split(' ')]
M = int(raw_input())
B = [int(x) for x in raw_input().split(' ')]

A.sort()
B.sort()

#print A
#print B
#print str(len(A))
x = 0
last_miss = -1 # Caution this is not a good sentry value!!!!
for y in range (0, len(B)):
    #print "x: " + str(x) + ", y: " + str(y)
    #print "last_miss: " + str(last_miss) + ", B[y]: " + str(B[y]) + ", A[x]: " + str(A[x])

    # if this value is the same as one already noted, just increment y
    if last_miss != B[y]:
        if x >= len(A):
          if y >= x:
            print B[y],
            last_miss = B[y]
        elif A[x] != B[y]:
          print B[y],
          last_miss = B[y]
        elif x < len(A):
             x += 1

print

#print "x: " + str(x) + ", y: " + str(y)
#print "last_miss: " + str(last_miss) + ", B[y]: " + str(B[y]) + ", A[x]: " + str(A[x])
