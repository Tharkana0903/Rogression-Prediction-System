# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1903065

# Date: 4/4/2022
count=0
progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0
user="y"

value=int(input("part 1--1\npart 2--2\nType your choice :"))

def histogram_value():
    global user,progress_count,retriever_count,excluded_count,count,trailer_count
    while user!="q":    
        try:
            credit=int(input("Pleace enter your credits at pass :"))
            defer=int(input("Pleace enter your credits at defer :"))
            fail=int(input("Pleace enter your credits at fail :"))
            if credit in range(0,121,20) and defer in range(0,121,20) and fail in range(0,121,20):

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
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
        count+=1
        print("\n") 
        user=input("Would you like to enter another set of data?\nEnter 'Y' for yes or 'q' to quit and view results: ")
        print("\n")
    histogram()

def value_check():
    def integer(mark):
        try:
            answer=int(mark)
            sign="true"
            return sign
        except:
            print("Integer requied")


    def range_find(user):
        if user not in ('0','20','40','60','80','100','120'):
            print("Out of range")
        else:
            output="true"
            return output 
    #--------------------------------------------------------------------

    while True:
        pass_mark=input("Pleace enter your credits at pass :")
        if integer(pass_mark)=="true" and range_find(pass_mark)=="true":
            break
        
    while True:
        Defer_mark=input("Pleace enter your credits at defer :")
        if integer(Defer_mark)=="true" and range_find(Defer_mark)=="true":
            break
        
    while True:
        Fail_mark=input("Pleace enter your credits at fail :")
        if integer(Fail_mark)=="true" and range_find(Fail_mark)=="true":
            break

    pass_mark=int(pass_mark)
    Defer_mark=int(Defer_mark)
    Fail_mark=int(Fail_mark)
    #--------------------------------------------------------------------
    if pass_mark == 120: 
        print("Progress")
        
    elif pass_mark == 100:
        print("Progress(module trail)")


    elif pass_mark == 80 or pass_mark==60:
        print("Do not progress-module retrieve")
        
        
    elif pass_mark==40:
        if Defer_mark==0:
            print("Exclude")
        else:
            print("Do not progress-module retrieve")
            
    elif pass_mark==20:
        
        if Defer_mark==0 or Defer_mark==20:
            print("Exclude")
        else:
            print("Do not progress-module retrieve")
    elif pass_mark==0:
        if Defer_mark==40 or Defer_mark==20 or Defer_mark==0:
            print("Exclude")
        else:
            print("Do not progress-module retrieve")
    
def histogram():
    global user,progress_count,retriever_count,excluded_count,count

    print("---------------------------------------------------------------------------------------")
    print("\nHorizontal Histogram"
          "\nProgress", progress_count, " : ", progress_count * "*",
          "\nTrailer", trailer_count, " : ", trailer_count * "*",
          "\nRetriever", retriever_count, " : ", retriever_count * "*",
          "\nExcluded", excluded_count, " : ", excluded_count * "*",
          "\n",progress_count + trailer_count + retriever_count + excluded_count, "outcomes in total")
if value==1:
    value_check()
elif value==2:
    histogram_value()
else:
    print("Invalied user input")
    
    
