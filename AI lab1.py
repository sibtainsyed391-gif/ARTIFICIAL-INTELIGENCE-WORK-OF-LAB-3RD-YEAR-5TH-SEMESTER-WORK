marks = (65,78,45,89,56,90,34,76,88,54)
print(marks)
total=sum(marks)
print("total marks:",total)

average = total / len(marks)
print("average marks:",average)


count = 0

for m in marks:
  if m >=50:
    count +=1

    print("students scoring 50 or above:",count)

if average>=75:
  print("Excellent performence")

elif average >=60:
  print ("good performence")

else:
  print("need to improve")

message=input ("enter message:").lower()

keywords =["offer","free","winner","urgent"]

spam=False

for word in keywords:
  if word in message:
    spam=True

if spam:
  print("spam message")
else:
  ("normal message")

exam_scores = [75,82,60,90,68]
interview_scores=[65,55,70,80,50]

for i in range(5):

  exam = exam_scores[i]
  interview = interview_scores[i]
 
  if exam >=70 and interview >=60:
    print ("applicant ",i+1,": admitted")

  elif exam >=70 and interview <60 :
    print ("applicant:", i+1, ": waiting list" )

else:
  print("applicant:", i+1 ,": Rejected")


