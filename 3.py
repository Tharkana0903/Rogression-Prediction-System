# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1903065

# Date: 8/4/2022
#creating variables---
count=0
progress_list=[]
trailer_list=[]
retriever_list=[]
excluded_list=[]
progress_count=0
trail_count=0
retriever_count=0
exclude_count=0
user="y"
status_1=0
status_2=0
status_3=0
status_4=0

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
                progress_list.append(str(credit) + "," + str(defer) + "," + str(fail))
                progress_count+=1
                status_1="Progress :"

            elif credit==100 and (defer ==20 or fail==20):
                print("progresss(module trailer)")
                trailer_list.append(str(credit) + "," + str(defer) + "," + str(fail))
                trail_count+=1
                status_2="progresss(module trailer) :"
               

            elif fail<80:
                print("Module retriever")
                retriever_list.append(str(credit) + "," + str(defer) + "," + str(fail))
                retriever_count+=1
                status_3="Module retriever :"
                

            elif fail>=80:            
                print("Exclude")
                excluded_list.append(str(credit) + "," + str(defer) + "," + str(fail))
                exclude_count+=1
                status_4="Exclude :"
              
        else:
            print("out of range")
       
    except ValueError:
        print("Integer required")
    count+=1
    print("\n") 
    user=input("Would you like to enter another set of data?\nEnter 'Y' for yes or 'q' to quit and view results: ")
    print("\n")
    
def print_list(no,list_name,status):
    "This function display all stored data"
    for x in range(no):
        print(status,list_name[x])
    
#Display output---
print("------------------------------------------------------------------------------------")

print_list(progress_count,progress_list,status_1)
print_list(trail_count,trailer_list,status_2)
print_list(retriever_count,retriever_list,status_3)
print_list(exclude_count,excluded_list,status_4)

"\n"
print(count,"outcomes in total.")
print("------------------------------------------------------------------------------------")
