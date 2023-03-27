# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1903065

# Date: 7/4/2022

#creating variables---
count=0
progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0
user="y"

#while loop and process---
while user!="q":    
    try:
        credit=int(input("Pleace enter your credits at pass :"))
        defer=int(input("Pleace enter your credits at defer :"))
        fail=int(input("Pleace enter your credits at fail :"))

        if credit <=120 and defer<=120 and fail<=120:
            if credit+defer+fail !=120:
                print("Total incorrect")
              
            elif credit==120:
                print("Progress")
                progress_count+=1

            elif credit==100 and (defer ==20 or fail==20):
                trailer_count+=1
                print("progresss(module trailer)")

            elif fail<80:
                retriever_count+=1
                print("Module retriever")

            elif fail>=80:
                excluded_count+=1
                print("Exclude")
                
        else:
            print("out of range")
       
    except ValueError:
        print("Integer required")
    count+=1
    print("\n") 
    user=input("Would you like to enter another set of data?\nEnter 'Y' for yes or 'q' to quit and view results: ")
    print("\n")

def histogram(no):
    ""
    for x in range(no):
        print("*")
print("------------------------------------------------------------------------------------")
print("Horizontal Hostogram ")
header=["Progres" , "Trailer" , "Retriever" , "Excluded"]
print(" ".join(header))
for x in range(max(progress_count,trailer_count,retriever_count,excluded_count)):#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops#:~:text=You%20can%20use,Improve%20this%20answer
    print("{0}        {1}        {2}         {3}". format(
        '*' if x < progress_count else ' ',
        '*' if x < trailer_count else ' ',
        '*' if x < retriever_count else ' ',
        '*' if x < excluded_count else ' '
        ))


print(count,"outcomes in total.")
print("------------------------------------------------------------------------------------")
