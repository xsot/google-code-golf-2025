# ovs (156 bytes, gold)
p=lambda m,X=8,f=0:[[sum({*e*sum(m,[-f])})for e in r[x:x+X]]for x in range(len(m[0]))for r in m+[[0]*99]if(f:=r[x]*(X*[r[x]]in(r[x:x+X],[f]*X)))]or p(m,X-1)

### mwi (247 (281 unzipped) bytes)
def p(m):
 d,b,*z=sorted(set(a:=sum(m,[])),key=a.count);N,M=len(m),len(m[0])
 for y in range(N):
  for x in range(M):
   Y=y;X=x
   for e in range(M):X+=(m[y]*2)[X]==b<M>X;Y+=Y<N!=(m[Y]*2)[x]==b;z=max(z,[sum(sum(a:=[[d*(e>0)for e in e[x:X]]for e in m[y:Y]],[]))//d,a])
 return z[1]

### xsot (258 (268 unzipped) bytes)
def p(m):
 d,b,*z=sorted(set(a:=sum(m,[])),key=a.count);N,M=len(m),len(m[0])
 for i in range(N*M):
  Y=y=i%N;X=x=i//N
  while(m[y]*2)[X]==b<M>X:X+=1
  while Y<N!=(m[Y]*2)[x]==b:Y+=1;z=max(z,[sum(sum(a:=[[d*(e>0)for e in l[x:X]]for l in m[y:Y]],[]))//d,a])
 return z[1]

########
# NOTE to self: cannot use index as we need to find the next non-box color
def p(m):
    """
    Finds the hollow rectangular box of 2s that contains the most 1s.

    The function iterates through a matrix to identify non-overlapping boxes
    formed by the digit b. For each box, it counts the number of 1s inside
    it and returns the box (as a new matrix) that has the highest count.

    Args:
        matrix: A list of lists of integers (0, 1, or b) representing the matrix.

    Returns:
        A new list of lists representing the box with the most 1s.
        If no boxes are found, or in case of a tie, it returns the first
        box found with the maximum count. Returns an empty list if the
        input matrix is empty or no boxes are present.
    """
    a = sum(m,[])
    d,b,_ = sorted(set(a), key=a.count)

    rows, cols = len(m), len(m[0])
    max_dots = -1

    for r1 in range(rows):
        for c1 in range(cols):
            # Assume this is the top left corner
            # Move along the top and left edges until we reach the bottom right corner
            r2, c2 = r1, c1
            while c2 + 1 < cols and m[r1][c2 + 1] == b:
                c2 += 1
            while r2 + 1 < rows and m[r2 + 1][c1] == b:
                r2 += 1

            # potential answer
            a = [[d*(e>0)for e in m[i][c1:c2+1]]for i in range(r1, r2+1)]

            dots = sum(sum(a,[]))//d

            if dots > max_dots:
                max_dots = dots
                result_box = a

    return result_box

### combined (258 (268 unzipped) bytes)
def p(m):
 d,b,*z=sorted(set(a:=sum(m,[])),key=a.count);N,M=len(m),len(m[0])
 for i in range(N*M):
  Y=y=i%N;X=x=i//N
  while(m[y]*2)[X]==b<M>X:X+=1
  while Y<N!=(m[Y]*2)[x]==b:Y+=1;z=max(z,[sum(sum(a:=[[d*(e>0)for e in l[x:X]]for l in m[y:Y]],[]))//d,a])
 return z[1]
