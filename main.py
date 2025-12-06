#enter a medical cause
medical_cause = input("Did the student have a medical issue that prevented them from taking the exam?")
#condition 1
if medical_cause.lower() == "yes":
    print("The student is excused from taking the exam due to medical reasons.")

else:
    exam_score=int(input("Enter the student's score"))
    #condition 2
    if exam_score >= 500:
        print("The student is allowed to move to the next grade")
    else:
        print("The student is not allowed to move to the next grade due to low performance and no medical cause.")