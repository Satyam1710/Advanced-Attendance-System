import pandas as pd
 
# data of all the student.
data = {'Name':['BILLGATES','JACKMA','SATYAM.JPG', 'ELONMUSK'],
        'Age':[20, 21, 19, 18],
        'Roll_No':[101,102,103,104],
        'Mail_Id':["billgates@gmail.com","jackma@gmail.com","satyam171001@gmail.com","elonmusk@gmail.com"],
        'WhatsApp':[9876543210, 8976543210,6201558743,7896543210]}
 
# Create DataFrame
df = pd.DataFrame(data)
#print(df)