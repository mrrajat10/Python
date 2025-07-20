def count_set_bit(n):
  count=0
  while(n):
    count+=(n&1)
    n>>=1
  return count
N=int(input("Enter The No:"))
print(count_set_bit(N))