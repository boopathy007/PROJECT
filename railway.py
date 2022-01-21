import os
import time

pas_id = 1

no_seat = []
no_wait = []

for i in range(1,4,1):
    no_seat.append(str(i))
    no_wait.append('w')

booked = []
wait = []
admin = [{'ad_name':'admin','ad_pass':1234}]
customer = []
train = []

def bookticket(pas_id,pnr):
    os.system('cls')
    if len(no_seat) >= 1:
        while True:
            c = True
            os.system('cls')
            print(len(no_seat))
            print("\n1.Coimbatore\n2.Tirupur\n3.Erode\n4.Salem\n5.Perambur\n6.Chennai")
            pickup = int(input("Pickup Point:"))
            drop = int(input("Drop Point:"))
            if pickup == drop and drop < pickup and pickup >=1 and drop<=6:

                input("Invalid Input!!press enter to continue")
                
            elif pickup != drop and drop > pickup and pickup >=1 and drop<=6:
                if len(booked) >=1:
                    for i in booked:
                        if i['drop'] == pickup and i['status'] == 'booked':
                            i['status'] = 'rebooked'
                            booked.append({'id': pas_id, 'pickup': pickup, 'drop': drop, 'seat_no': i['seat_no'],'pnr':pnr,'status':'booked'})
                            print("Your id:",pas_id)
                            input("Ticket Booked")
                            c = False
                            break


                    else:
                        booked.append({'id': pas_id, 'pickup': pickup, 'drop': drop, 'seat_no': no_seat[0], 'pnr': pnr,'status':'booked'})
                        print("Your id:", pas_id)
                        input("Ticket Booked")
                        no_seat.remove(no_seat[0])
                        break
                elif len(booked) == 0:
                    booked.append({'id': pas_id, 'pickup': pickup, 'drop': drop, 'seat_no': no_seat[0], 'pnr': pnr,'status':'booked'})
                    print("Your id:", pas_id)
                    input("Ticket Booked")
                    no_seat.remove(no_seat[0])
                    break
            if c:
                pass
            else:
                break
    elif len(no_seat) == 0:
        while True:
            os.system('cls')
            print("\n1.Coimbatore\n2.Tirupur\n3.Erode\n4.Salem\n5.Perambur\n6.Chennai")
            pickup = int(input("Pickup Point:"))
            drop = int(input("Drop Point:"))
            if pickup == drop and drop < pickup:
                input("Invalid Input!!press enter to continue")
            elif pickup != drop and drop > pickup:
                if len(no_wait) >= 1:
                    for i in booked:
                        if i['drop'] == pickup and i['status'] == 'booked':
                            i['status'] = 'rebooked'
                            booked.append({'id':pas_id,'pickup':pickup,'drop':drop,'seat_no':i['seat_no'],'pnr':pnr,'status':'booked'})
                            print("Your id:", pas_id)
                            break
                    else:
                        booked.append({'id': pas_id, 'pickup': pickup, 'drop': drop, 'seat_no': no_wait[0], 'pnr': pnr,
                                       'status': 'booked'})
                        print("Your id:", pas_id)
                        input("You are in waiting list!!\n press enter to continue")
                        no_wait.remove(no_wait[0])
                        break
                elif len(no_wait) == 0:
                    input("No seats avilable")
                    break




def cancelticket():
    os.system('cls')
    op = int(input("Enter Passenger ID:"))
    for i in booked:
        if op == i['id']:
            no_seat.append(i['seat_no'])

            for j in booked:
                if j['seat_no'] == 'w':

                    no_wait.append(j['seat_no'])
                    j['seat_no'] = i['seat_no']
                    no_seat.remove(i['seat_no'])
                    break



            booked.remove(i)

            input("Ticket cancel")
            break
    else:
        input("No passenger found")





pnr = 1001
while True:
    os.system('cls')
    op = int(input("1.Admin Login\n2.Customer login\n3.Exit"))
    if op == 1:
        ad_name = input("user name:")
        ad_pass = int('passeord:')
        for i in admin:
            if i['ad_name'] ==  ad_name and i['ad_pass'] == ad_pass:
                input("login succefull")

    elif op == 2:
        while True:
            a  = int(input("1.New User\2.Exiting User\n3.Exit"))

            if a== 1:
                os.system('cls')
                user_name = input("User nmae:")
                user_pass = int(input("Password:"))
                customer.append({'ueser_name':user_name,'user_pass':user_pass})

            elif a== 2:
                os.system('cls')
                u_name = input("user name:")
                u_pass = int(input("password:"))
                for i in customer:
                    if i['user_name'] == u_name and i['user_pass']:
                        input("login succesfull")

                        os.system('cls')
                        op_1 = int(input(("1.Book Ticket\n2.Cancel Ticket\n3.View ticket\n4.All pasenger\n5.Exit\nEnter the option:")))
                        if op_1 == 1:
                            os.system('cls')
                            bookticket(pas_id,pnr)
                            pas_id += 1
                            pnr += 1

                        elif op_1 == 2:
                            os.system('cls')
                            cancelticket()
                        elif op_1 == 3:
                            os.system('cls')
                            b = int(input("Enter Passenger ID:"))
                            for i in booked:
                               if i['id'] == b:
                                    print(i)
                                    input()
                        elif op_1 == 4:
                            for i in booked:
                                print(i)
                                input()
                        elif op_1 == 5:
                            break
            elif a == 3:
                os.system('cls')
                input("Thank You")
                exit()