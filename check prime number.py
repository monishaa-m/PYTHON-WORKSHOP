n1=int(input("enter any number:"))
counter=0;
if n1>1:
    for i in range(2,int(n1/2)+1):        
        if(n1%i)==0:
            counter=counter+1;
if(counter>0):
    print("Not Prime")
else:
    print("Its prime")
          
