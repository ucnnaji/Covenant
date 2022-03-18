import mysql.connector #library to facilitate connection to the dataset(Malaria)

import time #library to enable access to the database one at a time

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="demo"
)

mycursor = mydb.cursor()

ind_Urban=[]
ind_Rural=[]

ind_Adult=[]
ind_Child=[]

ind_Mosquito_Yes=[]
ind_Mosquito_No=[]

ind_Mosquito_Yes=[]
ind_Mosquito_No=[]

ind_Education_High=[]
ind_Education_Average=[]
ind_Education_Low=[]


mycursor.execute("SELECT * FROM malaria WHERE Residence_Type='Urban'") #query the dataset to fetch all records with value "Urban"

Residence_Type_Urban = mycursor.fetchall()



for x in Residence_Type_Urban:
  ind_Urban.append(x[0])

time.sleep(0.1)

mycursor.execute("SELECT * FROM malaria WHERE Residence_Type='Rural'") #running two execute function will raise an error

Residence_Type_Rural = mycursor.fetchall()


for y in Residence_Type_Rural:
  ind_Rural.append(y[0])


print("Indiscernibility relation for Residence_Type partition")
Res=(ind_Urban,ind_Rural)
print(Res,'\n')




#print(Res[0][0],"\n")#dddddd

time.sleep(0.8) # Use a function for the for loop


mycursor.execute("SELECT * FROM malaria WHERE Age='Adult'") 

Age_Adult=mycursor.fetchall()

for a in Age_Adult:
  ind_Adult.append(a[0])


time.sleep(0.3)


mycursor.execute("SELECT * FROM malaria WHERE Age='Child'") 

Age_Child=mycursor.fetchall()


for a in Age_Child:
  ind_Child.append(a[0])
 
Age=(ind_Adult,ind_Child)
print("Indiscernibility relation for Age partition")
print(Age,"\n")



time.sleep(0.3)

mycursor.execute("SELECT * FROM malaria WHERE Mosquito_Net='Yes'") 

Mosquito_Yes=mycursor.fetchall()

for m in Mosquito_Yes:
  ind_Mosquito_Yes.append(a[0])




time.sleep(0.3)

mycursor.execute("SELECT * FROM malaria WHERE Mosquito_Net='No'") 

Mosquito_No=mycursor.fetchall()

for m in Age_Child:
  ind_Mosquito_No.append(a[0])

Mosquito=(ind_Mosquito_Yes,ind_Mosquito_No)
print("Indiscernibility relation for Mosquito Net partition")
print(Mosquito,"\n")



time.sleep(0.3)

mycursor.execute("SELECT * FROM malaria WHERE Education_of_Household='High'") 

Education_High=mycursor.fetchall()

for e in Education_High:
  ind_Education_High.append(a[0])




time.sleep(0.3)

mycursor.execute("SELECT * FROM malaria WHERE Education_of_Household='Average'") 

Education_Average=mycursor.fetchall()

for m in Education_Average:
  ind_Education_Average.append(a[0])



time.sleep(0.3)

mycursor.execute("SELECT * FROM malaria WHERE Education_of_Household='Low'") 

Education_Low=mycursor.fetchall()

for m in Education_Low:
  ind_Education_Low.append(a[0])

Education1=(ind_Education_High,ind_Education_Average,ind_Education_Low)
print("Indiscernibility relation for Education of the house-hold partition")
print(Education1,"\n")




  
  

