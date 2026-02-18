#If function to check the status of a number
def numCheck(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negitive"
    else:
        return "Zero"

#Check prime function
def primeCheck(num):

    #set return bool
    isPrime = True

    #Check that it is large enough
    if num > 1:

        #Check for all possible factors
        for i in range(2,num):

            #if factor is found
            if num % i == 0:
                isPrime = False
                break
    
    return isPrime

#Main section
#Show the number checker
negNum = -1
zeroNum = 0
posNum = 1
print(negNum, "is ", numCheck(negNum))
print(zeroNum, "is ", numCheck(zeroNum))
print(posNum, "is ", numCheck(posNum))

#Prime number checker
primeList = []
counter = 2
while (len(primeList) < 10):
    isPrime = primeCheck(counter)
    if isPrime == True:
        primeList.append(counter)
    counter += 1
print(primeList)

#total from 0 to 100
whileCounter = 0
total = 0
while(whileCounter < 101):
    total += whileCounter
    whileCounter += 1
print(total)