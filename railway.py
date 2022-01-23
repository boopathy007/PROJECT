import os

pnr = 1000
gap =" "*2

ps_id = 1
booked = []
wait = []
admin = [{'ad_name':'admin','ad_pass':1234}]
customer = []
train = []

def bookticket(pnr,a):
    os.system('cls')
    print('TRAIN NAME'.ljust(15),'TRAIN NUMBER'.ljust(15),'TO'.ljust(10),'TO'.ljust(10),'avilable seat'.ljust(15))
    print("-" * 70)
    for i in train:
        print(i['t_name'].ljust(15),str(i['t_num']).ljust(15),i['station'][0].ljust(15),i['station'][-1].ljust(15),str(i['available_seat']).ljust(15))
    print("-" * 70)
    tr_num = int(input("Enter train number:"))

    for i in train:
        if i['t_num'] == tr_num:
            print("\ntrain name:", i['t_name'])
            print("\nStations:")
            co = 0
            for j in i['station']:
                co += 1
                print(co, '.', *j, sep='')
            no_se = int(input("Enter no.of pasengers:"))
            if no_se <= i['available_seat'] and i['available_seat'] != 0 :
                for n in range(no_se):
                    if no_se <= ((len(i['seat_no'])) + (len(i['wait']))):
                        p_name = input(("passenger name:"))
                        pickup = int(input("Enter pickup station:"))
                        drop = int(input("Enter drop station:"))
                        for p in range(len(i['seat_no'])):
                            if sum(i['seat_no'][p][pickup - 1:drop - 1]) == 0:
                                booked.append(
                                    {'p_name': p_name, 't_name': i['t_name'], 't_num': i['t_num'], 'ps_id': a['ps_id'],
                                     'seat_no': (p + 1), 'pnr': pnr, 'status': 'booked',
                                     'pickup': i['station'][pickup - 1], 'drop': i['station'][drop - 1],
                                     'pick_no': (pickup), 'drop_no': (drop)})
                                print("Ticket booked!!!")
                                print("Seat no:", (p + 1))
                                i['available_seat'] -= 1
                                input()
                                for k in range(pickup - 1, drop):
                                    i['seat_no'][p][k] = 1
                                break
                        else:
                            for g in range(len(i['wait'])):
                                if sum(i['wait'][g][pickup - 1:drop - 1]) == 0:
                                    booked.append(
                                        {'p_name': p_name, 't_name': i['t_name'], 't_num': i['t_num'],
                                         'ps_id': a['ps_id'],
                                         'seat_no': (g + 1), 'pnr': pnr, 'status': 'waiting',
                                         'pickup': i['station'][pickup - 1], 'drop': i['station'][drop - 1],
                                         'pick_no': (pickup), 'drop_no': (drop)})
                                    print("Your are in waiting list")
                                    print("Seat no: W", (g + 1))
                                    i['available_seat'] -= 1
                                    input()
                                    for u in range(pickup - 1, drop):
                                        i['wait'][g][u] = 1
                                    break
                            else:

                                input("No Seat avilabele!!!!")
                                input()
                                break


            elif no_se > i['available_seat'] or i['available_seat'] == 0:
                print("No seat avilable")
                input()
                break


while True:
    while True:
        os.system('cls')
        op = int(input("1.Admin Login\n2.Customer login\n3.Exit\nEnter option:"))
        if op == 1:
            os.system('cls')
            ad_name = input("user name:")
            ad_pass = int(input("password:"))
            for i in admin:
                if i['ad_name'] == ad_name and i['ad_pass'] == ad_pass:
                    while True:
                        os.system('cls')

                        b = int(input("1.Add Train\n2.exit\nenter option:"))
                        if b == 1:
                            os.system('cls')
                            station = []
                            rac_no = []
                            wait = []
                            seat_no = []
                            po = []
                            po1 = []
                            t_name = input("Train Name:")
                            t_num = int(input("Train Number:"))
                            no_station = int(input("No of stations:"))

                            for i in range(no_station):
                                sta = input("Station Name:").upper()
                                station.append(sta)
                            no_seat = int(input("no of seat:"))
                            for k in range(no_seat ):
                                for a in range(no_station):
                                    po.append(0)
                                seat_no.append(po)
                                po = []

                            no_wait = int(input("enter no.of waiting ticket:"))
                            for k in range(no_wait):
                                for r in range(no_station):
                                    po1.append(0)
                                wait.append(po1)
                                po1 = []
                            total_seat = no_seat + no_wait

                            train.append({'t_name': t_name, 't_num': t_num, 'station': station, 'seat_no': seat_no,
                                          'wait': wait, 'to_seat': no_seat,'available_seat':total_seat})
                            input("Train added succefully!!")
                        elif b == 2:
                            break



                        elif b == 2:
                            break

        elif op == 2:
            os.system('cls')
            while True:
                os.system('cls')
                a = int(input("1.New User\n2.Exiting User\n3.Exit"))

                if a == 1:
                    os.system('cls')
                    user_name = input("User name:")
                    user_pass = int(input("Password:"))
                    customer.append({'user_name': user_name, 'user_pass': user_pass, 'ps_id': ps_id})

                    input("Account created!!!")
                    ps_id += 1
                elif a == 2:
                    os.system('cls')

                    os.system('cls')
                    u_name = input("user name:")
                    u_pass = int(input("password:"))
                    for i in customer:
                        if i['user_name'] == u_name and i['user_pass']:
                            input("login succesfull")
                            while True:
                                os.system('cls')
                                op_1 = int(input(("1.Book Ticket\n2.Cancel Ticket\n3.View ticket\n4.Exit\nEnter the option:")))
                                if op_1 == 1:
                                    os.system('cls')
                                    bookticket(pnr, i)
                                    pnr += 1

                                elif op_1 == 2:
                                    os.system('cls')
                                    print(
                                        f"{'PNR':5s}{gap}{'passenger name':15s}{gap} {'Train name':8s}{gap}{'train number':12s}{gap}{'from':5s}{gap}{'to':5s}{gap}{'seat no':10s}{gap}{'status':12s}")
                                    print("-" * 80)

                                    for m in booked:

                                        if m['ps_id'] == i['ps_id']:
                                            print(
                                                f"{m['pnr']:5}{gap}{m['p_name']:15s}{gap}{m['t_name']:8s}{gap}{m['t_num']:12}{gap}{m['pickup']:5s}{gap}{m['drop']:5s}{gap}{m['seat_no']:10}{gap}{m['status']:12s}{gap}{m['status']:10s}")
                                        else:
                                            input("No tickes booked")
                                            break
                                    c_pnr = int(input("Enter PNR no to cancel:"))
                                    for m in booked:
                                        if m['ps_id'] == i['ps_id'] and m['pnr'] == c_pnr:
                                            for h in train:
                                                if h['t_num'] == m['t_num']:
                                                    for s in range(m['pick_no']-1,m['drop_no']):
                                                        h['seat_no'][m['seat_no']-1][s] = 0
                                                    booked.remove(m)
                                                    h['available_seat'] += 1

                                                    for g in booked:
                                                        if g['status'] == 'waiting' and g['t_num'] == h['t_num']:
                                                            for q in range(len(h['seat_no'])):
                                                                if sum(h['seat_no'][q][g['pick_no']-1:g['drop_no']]) == 0:
                                                                    g['status'] = 'booked'
                                                                    h['available_seat'] += 1
                                                                    for s in range(g['pick_no']-1,g['drop_no']):
                                                                        h['wait'][g['seat_no']-1][s] = 0
                                                                    g['seat_no'] = q + 1
                                            input("Ticket Cancelled")

                                elif op_1 == 3:
                                    os.system('cls')
                                    print(
                                        f"{'PNR':5}{gap}{'passenger name':15s}{gap} {'Train name':8s}{gap}{'train number':12}{gap}{'from':5s}{gap}{'to':5s}{gap}{'seat no':10}{gap}{'status':12}")
                                    print("-" * 70)
                                    if booked == []:
                                        input("No ticket has been booked")
                                    elif booked != []:

                                        for m in booked:

                                            if m['ps_id'] == i['ps_id']:
                                                print(
                                                    f"{m['pnr']:5}{gap}{m['p_name']:15s}{gap}{m['t_name']:8s}{gap}{m['t_num']:12}{gap}{m['pickup']:5s}{gap}{m['drop']:5s}{gap}{m['seat_no']:10}{gap}{m['status']:10s}")
                                        input("\nPress enter to continue")

                                elif op_1 == 4:
                                    os.system('cls')
                                    break


                elif a == 3:
                    os.system('cls')
                    input("Thank You")
                    break

        elif op == 3:
            os.system('cls')
            input("Thank You")
            exit()
