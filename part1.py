from sympy import substitution


def Levenstein_distance(a,b):
    #defining the rows and cols for 2d matrix which is equal to the length of a and b
    (m,n)= (len(a) , len(b))
 
    #initilizing the array named lev with size equal to (n+1)x (m+1)
    lev = [[0 for x in range(n+1)] for y in range(m+1)]
    
    #populating the row from 1 to m+1 
    for i in range(1, m + 1):
        lev[i][0]= i
       
    #populating the col from 1 to n+1
    for j in range(1, n + 1):
        lev[0][j]= j
      
    #implementing the checks in order to calculate levenstein distance
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            #check
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
                
            #levenstein defination for calculating cost 
            left = lev[i][j-1]
            left_up = lev[i-1][j-1]
            top = lev[i-1][j]
            lev[i][j] = min((left + 1) , (top + 1), (left_up + cost))
            l_dist = lev[i][j]
            #calculating insertions,deletions and subsitutions
            insertions = abs(m - n)
            subsitutions = l_dist - insertions
            deletions = (left_up - left - 1)
            if deletions < 0:
                deletions = 0 
     
    #printing the 2d matrix to show cost at every point 
    for r in range(n):
        print(lev[r])
           
    #returning the levenstein distance which is the last cost in matrix        
    return l_dist,insertions,deletions,subsitutions
 
#main code that calls levenstein distance method
a = input('Enter First String: ')
b = input('Enter Second string: ')
dist,ins,dels,subs =Levenstein_distance(a,b)

print('levenstein distance between "',a, '" and "' ,b,'" is = ' ,dist )
print('insertions: ',ins)
print('deletions: ',dels)
print('subsitutions: ',subs)