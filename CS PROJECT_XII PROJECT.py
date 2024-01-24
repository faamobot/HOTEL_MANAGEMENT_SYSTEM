###Jyothis Central School###
##Class XII  CBSE Computer science project##
##Project done by --> #Fahad
                                   #Vishnupriyan
                                                #Malif
print('\t\t\tLos Pollos Hotel Management System\t\t\t\t')
from tabulate import tabulate
import time
#Establishing connection to mysql
import mysql.connector as msc
mycon=msc.connect(host='localhost',user='root',passwd='123456')

#Checking connection to mysql
if mycon.is_connected():
    print('--->Connected to MySQL successfully')
    print('*'*120)
    
    #creating a database
    cur=mycon.cursor()
    cur.execute('create database if not exists los_pollos')

    #Creating tables
    cur.execute('use los_pollos')
    cur.execute('create table if not exists c_details(Customer_ID integer auto_increment primary key,Name varchar(40),Ph_no varchar(40),E_mail varchar(40),Gender char(1),Check_in Date,Room_no integer)') 
    cur.execute("create table if not exists r_details(Room_no integer primary key,Room_type varchar(40),Rate float,Status varchar(40) default 'vacant')")

     #function to add a room to the database
    def createroom():
        Room_no=int(input('Enter the room_no:'))
        Room_type=input('Enter the room type(Standard/Deluxe/Suite/Executive/Premium):')
        Rate=''
        if Room_type=="Standard":
            Rate=3000
        elif Room_type=='Deluxe':
            Rate=7000
        elif Room_type=='Suite':
            Rate=12000
        elif Room_type=='Executive':
            Rate=20000
        elif Room_type=='Premium':
            Rate=35000
        sql="insert into r_details(Room_no,Room_type,Rate) values({},'{}',{})"
        sqvl=sql.format(Room_no,Room_type,Rate)
        cur.execute(sqvl)
        mycon.commit()
        print('--->Room created successfully')
        print('*'*120)

    #function to edit room details
    def editroom():
        choice=int(input('Enter the room no:'))
        cur.execute('select * from r_details where Room_no={}'.format(choice,))
        data=cur.fetchall()
        if len(data)==0:
            print('Invalid Room no!!')
        else:
            tabulate1=[]
            for i in data:
                tabulate1.append(i)
            headers=['Room no','Room type','Rate','Room status']
            table=tabulate(tabulate1,headers,tablefmt='fancy_grid')
            print(table)
            print('Changing room type...')
            print('''--->To which type would you like to change the selected room to :
        1.Standard --> INR 3,000/night
        2.Deluxe --> INR 7,000/night
        3.Suite -->INR 12,000/night
        4.Executive  -->INR 20,000/night
        5.Premium  -->INR 35,000/night''')
            choice2=int(input('Enter your choice(1/2/3/4/5):'))
            choice3=''
            if choice2==1:
                choice3='Standard'
            elif choice2==2:
                choice3='Deluxe'
            elif choice2==3:
                choice3='Suite'
            elif choice2==4:
                choice3='Executive'
            elif choice2==5:
                choice3='Premium'
            cur.execute("update r_details set Room_type='{}' where Room_no={}".format(choice3,choice))
            print('Room details updated successfully !!')
            print('*'*120)            

    #function to remove rooms
    def removroom():
        while True:            
            room_no=int(input('Enter the room number to be removed:'))
            cur.execute('select * from r_details where Room_no={}'.format(room_no,))
            data=cur.fetchall()
            if len(data)==0:
                print('Invalid Room no!!')
            else:            
                cur.execute('delete from r_details where Room_no={}'.format(room_no,))
                print('Room removed successfully !!')
                break
    #function to show all rooms
    def showallroom():
        cur.execute('Select * from r_details')
        data=cur.fetchall()
        tabulate1=[]
        if len(data)==0:
            print('--->There are no rooms available at the moment :(')
            print('*'*120)
        else:
            for i in data:
                tabulate1.append(i)
            headers=['Room no','Room type','Rate','Room status']
            table=tabulate(tabulate1,headers,tablefmt='fancy_grid')
            print(table)
            print('*'*120)

    #function to show vacant rooms
    def showvacroom():
        cur.execute("Select * from r_details where Status='vacant'")
        data=cur.fetchall()
        if len(data)==0:
            print('--->All rooms are occupied at the moment :(')
            print('*'*120)
        else:
            tabulate1=[]
            for i in data:
                tabulate1.append(i)
            headers=['Room no','Room type','Rate','Room status']
            table=tabulate(tabulate1,headers,tablefmt='fancy_grid')
            print(table)
            print('*'*120)        

    #function to show occupied rooms
    def showoccuproom():
        cur.execute("Select * from r_details where Status='occupied'")
        data=cur.fetchall()
        if len(data)==0:
            print('--->All rooms are vacant at the moment :)')
            print('*'*120)
        else: 
            tabulate1=[]
            for i in data:
                tabulate1.append(i)
            headers=['Room no','Room type','Rate','Room status']
            table=tabulate(tabulate1,headers,tablefmt='fancy_grid')
            print(table)
            print('*'*120)        

    #function to book a room
    rate=''
    def bookroom():
        print('''--->We have the following types of rooms:
    1.Standard --> INR 3,000/night
    2.Deluxe --> INR 7,000/night
    3.Suite -->INR 12,000/night
    4.Executive  -->INR 20,000/night
    5.Premium  -->INR 35,000/night''')
        choice1=int(input('Enter your choice(1/2/3/4/5):'))
        choice2=''
        global rate
        if choice1==1:
            choice2='Standard'
            rate=3000
        elif choice1==2:
            choice2='Deluxe'
            rate=7000
        elif choice1==3:
            choice2='Suite'
            rate=12000
        elif choice1==4:
            choice2='Executive'
            rate=20000
        elif choice1==5:
            choice2='Premium'
            rate=35000
        cur.execute("Select * from r_details where room_type='{}' and status='vacant'".format(choice2,))
        av_rooms=cur.fetchall()
        if len(av_rooms)==0:
            print('--->There are no vacant rooms of the desired type')
            print('*'*120)
            return
        room_no=av_rooms[0][0]
        cur.execute("update r_details set status='occupied' where room_no={}".format(room_no,))
        Name=input('Enter your name:')
        Ph_no=input('Enter your phone number:')
        E_mail=input('Enter your E-mail:')
        Gender=input('Enter your gender(M/F)')
        Check_in=input('Enter the date of check in(YYYY-MM-DD):')
        cur.execute("insert into c_details(Name,Ph_no,E_mail,Gender,Check_in,Room_no) values('{}','{}','{}','{}','{}',{})".format(Name, Ph_no,E_mail,Gender,Check_in,room_no))
        mycon.commit()
        cur.execute("select Customer_ID from c_details where Ph_no='{}'".format(Ph_no,))
        var1=cur.fetchall()
        print('--->Room booked successfully !!\n--->Your customer ID is',var1[0][0],'and your Room no. is',room_no,'\n(Please note these down as it might be needed later)')
        print('*'*120)

    #function to display all customer details
    def showallcusdet():
        tabulate1=[]
        cur.execute('select * from c_details')
        data=cur.fetchall()
        for i in data:
            tabulate1.append(i)
        headers=['Customer_ID','Name','Ph_no','\tE_mail','Gender','Check_in','Room_no'] 
        table=tabulate(tabulate1,headers,tablefmt='fancy_grid')
        print(table)
        print('*'*120)
    #function to display customer details by ID
    def showcusdet():
        while True:
            cus_ID=input('Enter customer_ID:')
            cur.execute('select  Customer_ID,Name,Ph_no,E_mail,Gender,Check_in,Room_no from c_details where Customer_ID={}'.format(cus_ID,))
            var2=cur.fetchall()
            if len(var2)==0:
                print('--->Invalid Customer ID!!!')
                print('*'*120)
            else:
                tabulate1=[]
                for i in var2:
                    tabulate1.append(i)
                headers=['Customer_ID','Name','Ph_no','\tE_mail','Gender','Check_in','Room_no'] 
                table=tabulate(tabulate1,headers,tablefmt='fancy_grid')
                print(table)
                break
                print('*'*120)

    #function to edit customer details            
    def updtcusdet():
        while True:
            cusid=int(input('Enter your customer ID:'))
            cur.execute('select * from c_details where Customer_ID={}'.format(cusid))
            data=cur.fetchall()
            if len(data)==0:
                        print('Invalid Customer ID !!')
            else:          
                choice2=''
                print('''
        1.Name
        2.Ph_no
        3.E_mail
        4.Gender
        5.Check_in
        6.Room_no
        ''')
                choice=int(input('Please specify which customer details you would like to update/edit(1/2/3/4/5/6) :'))
                if choice==1:
                    choice2='Name'
                elif choice==2:
                    choice2='Ph_no'
                elif choice==3:
                    choice2='E_mail'
                elif choice==4:
                    choice2='Gender'
                elif choice==5:
                    choice2='Check_in'
                elif choice==6:
                    choice2='Room_no'
                
                if choice==1:
                    name=input('Enter the updated name :')
                    cur.execute("update c_details set Name='{}' where Customer_ID={}".format(name,cusid))
                if choice==2:
                    phno=input('Enter the updated phone number:')
                    cur.execute("update c_details set Ph_no='{}' where Customer_ID={}".format(phno,cusid))
                if choice==3:
                    email=input('Enter the update e-mail adress;')
                    cur.execute("update c_details set E_mail='{}' where Customer_ID={}".format(email,cusid))
                if choice==4:
                    gender=input('Enter the updated gender(M/F):')
                    cur.execute("update c_details set Gender='{}' where Customer_ID={}".format(gender,cusid))
                if choice==5:
                    
                    date=input('Enter the updated date of check_in(YYYY-MM-DDD):')
                    cur.execute("update c_details set Check_in='{}' where Customer_ID={}".format(date,cusid))
                if choice==6:
                    roomno=int(input('Enter updated room no:'))
                    cur.execute("update c_details set Room_no={} where Customer_ID={}".format(roomno,cusid))
                print('Customer details updated successfully !!')            
                print('*'*120)
                break 
    #function for checking out
    def checkout():
        while True:
            checkoutid=int(input('Enter the customer ID:'))
            cur.execute('select Room_no from c_details where Customer_ID={}'.format(checkoutid,))
            data=cur.fetchall()
            if len(data)==0:
                print('--->Invalid customer ID !!!')
                print('*'*120)
            else:
                dbt=data[0][0]
                cur.execute("update r_details set status='vacant' where Room_no={}".format(dbt,))
                cur.execute("delete from c_details where Customer_ID={}".format(checkoutid,))
                mycon.commit()
                choice=int(input('Enter the number of days stayed:'))
                totalbill=choice*rate
                time.sleep(1)
                print('--->Your total bill is',totalbill,'Please make your payment at the counter |^^|')
                print('--->Checked out successfully')
                print('*'*120)
                break

        
    #Program menu loop
    while True:
        print('MENU')
        print('-----')
        print('1.Create a new room')
        print('2.Edit room details')
        print('3.Remove Rooms')
        print('4.Show all rooms')
        print('5.Show all vacant rooms')
        print('6.Show all occupied rooms')
        print('7.Book a room')
        print('8.Show all customer details')
        print('9.Show customer details by ID')
        print('10.Update customer details')
        print('11.Check out')
        print('12.Exit')
        print('*'*120)
        choice4 = int(input('Enter your choice:'))

        if choice4 == 1:
            createroom()
        elif choice4 == 2:
            editroom()
        elif choice4 == 3:
            removroom()
        elif choice4 == 4:
            showallroom()
        elif choice4 == 5:
            showvacroom()
        elif choice4 == 6:
            showoccuproom()
        elif choice4 == 7:
            bookroom()
        elif choice4==8:
            showallcusdet()
        elif choice4 == 9:
            showcusdet()
        elif choice4 == 10:
            updtcusdet()
        elif choice4 == 11:
            checkout()
            break
        elif choice4 == 12:
            break
        else:
            print('--->INVALID CHOICE !!')
            continue

        while True:
            print('1.Menu')
            print('2.Exit')
            choice5 = int(input('Enter your choice:'))
            print('*'*120)

            if choice5 == 1:
                break
            elif choice5 == 2:
                break
            else:
                print('--->INVALID CHOICE !!!')
                continue
        
        if choice5 == 2:
            break

else:
    print('Connection to MySQL failed !!')
    print('*'*120)
mycon.close()




    
    





    



