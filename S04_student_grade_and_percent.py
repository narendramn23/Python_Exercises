def total_percent(english, maths, science):

    maximum_marks = 80 + 90 + 100

    actual_marks_scored = english + science + maths

    total = (actual_marks_scored / maximum_marks) * 100

    return total


def student_marks():
   english = int(input("Enter marks scored in English total is 80: "))
   maths = int(input("Enter Marks scored in science total is 90: "))
   science = int(input("Enter Marks scored in maths total is 100: "))
   actual_marks_scored = english + science + maths
   marks = total_percent(english, maths, science)
   print ("You scored", actual_marks_scored, "out of 270")

   if marks >= 90:
       print("you scored", marks,"%","First Calss")
   elif marks >= 75:
        print("you scored", marks,"%","second class")
   elif marks <= 35:
        print("you scored", marks,"%", "Failed")
   else:
        print("you scored", marks,"%", "Average")
        

if __name__ == "__main__":

    print("this is main function:", __name__)
    student_marks()

        

   
    
    
