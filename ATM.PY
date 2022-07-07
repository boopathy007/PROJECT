import os
import time
import datetime as dt
amount = {2000:0,500:0,200:0,100:0}
withdraw = {2000:0,500:0,200:0,100:0}
locked_account = []
usr = [{'username':'boopathy','pin':'1234','bank':'sbi','balance':10000,'trans':[],'status':'open'},
       {'username':'harish','pin':'1234','bank':'hdfc','free_trans':5,'balance':10000,'trans':[],'status':'open'},
       {'username':'faheem','pin':'1234','bank':'indian','free_trans':5,'balance':10000,'trans':[],'status':'open'},
       {'username':'santhosh','pin':'1234','bank':'kvb','free_trans':5,'balance':10000,'trans':[],'status':'open'},
       {'username':'sathish','pin':'1234','bank':'sbi','balance':10000,'trans':[],'status':'open'},
       {'username':'pranav','pin':'1234','bank':'kvb','free_trans':5,'balance':10000,'trans':[],'status':'open'},
       {'username':'akilan','pin':'1234','bank':'hdfc','free_trans':5,'balance':10000,'trans':[],'status':'open'},
       {'username':'akash','pin':'1234','bank':'indian','free_trans':5,'balance':10000,'trans':[],'status':'open'}
       ]
def balance_in_atm():
    sum = 0
    for i in amount:
        sum += (amount[i] * i)
    return sum

def customer(user,trans_no):

    while True:
        os.system("cls")
        print("        STATE BANK OF INDIA     ")
        print("-----------------------------------")
        print("\n\tWELCOME ****"+user['username'][-3:],'!')
        print("-----------------------------------")
        cus_op = int(input("1.Withdraw\n2.Deposit\n3.Show Balance\n4.Mini Statement\n5.Fund Transfer\n6.Change pin\n7.Exit\n-----------------------------------\nEnter the option:"))
        if cus_op == 1:

            trans_no += 1
            if user['balance'] <= 1000:
                os.system("cls")
                print("            STATE BANK OF INDIA           ")
                print("------------------------------------------")

                print("Acount balance is low.You cant't withdraw!")
                print("------------------------------------------")
                input("Press 'ENTER' to continue")
            elif user['balance'] > 1000:
                os.system("cls")
                print("          STATE BANK OF INDIA     ")
                print("------------------------------------------")
                print("\n")
                sum = balance_in_atm()
                c = int(input("Enter the amount to be withdraw:"))
                b = c
                if user['bank'] != 'sbi' and user['free_trans'] == 0:
                    c += 25

                elif user['bank'] != 'sbi' and user['free_trans'] != 0:
                    user['free_trans'] -= 1
                if c <= ((user['balance'])-1000):

                    if c<=balance_in_atm():

                        v = c
                        for i in amount:

                            no_notes = int(c/i)

                            if no_notes<= amount[i]:
                                withdraw[i] = no_notes
                                c = int(c % i)
                                user['balance'] -= (i*no_notes)
                                amount[i] -= no_notes
                                sum -= (i * amount[i])


                            elif no_notes >  amount[i]:
                                c -= (amount[i]*i)
                                withdraw[i] = amount[i]
                                user['balance'] -= (i * amount[i])
                                amount[i] -= amount[i]
                                sum -= (i * amount[i])


                        if c == 0:

                            print("\nRs:",v,"has been withdrawed ")

                            user['trans'].append([dt.date.today().strftime('%d/%m'),"         ",v,' (-) BY WDL'])
                            for k in withdraw:
                                withdraw[i] = 0
                            print("\nYour Account balance:",user['balance'])
                            print("-----------------------------------")
                            input("\n\t\tPress Enter to contiue!!")
                        elif c>0:
                            for m in amount:
                                amount[m] += withdraw[m]
                                user['balance'] += m*withdraw[m]
                                withdraw[m] = 0

                            os.system("cls")
                            print("-----------------------------------")
                            print("      ATM runnig out of money      ")
                            print("-----------------------------------")
                            input("    Press 'ENTER' to continue      ")

                    else:
                        os.system("cls")
                        print("-----------------------------------")
                        print("      ATM runnig out of money      ")
                        print("-----------------------------------")
                        input("    Press 'ENTER' to continue      ")
                else:
                    os.system("cls")
                     print("               STATE BANK OF INDIA                 ")
                    print("---------------------------------------------------")
                    print("\n")
                    print("    Account balance is low.You cant't withdraw!    ")

                    input("\n        Press 'Enter' to continue")



        elif cus_op == 2:
            trans_no += 1
            os.system("cls")
            print("        STATE BANK OF INDIA     ")
            print("-----------------------------------")
            print("\n")
            print("           DEPOSIT MENU           ")
            print("-----------------------------------")
            dp_amount = int(input("\nEnter the amount to be deposited:"))
            user['balance'] += dp_amount
            print("\nRs.",dp_amount,"has been deposited in your account")
            print("\nAccount Balnce:",user['balance'])
            print("-----------------------------------")
            user['trans'].append([dt.date.today().strftime('%d/%m'),"         ",dp_amount,'(+) BY DEP'])
            input("\n\tPress 'ENTER' to contiue")

        elif cus_op == 3:
            trans_no += 1
            os.system("cls")
            print("          STATE BANK OF INDIA     ")
            print("----------------------------------------")
            print((" DATE             TIME"))
            print(dt.datetime.now().strftime(" %d/%m                %H:%M"))
            print("TXN NO:",trans_no)
            print()
            print("Holder name:****"+user['username'][-3:])
            print("\nAccount Balance :",user['balance'])
            print("----------------------------------------")
            input("        Press 'ENTER' to contiue")

        elif cus_op == 4:
            trans_no += 1
            os.system('cls')


            if user['trans'] == [ ]:
                print("    STATE BANK OF INDIA     ")
                print("----------------------------")
                print("TXN.NO:",trans_no)
                print("\nNo Transaction has been done")

            elif len(user['trans'])>0:
                print("               STATE BANK OF INDIA              ")
                print("------------------------------------------------")
                print("     DATE                 TIME           ")
                print(dt.datetime.now().strftime('    %d/%m                 %H:%M'))
                print("    Account Holder Name : ****"+user['username'][-3:])
                print("    TXN.NO:", trans_no)
                print("------------------------------------------------")
                print("STATEMENT FOR ****"+user['username'][-3:])
                print("\n")
                if len(user['trans']) <=5:
                    for i in user['trans']:
                        print("     ",*i)
                elif len(user['trans']) >5:
                    for j in range(-5,0,1):
                        print("     ",*user['trans'][j])
                print("\n   Avil Balance :      ",user['balance'])
                print("------------------------------------------------")
            input("\n\tPress 'ENTER' to continue")

        elif cus_op == 5:

            os.system("cls")
            print("        STATE BANK OF INDIA     ")
            print("-----------------------------------")
            print("\n")
            print("           FUND TRANSFER           ")
            print("-----------------------------------")
            res_name = input("\nEnter name of receiver:")
            for i in usr:
                if res_name == i['username']:


                    tr_amount = int(input(("\nEnter Amount to transfer:")))
                    if user['bank'] != i['bank']:
                        tr_amount += 20

                    if user['balance'] > 1000 and user['balance']>tr_amount:
                        if (user['balance']-tr_amount)<= 1000:
                            os.system("cls")
                            print("\n\t\tAcount balance is low.You cant't transfer!\n")
                        else:
                            trans_no += 1
                            os.system("cls")
                            fi_amount = (tr_amount)
                            user['balance'] -= tr_amount
                            print("        STATE BANK OF INDIA     ")
                            print("-----------------------------------")
                            print("TXN.NO:",trans_no)
                            print()
                            print("Rs.",(tr_amount-20),"has been transferd to ****"+(i['username'][-3:]))
                            print("Your account balance:",user['balance'])
                            print("-----------------------------------")
                            user['trans'].append([dt.date.today().strftime('%d/%m'),"         ",tr_amount,'(-) TO TFR'])
                            i['trans'].append([dt.date.today().strftime('%d/%m'),"         ",(tr_amount-20),'(+) BY TFR'])
                            i['balance'] += ((fi_amount)-20)
                            input()
                            break

            else:

                os.system("cls")
                print("        STATE BANK OF INDIA     ")
                print("-----------------------------------")
                print("\nWe couldn't find the account",res_name)
        elif cus_op ==6:
            os.system('cls')
            while True:
                print("        STATE BANK OF INDIA     ")
                print("-----------------------------------")
                op_1 = input("1.Change pin\n2.Exit\nEnter option:")
                if op_1 == '1':
                    os.system('cls')
                    print("        STATE BANK OF INDIA     ")
                    print("-----------------------------------")
                    old_pin = input("Enter old pin:")
                    new_pin = input("Enter new pin:")
                    con_pin = input("Confirm your pin:")
                    if new_pin == con_pin:
                        user['pin'] = new_pin
                        print("pin Change succesfully")
                    elif new_pin != con_pin:
                        input("Password didn't match\n press enter to continue")
                        pass
                    elif  user['pin'] != old_pin:
                        input("Wrong account pin")
                        pass
                elif op_1 == '2':
                    break

        elif cus_op == 7:
            os.system("cls")
            break





def add_amount():
    os.system("cls")
    print("        STATE BANK OF INDIA     ")
    print("-----------------------------------")
    print("\n")
    print("       Add fund to the ATM         ")
    print("-----------------------------------")
    for i in amount:
        print("Enter the number of",i,"notes:",end=" ")
        n = int(input())
        amount[i] += n



def show_money():
    os.system("cls")
    print("        STATE BANK OF INDIA     ")
    print("-----------------------------------")
    print("\n")
    print("         Cash avilability          ")
    print("-----------------------------------")
    for i in amount:
        print("Number of",i,"notes avilable:",amount[i])
    print("-----------------------------------")
    print("Total Amount is:",balance_in_atm())
    print("-----------------------------------")



while (True):
    os.system('cls')
    print("-----------------------------------")
    print("       STATE BANK OF INDIA         ")
    print("               ATM                ")
    print("-----------------------------------")
    time.sleep(2)
    os.system('cls')
    print("        STATE BANK OF INDIA     ")
    print("-----------------------------------")
    print("\n")

    print("               MENU                ")
    print("-----------------------------------")
    op = input("1.Admin\n2.Customer\n3.Exit\n-----------------------------------\nEnter your choise:")
    trans_no = 1000

    if op == '1':
        os.system("cls")

        trail = 3
        while trail >= 1:
            os.system("cls")
            print("        STATE BANK OF INDIA     ")
            print("-----------------------------------")
            print("\n")
            print("        Enter login details      ")
            print("-----------------------------------")
            print("\n")
            u_name = input("Enter user name:")
            u_pass = int(input("Enter password:"))

            if u_pass == 1234 and u_name == "admin":
                os.system("cls")
                print("        STATE BANK OF INDIA     ")
                print("-----------------------------------")
                print("\n")

                print("         Login Succesfull         ")


                time.sleep(2)
                while True:
                    os.system("cls")
                    print("        STATE BANK OF INDIA     ")
                    print("-----------------------------------")
                    print("\n")
                    print("            ADMIN MENU\n-----------------------------------\n1.Add Amount\n2.Show Balance\n3.Blocked list\n4.Exit")
                    admin_op = int(input("Enter Your Choise : "))

                    if admin_op == 1:
                        add_amount()
                        print("\n-----------------------------------")
                        print("       Amount added succesfull           ")
                        print("-----------------------------------")
                        input("\n    Press 'ENTER' to continue\n")
                    elif admin_op == 2:
                        show_money()
                        input("\n\tPress 'ENTER' to continue\n")

                    elif admin_op == 3:
                        while True:
                            os.system('cls')
                            print("        STATE BANK OF INDIA     ")
                            print("-----------------------------------")
                            b = int(input("1.Unblock\n2.Exit\nEnter option:"))
                            if b == 1:
                                if locked_account == []:
                                    os.system('cls')
                                    print("        STATE BANK OF INDIA     ")
                                    print("-----------------------------------")

                                    input("\nNo bloced account")
                                else:
                                    os.system('cls')
                                    print("        STATE BANK OF INDIA     ")
                                    print("-----------------------------------")
                                    for q in locked_account:
                                        print(q['username'])
                                    j = input("Enter User name to unblock:")
                                    for d in locked_account:
                                        if j == d['username']:
                                            d['status'] = 'open'
                                            input("Account Unblocked")
                                            locked_account.remove(d)
                                            break


                            elif b== 2:
                                break




                    elif admin_op == 4:
                        os.system('cls')
                        print("        STATE BANK OF INDIA     ")
                        print("-----------------------------------")
                        print("\n")
                        print("             Thank You!         ")

                        input("\n\tPress 'ENTER' to continue\n")
                        break
                    else:
                        print("        STATE BANK OF INDIA     ")
                        print("-----------------------------------")
                        print("\n")
                        print("Wrong Option")
                        input("\n\tPress 'ENTER' to continue\n")
                trail = 0

            elif u_pass != 1234:
                os.system("cls")
                print("        STATE BANK OF INDIA     ")
                print("-----------------------------------")
                print("\n")

                print("invalid password")
                print("Attempts Left : ",trail-1)

                trail -= 1
                input("\n\tPress 'ENTER' to continue\n")


    elif op == '2':

        trail = 3
        while trail > 0:
            os.system("cls")
            print("        STATE BANK OF INDIA     ")
            print("-----------------------------------")
            print("\n")
            print("\tEnter login details")
            print("-----------------------------------")


            print("Enter user name:",end=" ")
            cu_name = input()
            print("Enter password:",end=" ")
            cu_pass = (input())
            os.system('cls')


            for i in usr:

                if cu_name == i['username'] and cu_pass == i['pin']:
                    if i['status'] == 'open':
                        os.system('cls')
                        print("        STATE BANK OF INDIA     ")
                        print("-----------------------------------")
                        print("\n")

                        print("         Login Succesfull!         ")

                        time.sleep(2)
                        user = i
                        tr = trans_no
                        customer(user, tr)
                        trans_no = tr

                        trail = 0
                        break

                    elif i['status'] == 'blocked':
                        input("Account locked!!! Contact admin")
                        break
                        break
                elif cu_name == i['username'] and i['status'] == 'blocked':
                    os.system('cls')
                    input("Account locked!!! contact admin")
                    break
                    break
                elif cu_name == i['username'] and cu_pass != i['pin']:
                    os.system('cls')
                    trail -= 1
                    print("        STATE BANK OF INDIA     ")
                    print("-----------------------------------")
                    print("\n")
                    print("Invalid input")
                    print("Attempt left", trail)
                    print("\n-----------------------------------")
                    input("\nPress 'ENTER' to continue")
                    if trail == 0:
                        input("Account locked!!!")
                        locked_account.append(i)
                        i['status'] = 'blocked'
                        break
                    break

                elif cu_name != i['username'] :
                    input("invalid user name")
                    break







    elif op == '3':
        os.system('cls')
        print("        STATE BANK OF INDIA     ")
        print("-----------------------------------")
        print("\n")

        print("            Thank You              ")

        exit()

    else:
        os.system('cls')
        print("        STATE BANK OF INDIA     ")
        print("-----------------------------------")
        print("\n")
        print("Invalid option")
        input("\nPress 'ENTER' to contiue")


