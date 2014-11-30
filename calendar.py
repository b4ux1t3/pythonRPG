scores = []

run = True

average = 0
# Do
while run:
    scores.append(input("Give me a number: "))
    
    stop = input("Type stop to stop or enter to keep going")
    if stop == "stop":
        run = False
        
for i in scores:
    average += i
    
average /= len(scores)

print "The average is %s" % (average)
