import pandas as pd
from SendingEmail import sendMail
from StudentDatBase import df

allStudentsNAme = []
for name in df["Name"]:
    allStudentsNAme.append(name)
#print(allStudentsNAme)

data = pd.read_csv(r"D:\face reognition\Attendance.csv")
presentStudents = []
absentStudents = []
absentStudents_index = []
for nm in data["Name"]:
    presentStudents.append(nm)

for index,nm in enumerate(allStudentsNAme):
    if nm not in presentStudents:
        absentStudents.append(nm)
        absentStudents_index.append(index)
#print(absentStudents)
#print(absentStudents_index)
receiverMail_list = []
for id in absentStudents_index:
    receiverMail_list.append(df["Mail_Id"][id])

#print(receiverMail_list)

# sending mail to all absent student , by importing our own module SendingEmail.py which is having a method sendMail(receiver_mail)
for receiver_mail in receiverMail_list:
    sendMail(receiver_mail)

print("Mail sent successfully to all absent student")
