print("Question 1")
Countlines = open("Example_15.txt","r")
for i,text in enumerate(Countlines):
    print(i,text)
print("Total number of lines are:",i+1)

Countlines.close()

print("Question 2")
Writelines = open("Example_15(1).txt","w")
Writelines.write("\n1. Steve Jobs is a popular name in the world.")
Writelines.write("\n2. He was the co-founder and chairman of Apple Inc.")
Writelines.write("\n3. He is also referred to as an industrial designer, investor, and media tycoon.")
Writelines.write("\n4. His full name was Steven Paul Jobs.")
Writelines.write("\n5. He was born on 24th February in the year 1955.")
Writelines.close()
print("Please check the changes in the file Example_15(1).txt")

print("Question 3")
Writelines = open("Example_15(1).txt","a")
Writelines.write("\n\n1. Steve Paul Jobs is regarded as a successful American businessman.")
Writelines.write("\n2. He had attained success in different fields.")
Writelines.write("\n3. He had a great contribution to the development of computers and mobiles.")
Writelines.write("\n4. He is stated as the initiator of the personal computer revolution.")
Writelines.write("\n5. He had served as the CEO of Apple Inc from 1997 to 2011.")
Writelines.close()
print("Please check the changes in the file Example_15(1).txt")