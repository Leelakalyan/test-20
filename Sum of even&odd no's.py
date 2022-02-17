#sum of even numbers and odd numbers
n=int(input('enter number:'))
sum=0
sum2=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print('even sum is:',sum)
for i in range(1,n+1):
    if i%2==1:
        sum2=sum2+i
print('odd sum is:',sum2)

Output:
enter number:
10
even sum is: 30
odd sum is: 25
