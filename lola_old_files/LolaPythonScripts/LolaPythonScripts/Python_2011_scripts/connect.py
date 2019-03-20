import cx_Oracle

con=cx_Oracle.connect('om','om','xe')
cur=con.cursor()

login=input("Please enter your user name: ")
password=input("Please enter your password: ")
print con.version
con.close()
