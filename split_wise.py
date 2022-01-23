import os
group_id = 1000
users,group,activity= [],[],[]
group_type_list = {'1':'Trip','2':'Hotel','3':'Travel','4':'Food','5':'Apartment','6':'other'}
user_id = 100
total_activity = []
def usermenu(user,activity,group,group_id):
    global n
    os.system('cls')
    while True:
        os.system('cls')
        print("".rjust(12), "SPLIT WISE")
        print("-" * 42)
        print("1.Create\Delete Group".ljust(25), "2.Existing Group".rjust(5))
        print("3.Activity".ljust(25), "4.Add Expense".rjust(5))
        print("5.Exit")
        op = int(input("\nEnter Option:"))
        if op == 1:
            os.system('cls')
            while True:
                os.system('cls')
                op_1 = int(input("1.Create Group\n2.Delete Group\n3.Exit\nEnter option:"))
                if op_1 == 1:
                    group_name = input("Enter Group Name:")
                    print("Choose Group Type:")
                    jk = 1
                    for kl in group_type_list:
                        print(jk, '.', group_type_list[kl].ljust(25))
                        jk += 1
                    op_2 = input("enter group type:")
                    group_type = group_type_list[op_2]

                    group_id += 1
                    no_members = int(input("No.of members:"))
                    for h in range(no_members):
                        member_id = int(input("Enter Friends UserID:"))
                        for k in users:
                            if member_id == k['user_id']:
                                group.append({'owner_id': user['user_id'], 'user_name': k['user_name'],
                                              'group_name': group_name, 'group_id': group_id, 'user_id': member_id,
                                              'group_type': group_type,
                                              })

                                input("Member added to group")
                                break

                    total_activity.append({'owner_id': user['user_id'], 'user_id': user['user_id'],
                                           'activity': ['created group', group_name]})


                elif op_1 == 2:
                    print("".rjust(10), "SPLIT WISE")
                    print("-" * 45)
                    y = False
                    if group == []:
                        input("No group")
                        break

                    elif group != []:

                        for h in group:
                            if h['owner_id'] == user['user_id']:
                                y = True
                    if y:

                        print("Group Name".ljust(15), "Group Type".rjust(15), "GroupID".rjust(10))
                        print("-" * 45)
                        v = []
                        for j in group:
                            if j['owner_id'] == user['user_id'] and j['group_name'] not in v:
                                print(j['group_name'].ljust(15), j['group_type'].rjust(15),
                                      str(j['group_id']).rjust(15))
                                v.append(j['group_name'])
                        rem_grp = int(input("Enter groupID to remove or '0' to exit:"))
                        if rem_grp == 0:
                            break

                        elif rem_grp != 0:
                            for k in range(len(group)):
                                for j in group:
                                    if j['group_id'] == rem_grp and j['owner_id'] == user['user_id']:
                                        n = j
                                        group.remove(j)
                            total_activity.append({'owner_id': user['user_id'], 'user_id': user['user_id'],
                                                   'activity': [n['group_name'], 'group removed']})
                            for k in activity:
                                if k['group_id'] == rem_grp:
                                    activity.remove(k)

                            input("Group Removed")
                    else:
                        input("No group")

                elif op_1 == 3:
                    break

        elif op == 2:
            os.system('cls')
            while True:
                os.system('cls')
                print("".rjust(10), "SPLIT WISE")
                print("-" * 45)
                print("Group Name".ljust(15), "Group Type".rjust(15), "GroupID".rjust(10))
                print("-" * 45)

                v = []
                for j in group:
                    if j['owner_id'] == user['user_id'] or j['user_id'] == user['user_id']:
                        if j['group_name'] not in v:
                            print(j['group_name'].ljust(15), j['group_type'].rjust(15), str(j['group_id']).rjust(15))
                            v.append(j['group_name'])

                gp_id = int(input("Enter Group ID or '0' to exit : "))
                if gp_id == 0:
                    break
                while True:
                    os.system('cls')
                    print("GroupID".ljust(10), "Group Member".ljust(20),"MemberID".ljust(10))
                    print("-" * 55)
                    for gh in group:
                        if gh['group_id'] == gp_id:
                            print(str(gh['group_id']).ljust(10), gh['user_name'].ljust(20),str((gh['user_id'])).ljust(10))
                    print("-" * 55)
                    b = int(input("1.Add Expense\n2.Totals\n3.Activity\n4.Exit\nEnter option:"))
                    if b == 1:
                        acty = input("Enter Description:")
                        total_exp = int(input("Enter Amount:"))

                        ty = int(input("1.Split Equally\n2.Split Unequally\n3.Split by percentage\nEnter option:"))
                        if ty == 1:
                            os.system('cls')
                            print("GroupID".ljust(10), "Group Member".ljust(20), "MemberID".ljust(10))
                            print("-" * 55)
                            for gh in group:
                                if gh['group_id'] == gp_id and gh['owner_id'] == user['user_id'] or gh['user_id'] == user['user_id']:
                                    print(str(gh['group_id']).ljust(10), gh['user_name'].ljust(20),
                                          str((gh['user_id'])).ljust(10))
                            print("-" * 55)

                            no_mem = int(input("Enter number of members to split:"))

                            paid_id = int(input("Enter payer ID:"))

                            exp = round((total_exp / no_mem), 2)
                            for j in range(no_mem):
                                p_id = int(input("Enter memberID:"))
                                if paid_id == p_id:
                                    for fg in group:
                                        if fg['group_id'] == gp_id and fg['owner_id'] == user['user_id']:
                                            if fg['user_id'] == paid_id:
                                                print(fg['user_name'], 'paid RS.', total_exp)
                                                activity.append({'user_name': fg['user_name'],
                                                                 'group_name': fg['group_name'], 'group_id': gp_id,
                                                                 'user_id': fg['user_id'],'owner_id':user['user_id'],
                                                                 'expense': total_exp,'purpose':acty, 'paid': total_exp,'barrow':0,
                                                                 'paid_id': paid_id, 'status': 'paid'})
                                                total_activity.append(
                                                    {'owner_id':user['user_id'],'user_id': paid_id, 'activity': ['paid', total_exp,'to',fg['group_name'],'group']})

                                                break
                                elif paid_id != p_id:
                                    for fg in group:
                                        if fg['group_id'] == gp_id and fg['owner_id'] == user['user_id'] or fg['user_id'] == user['user_id']:
                                            if fg['user_id'] == p_id:
                                                print(fg['user_name'], 'paid RS.', exp)
                                                activity.append({'user_name': fg['user_name'],
                                                                 'group_name': fg['group_name'], 'group_id': gp_id,
                                                                 'user_id': fg['user_id'],'owner_id':user['user_id'],
                                                                 'expense': total_exp,'paid':0,'purpose':acty,'barrow':exp,
                                                                 'paid_id': paid_id,'status': 'barrow'})
                                                total_activity.append({'owner_id':user['user_id'],'user_id': p_id,
                                                                       'activity': ['barrowed', exp, 'from', paid_id,'in',fg['group_name'],'group']})
                                                break

                            input()
                        elif ty == 2:
                            print("GroupID".ljust(10), "Group Member".ljust(20), "MemberID".ljust(10))
                            print("-" * 55)
                            for gh in group:
                                if gh['group_id'] == gp_id and gh['owner_id'] == user['user_id']:
                                    print(str(gh['group_id']).ljust(10), gh['user_name'].ljust(20),
                                          str((gh['user_id'])).ljust(10))
                            print("-" * 55)

                            paid_id = int(input("Enter payer ID:"))
                            b = []
                            while True:
                                sum = 0
                                for fg in group:
                                    if fg['group_id'] == gp_id and fg['owner_id'] == user['user_id'] or fg['user_id'] == user['user_id']:
                                        print("Amount shared by",fg['user_name'],'(',fg['user_id'],')')
                                        amt = int(input("Enter amount:"))
                                        b.append([fg['user_id'],amt])

                                for a in b:
                                    sum += a[1]
                                if sum == total_exp:
                                    for gh in group:
                                        if gh['group_id'] == gp_id and gh['owner_id'] == user['user_id']:
                                            for a in b:
                                                if a[0] == gh['user_id']:
                                                    if a[0] == paid_id:
                                                        activity.append({'user_name': gh['user_name'],
                                                                     'group_name': gh['group_name'], 'group_id': gp_id,
                                                                     'user_id': gh['user_id'],'owner_id':user['user_id'],
                                                                     'expense': total_exp,'paid':total_exp,'barrow':0,'paid_id': paid_id,
                                                                     'status': 'paid','purpose':acty})
                                                        total_activity.append({'owner_id':user['user_id'],'user_id': gh['user_id'],
                                                                               'activity': ['paid', total_exp, 'to',
                                                                                            gh['group_name'], 'group']})
                                                    elif a[0] != paid_id:
                                                        activity.append({'user_name': gh['user_name'],
                                                                         'group_name': gh['group_name'],
                                                                         'group_id': gp_id,
                                                                         'user_id': gh['user_id'],'owner_id':user['user_id'],
                                                                         'expense': total_exp,'paid':0,'barrow':a[1], 'paid_id': paid_id,
                                                                         'status': 'barrow','purpose':acty})
                                                        total_activity.append({'owner_id':user['user_id'],'user_id': gh['user_id'],
                                                                               'activity': ['barrowed', a[1], 'from',paid_id,'in',gh['group_name'],'group']})

                                    break
                                elif sum != total_exp:
                                    if sum > total_exp:
                                        print("per person amount don't add upto to total expense")
                                        print("You are over by",(sum - total_exp))
                                        sum = 0
                                        input()
                                    elif sum < total_exp:
                                        print("per person amount don't add upto to total expense")
                                        print("You are under by", (total_exp - sum))
                                        sum = 0
                                        input()

                        elif ty == 3:
                            print("GroupID".ljust(10), "Group Member".ljust(20), "MemberID".ljust(10))
                            print("-" * 55)
                            for gh in group:
                                if gh['group_id'] == gp_id and gh['owner_id'] == user['user_id'] or gh['user_id'] ==  user['user_id']:
                                    print(str(gh['group_id']).ljust(10), gh['user_name'].ljust(20),
                                          str((gh['user_id'])).ljust(10))
                            print("-" * 55)

                            paid_id = int(input("Enter payer ID:"))
                            b = []
                            sum = 0
                            while True:
                                for fg in group:
                                    if fg['group_id'] == gp_id and fg['owner_id'] == user['user_id'] or fg['user_id'] == \
                                            user['user_id']:
                                        print("Amount shared by", fg['user_name'], '(', fg['user_id'], ')')
                                        per = int(input("Enter percent:"))
                                        sum += per
                                        amt = round((total_exp * per / 100), 2)
                                        b.append([fg['user_id'], amt])
                                if sum == 100:
                                    for gh in group:
                                        if gh['group_id'] == gp_id and gh['owner_id'] == user['user_id'] or gh[
                                            'user_id'] == user['user_id']:
                                            for a in b:
                                                if a[0] == gh['user_id']:
                                                    if a[0] == paid_id:
                                                        activity.append({'user_name': gh['user_name'],
                                                                         'group_name': gh['group_name'],
                                                                         'group_id': gp_id,
                                                                         'user_id': gh['user_id'],
                                                                         'expense': total_exp, 'paid': a[1],
                                                                         'barrow': 0,
                                                                         'paid_id': paid_id,
                                                                         'owner_id': user['user_id'],
                                                                         'status': 'paid', 'purpose': acty})
                                                        total_activity.append(
                                                            {'owner_id': user['user_id'], 'user_id': paid_id,
                                                             'activity': ['paid', total_exp, 'to', gh['group_name'],
                                                                          'group']})

                                                    elif a[0] != paid_id:
                                                        activity.append(
                                                            {'user_name': gh['user_name'], 'owner_id': user['user_id'],
                                                             'group_name': gh['group_name'],
                                                             'group_id': gp_id,
                                                             'user_id': gh['user_id'],
                                                             'expense': total_exp, 'paid': 0,
                                                             'barrow': a[1],
                                                             'paid_id': paid_id,
                                                             'status': 'barrow', 'purpose': acty})
                                                        total_activity.append(
                                                            {'owner_id': user['user_id'], 'user_id': gh['user_id'],
                                                             'activity': ['barrowed', a[1], 'from', gh['user_id'], 'in',
                                                                          gh['group_name'],
                                                                          'group']})
                                    break

                                elif sum != 100:
                                    if sum > 100:
                                        print("Per person percentage don't add upto 100")
                                        print("You are over buy", (sum - 100))
                                        input()
                                        break
                                    elif sum < 100:
                                        print("Per person percentage don't add upto 100")
                                        print("You are under buy", (100 - sum))
                                        input()

                        elif ty == 4:
                            break

                    elif b == 2:
                        os.system('cls')
                        d = False
                        for ac in activity:
                            if ac['group_id'] == gp_id:
                                d = True
                        if d:
                            os.system('cls')
                            while True:
                                print("GROUP NAME".ljust(15), "GROUPID".ljust(10), "MEMBER NAME".ljust(15),
                                      "MEMBERID".ljust(10),
                                      "EXPENSE".ljust(12),
                                      "PAID BY".ljust(10), "PAID".ljust(8), "BARROW".ljust(8))
                                print("-" * 110)
                                a = []
                                for g in activity:
                                    sum = 0

                                    for h in activity:
                                        if h['user_id'] == g['user_id'] and h['paid_id'] == g['paid_id']:
                                            sum += h['barrow']
                                    if g['user_id'] not in a and g['barrow'] != 0:
                                        print(g['group_name'].ljust(15),str(g['group_id']).ljust(10)
                                          ,g['user_name'].ljust(15),str(g['user_id']).ljust(10),
                                          str(g['expense']).ljust(12),
                                          str(g['paid_id']).ljust(10),str(g['paid']).ljust(8),
                                          str(sum).ljust(8))
                                        a.append(g['user_id'])
                                    elif g['user_id'] in a:
                                        sum += sum

                                op_3 = int(input("1.Settle Up\n2.Exit\nEnter option:"))
                                if op_3 == 1:
                                    set_id = int(input("Enter Member id to settle up:"))
                                    os.system('cls')
                                    print("GROUP NAME".ljust(15), "GROUPID".ljust(10), "MEMBER NAME".ljust(15),
                                          "MEMBERID".ljust(10),
                                          "EXPENCE".ljust(12),
                                          "PAID BY".ljust(10), "PAID".ljust(8), "BARROW".ljust(8))
                                    print("-" * 110)
                                    for g in activity:
                                        if g['group_id'] == gp_id and g['user_id'] == set_id:
                                            print(g['group_name'].ljust(15),str(g['group_id']).ljust(10),
                                                  g['user_name'].ljust(15),str(g['user_id']).ljust(10),
                                                  str(g['expense']).ljust(12),str(g['paid_id']).ljust(10),
                                                  str(g['paid']).ljust(8),str(g['barrow']).ljust(8))
                                    br_id = int(input("Enter barrowers id to settle up or '0' to exit:"))
                                    if br_id == 0:
                                        break
                                    elif br_id != 0:
                                        for g in activity:
                                            if g['group_id'] == gp_id and g['user_id'] == set_id and g['paid_id'] == br_id:
                                                total_activity.append(
                                                    {'owner_id': user['user_id'], 'user_id': set_id,
                                                     'activity': ['paid',g['barrow'], 'to', g['paid_id']]})

                                                activity.remove(g)
                                                print(br_id,"has been settled up")
                                                input()
                                elif op_3 == 2:
                                    break

                        elif d == False:
                            input("No settelment!!")
                            break

                    elif b == 3:
                        os.system('cls')
                        print("GROUP NAME".ljust(15), "GROUPID".ljust(10), "MEMBER NAME".ljust(15),
                              "MEMBERID".ljust(10), "ACTIVITY".ljust(15),
                              "EXPENSE".ljust(12),
                              "PAID BY".ljust(10), "PAID".ljust(8), "BARROW".ljust(8))
                        print("-" * 110)
                        a = []
                        for g in activity:

                            if g['group_id'] == gp_id:
                                print(g['group_name'].ljust(15), str(g['group_id']).ljust(10)
                                      , g['user_name'].ljust(15), str(g['user_id']).ljust(10),
                                      g['purpose'].ljust(15), str(g['expense']).ljust(12),
                                      str(g['paid_id']).ljust(10), str(g['paid']).ljust(8),
                                      str(g['barrow']).ljust(8))
                                a.append(g['user_id'])
                        input()

                    elif b == 4:
                        break

        elif op == 3:
            os.system('cls')
            d = False
            for ac in total_activity:
                if ac['user_id'] == user['user_id']:
                    d = True
            if d:
                for ac in total_activity:
                    if ac['owner_id'] == user['user_id']:
                        print(*ac['activity'])

                input()
            elif d == False:
                input("No Activity!!")
                break
        elif op == 4:
            os.system("cls")

        elif op == 5:
            break



while True:

    os.system('cls')
    print("".rjust(8),"SPLIT WISE")
    print("-"*30)
    op= int(input("1.New User\n2.Existing User\n3.Exit\nEnter option:"))
    if op== 1:

        os.system('cls')
        print("".rjust(8), "SPLIT WISE")
        print("-" * 30)
        new_username = input("Enter Username:")
        new_password = int(input("Enter password:"))
        user_id += 1
        print("Your UserID:",user_id)
        users.append({'user_name':new_username,'user_password':new_password,'user_id':user_id})
        input("Account Created!!!")
    elif op==2:
        os.system('cls')
        log_id = int(input("Enter user ID:"))
        log_password = int(input("Enter password:"))
        for user in users:
            if user['user_id'] == log_id and user['user_password'] == log_password:
                input("LOGIN SUCCESFULL!!")
                usermenu(user,activity,group,group_id)

    elif op==3:
        exit()