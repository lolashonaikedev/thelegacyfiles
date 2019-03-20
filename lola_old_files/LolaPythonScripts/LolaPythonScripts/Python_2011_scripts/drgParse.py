import cx_Oracle
import csv
import os


con= cx_Oracle.connect('ex','ex','xe')
answer=True
while answer==True:
 #Set Up Options for Clients to Use in Web Application and parse the integer
 print "Welcome to the Consumer Complaints Application (CCA). Please select from one of the Options below to be analyzed"
 print "Option 22: View The Top 20 Highest Number of Complaints by Company Name and Financial Product"
 print "Option 22: View The Top 20 Highest Number of Complaints by State and Financial Product"
 print "Option 33: View Some of the Companies who had a Green Climate ( Excellent Positive Handling Consumer Complaint Response)"
 print "Option 44: View Some of the Companies who had a Yellow Climate (Decent Positive Handling Consumer Client Response)"
 print "Option 55: View Some of the Companies who had a Red Climate (Negative Handling Response"
 choice= int(input("Enter Choice Number here:"))
 if choice == 11:
  cur11= con.cursor()
  outfile11=open("companyHigh.xlsx","w")
  output11=csv.writer(outfile11, dialect='excel')
  cur11.execute('select  company_name, financial_product, count(issue) from consumer_complaint group by company_name, financial_product, issue order by count(issue) desc') 
  for i in range (20):
   for row in cur11:
    print row
    output11.writerow(row)
    break
 elif choice ==22:
  cur22= con.cursor()
  outfile22=open("stateHigh.csv","w")
  output=csv.writer(outfile22, dialect='excel')
  cur22.execute('select  state, financial_product, count(issue) from consumer_complaint group by state, financial_product, issue order by count(issue) desc')
  for i in range (20):
   for row in cur22:
    print row
    output22.writerow(row)
    break
 elif choice ==33:
  cur33= con.cursor()
  outfile33=open("greenClimate.csv","w")
  output33=csv.writer(outfile33, dialect='excel')
  cur33.execute('select distinct company_name from consumer_complaint where company_response like \'%Closed%\'and timely_response = \'Yes\' and consumer_disputed = \'No\' and rownum <20')
  for row in cur33:
   for i in range(20):
    print row
    output33.writerow(row)
    break
 elif choice ==44:
  cur44= con.cursor()
  outfile44=open("yellowClimate.csv","w")
  output44=csv.writer(outfile44, dialect='excel')
  cur44.execute('select distinct company_name from consumer_complaint where company_response like \'%In%\'and timely_response = \'Yes\' and consumer_disputed = \'No\' and rownum <20')
  for row in cur44:
   for i in range(20):
    print row
    output44.writerow(row)
    break
 elif choice==55:
  cur55= con.cursor()
  outfile55=open("redClimate.csv","w")
  output55=csv.writer(outfile55, dialect='excel')
  cur55.execute('select distinct company_name from consumer_complaint where timely_response = \'No\' and consumer_disputed = \'No\' and rownum <20')
  for row in cur55:
   for i in range(20):
    print row
    output55.writerow(row)
    break
 else:
  print "Wrong Choice. Please Try Again"
  answer=str(input("Would you like to retry using the application (yes or no)?:"))
  if answer=="yes":
    continue
  elif answer=="no":
    print "Thank you for using the Consumer Client Application"
    answer=False
  else:
    print "Error, continuing"
    continue
    
  

con.close()
