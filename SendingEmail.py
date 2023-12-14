import smtplib, ssl
import pandas as pd
from StudentDatBase import df
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 587  
smtp_server = "smtp.gmail.com"
sender_email = "pandatxyz@gmail.com"
password = "wudd kcew uivu zesh"

# message = """\
# Subject: Hi there

# This message is sent from Satyam's Attendace system project for being absent ."""

message = MIMEMultipart("alternative")
message["Subject"] = "Absent from Today's Class"
message["From"] = sender_email


# Create the plain-text and HTML version of your message
text = """\
Hello,
This mail has been sent from XYZ School office 
to you due to your absence from todays class.
follow the below form and give the valid reason 
for your absence.
And ensure to be present in next upcoming classes
as exams are very near.

XYZ School authorities
"""
html = """\
<html>
  <body>
    <p> <h3> mail sent by XYZ School </h3> </p>
    <p>Hello,<br>
      This mail has been sent from XYZ School office 
      to you due to your absence from todays class.
      follow the below form and give the valid reason 
      for your absence.
      And ensure to be present in next upcoming classes
      as exams are very near.<br>
    </p>
 <h1>Form TO Be Filled</h1>
    <i><h3>Kindly fill this form </h3></i> <br>
    <FORM action="mailto:simon.long@cit.ie" method="post" enctype="text/plain">
      First Name : <INPUT type="text" name="firstname" placeholder="Enter name here">
      Last Name : <INPUT type="text" name="secondname"  placeholder="Enter surname here">
      <BR>
      <BR>
      <!--It's important that both of these radio button have the same name so they behave as one component (i.e. Only one can be selected at a time)-->  
      <INPUT type="radio" name="gender" value="male">Male<BR>
      <INPUT type="radio" name="gender" value="female">Female  
      <BR>
      <BR>
      <!--This uses the new HTML "email" INPUT type which will automatically validates the email address when the SUBMIT button is clicked-->
      email: <INPUT type="email" name="mail" placeholder="e-mail address">
      <BR>
      <BR>
        Class:  <SELECT name="Class">
          <OPTION value="Eighth">Eighth</OPTION>
          <OPTION value="Ninth">Ninth</OPTION>
          <OPTION value="Tenth">Tenth</OPTION>
          <OPTION value="Eleventh">Eleventh</OPTION>
          <OPTION value="Twelfth">Twelfth</OPTION>
        </SELECT>
        <BR>
        <BR>
      Roll number: <INPUT Type="text" name="Roll Number:" placeholder="Enter your Roll no.">
        <BR>
        <strong>Describe Reason for your absence :</strong> <BR>        
        <TEXTAREA rows="6" cols="50" name="commentfield"></TEXTAREA>
        <BR>

        <BR>
        <INPUT TYPE="submit" value="Send my reason">
        <INPUT TYPE="reset" value="Reset">
    </FORM>


  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

server = smtplib.SMTP(smtp_server,port)
# server.connect('smtp.gmail.com','587')
# server.ehlo()
server.starttls()
server.login(sender_email,password)

def sendMail(receiver_mail):
    try:
        server.sendmail(sender_email,receiver_mail,message.as_string())
    except Exception as e:
        print("Something went wrong and that issue is ..,",e)
    


students_present_data = pd.read_csv(r"D:\face reognition\Attendance.csv")
students_present = list(students_present_data["Name"])

absent_student_index = []
absent_student_name = []
absent_student_email = []
for index,name in enumerate(df.Name):
    if name not in students_present:
        absent_student_index.append(index)
        absent_student_name.append(name)
        absent_student_email.append(df.Mail_Id[index])
# print(absent_student_email)
for index,receiver_mail in enumerate(absent_student_email):
    # message['To'] = absent_student_name[index] 
    sendMail(receiver_mail)

print("Mail sent successfully to all absent student")
