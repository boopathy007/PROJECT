import os
from operator import  itemgetter as it
book_id = 100
gap = " "*3
rent_history = []
books = []
rent_list = []
cart = []
student_list =[{'name': "boopathy", 'st_id':"s101" , 'st_pass': 123, 'wallet': 1500,'status':"approved"}]
admin_list = [{'name':'boopathy','ad_id':'a101','ad_pass':123}]
def admin(book_id):
    os.system('cls')
    while True:

        os.system('cls')
        print("Welcome to admin menu")
        print('1.Add book\n2.Modify book\n3.View all book\n4.Search book\n5.Add admin or student\n6.Fine limits\n7.Report\n8.Exit')
        try:
            op_1 = int(input("Enter your option:"))
            if op_1 == 1:
                os.system('cls')
                print("Add books")
                while True:
                    book_id += 1
                    os.system('cls')
                    print("Add books")
                    book_name = input("Enter book name:")
                    book_author = input("Enter book auhtor name:")
                    cost_book = int(input("Cost of book:"))
                    quantity = int(input("Enter quantity:"))
                    books.append({'book_name':book_name,'author':book_author,'cost':cost_book,'book_id':book_id,'quantity':quantity,'status':'available'})
                    input("Book added to list succefully")
                    os.system('cls')

                    g = int(input("Want to add more books\n1.Yes\n2.No"))
                    if g==1:
                       pass

                    elif g== 2:
                        break

            elif op_1 == 2:
                os.system('cls')
                print("Book modify")
                while True:
                    if books == []:
                        input("No books")
                        break
                    os.system('cls')
                    print("Book modify")
                    print(f"{'Name of book':20s}{'Author Name':15s}{'Bookid':10s}{'Avilable quantity':20s}{'cost':10s}")
                    print("-" * 50)
                    for i in books:
                        print(f"{i['book_name']:20s}{i['author']:15s}{i['book_id']:5}{i['quantity']:5}{i['cost']:8}")
                    try:

                        os.system('cls')
                        print("Book modify")
                        print(f"{'Name of book':20s}{'Author Name':15s}{'Bookid':10s}{'Avilable quantity':20s}{'cost':10s}")
                        for i in books:
                            print(f"{i['book_name']:20s}{i['author']:15s}{i['book_id']:5}{i['quantity']:5}{i['cost']:8}")
                        op_2 = int(input("Enter book id to modify or '0' to exit"))
                        if op_2 == 0:
                            break
                        elif op_2 != 0:
                            for i in books:
                                if op_2 == i['book_id']:
                                    op_3 = int(input("1.Add quantity\n2.Remove quantity\n3.Change price\n4.Remove book\nEnter option"))
                                    if op_3 == 1:
                                        ad_qty = int(input("Enter quantity to add:"))
                                        i['quantity'] += ad_qty
                                        input("Book added")
                                        break
                                    elif op_3 == 2:
                                        re_qty = int(input("Enter quantity to remove:"))
                                        i['quantity'] -= re_qty
                                        input("Book added")
                                        if i['quantity'] == 0:
                                            books.pop(i)
                                        break
                                    elif op_3 == 3:
                                        print("Current price of book:", i['cost'])
                                        pr_ = int(input("Enter new price of book:"))
                                        i['cost'] = pr_
                                        input("Price of book changed!!!")
                                        break
                                    elif op_3 == 4:
                                        books.remove(i)
                                        input("Book removed from list")
                                        break

                                break
                            break

                    except:
                        input("Invalid input")

            elif op_1 == 3:
                os.system('cls')
                print(f"{'Name of book':20s}{gap}{'Author Name':15s}{gap}{'Bookid':10s}{gap}{'Avilable quantity':20s}{gap}{'status':20s}")
                print("-"*50)
                books.sort(key=it('book_name'))
                for y in books:
                    print(f"{y['book_name']:20s}{gap}{y['author']:15s}{gap}{y['book_id']:5}{gap}{y['quantity']:20}{gap}{y['status']}")
                input()


            elif op_1 == 4:
                os.system('cls')
                print("Book search")
                op_4 = int(input("Enter book id:"))
                for i in books:
                    if op_4 == i['book_id']:
                        print(f"{'Name of book':20s}{'Author Name':15s}{'Bookid':10s}{'Avilable quantity':20s}")
                        print("-" * 50)
                        print(f"{i['book_name']:20s}{i['author']:15s}{i['book_id']:5}{i['quantity']:5}")
                        break
                input()



            elif op_1 == 5:
                os.system('cls')
                while True:
                    os.system('cls')
                    try:
                        op_5 = int(input("1.Add Admin\n2.Approve student request\n2.Add student\n3.Exit"))
                        if op_5 == 1:
                            os.system('cls')
                            ad_name = input("Enter name:")
                            ad_pass = int(input("enter password:"))
                            ad_id = ('a'+str(100 + len(admin_list) + 1))
                            print("Your ID:",ad_id)
                            admin_list.append({'name': ad_name, 'ad_id': ad_id, 'ad_pass': ad_pass})
                            input("Admin Added")

                        elif op_5 == 3:
                            c = False
                            for l in student_list:
                                if l['status'] == 'wait':
                                    c = True
                            if c:
                                print("Student name\t\tStatus\t\tstudent id")
                                print("-"*20)
                                for l in student_list:
                                    if l['status'] == 'wait':
                                        print(l['name'],'\t\t',i['status'],'\t\t',i['st_id'])
                                ap_id = input(("Enter student id to approve or '0' to exit"))
                                if ap_id == '0':
                                    break
                                elif ap_id != '0':
                                    for l in student_list:
                                        if l['st_id'] == ap_id and l['status'] == 'wait':
                                            l['status'] = 'approved'
                                            input("Student request approved")
                                            break

                            elif c == False:
                                input("No request")
                                break

                        elif op_5 == 3:

                            os.system('cls')
                            st_name = input("Enter name:")
                            st_pass = int(input("enter password:"))
                            st_id = ('s'+ str(100 + len(student_list) + 1))
                            print("Your ID:", st_id)
                            student_list.append({'name': st_name, 'st_id': st_id, 'st_pass': st_pass, 'wallet': 1500})
                            input("Student Added")

                        elif op_5 == 4:
                            break

                    except:
                        input("invalidinput")

            elif op_1 == 6:
                os.system('cls')

            elif op_1 == 7:
                os.system('cls')

            elif op_1 ==8:
                os.system('cls')
                input("Thank you")
                break
        except:
            os.system('cls')
            input("Invalid option")
            pass


def student(i):
    os.system('cls')
    print("Student menu")
    while True:
        os.system('cls')
        n = int(input("1.Rent book\n2.Cart\n3.Return book\n4.View fine\n5.Add Amount\n6.Exit"))
        if n == 1:
            while True:
                os.system('cls')
                if books == []:
                    input("No books avilable")
                    break
                elif books != []:
                    print(
                        f"{'Name of book':20s}{gap}{'Bookid':10s}{gap}{'Avilable quantity':20s}{gap}{'status':20s}")
                    print("-" * 50)

                    st = False
                    bo = False
                    for j in books:
                        print(
                            f"{j['book_name']:20s}{gap}{j['book_id']:5}{gap}{j['quantity']:5}{gap}{j['status']:10s}")

                        bk_id = int(input("Enter book ID to add to cart:"))
                        for a in books:
                            if a['book_id'] == bk_id:
                                if cart == []:
                                    if a['quantity'] > 0 and a['status'] == 'available':
                                        if i['wallet'] >= 500:
                                            cart.append(
                                                {'st_name': i['name'], 'st_id': i['st_id'], 'book_id': a['book_id'],
                                                 'book_name': a['book_name'],
                                                 'quantity': 1, 'status': a['status']})
                                            input("Book added to cart!!!")
                                            break
                                        elif i['wallet'] < 500:
                                            input("Low account balance")
                                    elif a['quantity'] == 0:
                                        input("All books rented!!")
                                        break

                                elif cart != []:
                                    for t in cart:
                                        if t['st_id'] == i[st_id]:
                                            st = True
                                            break

                                if st:
                                    for t in cart:
                                        if t['st_id'] == i[st_id] and t['book_id'] == bk_id and t['status'] == "available":
                                            bo = True
                                            break
                                elif st == False:
                                    if a['quantity'] > 0 and a['status'] == 'available':
                                        if i['wallet'] >= 500:
                                            cart.append(
                                                {'st_name': i['name'], 'st_id': i['st_id'], 'book_id': a['book_id'],
                                                 'book_name': a['book_name'],
                                                 'quantity': 1, 'status': a['status']})
                                            input("Book added to cart!!!")
                                            break
                                        elif i['wallet'] < 500:
                                            input("Low account balance")
                                    elif a['quantity'] == 0:
                                        input("All books rented!!")
                                        break

                                if bo:
                                    input("This book has been already in cart")
                                    break
                                elif bo == False:
                                    if a['quantity'] > 0 and a['status'] == 'available':
                                        if i['wallet'] >= 500:
                                            cart.append(
                                                {'st_name': i['name'], 'st_id': i['st_id'], 'book_id': a['book_id'],
                                                 'book_name': a['book_name'],
                                                 'quantity': 1, 'status': a['status']})
                                            input("Book added to cart!!!")
                                            break
                                        elif i['wallet'] < 500:
                                            input("Low account balance")
                                    elif a['quantity'] == 0:
                                        input("All books rented!!")
                                        break

                break

        elif n == 2:
            os.system('cls')
            if cart == []:
                input("no book in cart")
                pass
            elif cart != []:
                print("BOOK NAME\t\tQuantity")
                while True:
                    v = False
                    for j in cart:
                        if j['st_id'] == i['st_id']:
                            v = True
                    if v:
                        for h in cart:
                            if h['st_id'] == i[st_id]:
                                print(h['book_name'], '\t\t', h['quantity'])
                        op_2 = int(input("1.Rent\n2.Remove book\n3.Exit"))
                        if op_2 == 1:
                            os.system('cls')
                            for l in cart:
                                if l['st_id'] == i['st_id'] and l['status'] == 'available':
                                    ren = l
                                    ren['status'] = "rented"

                                    cart.remove(l)
                                    cart.append(
                                        {'st_name': i['name'], 'st_id': i['st_id'], 'book_id': ren['book_id'],
                                         'book_name': ren['book_name'],
                                         'quantity': 1, 'status': ren['status'], 'rent_date': [2022, 1, 12]})

                                    input("Book rented!!!")
                                    for h in books:
                                        if h['book_id'] == ren['book_id']:
                                            h['quantity'] -= 1
                                            break


                        elif op_2 == 2:
                            os.system('cls')
                            for h in books:
                                print(h['book_name'], '\t\t', h['quantity'])
                            op_3 = int(input("Enter book id to remove:"))
                            for h in cart:
                                if h['st_id'] == i['st_id'] and h['book_id'] == op_3:
                                    cart.remove(h)
                                    input("Book removed from cart!!!")
                                    break

                        elif op_2 == 3:
                            break
                    elif v == False:
                        input("No book in cart!!!")
                        break

        elif n == 3:
            os.system('cls')
            for h in cart:
                if h['st_id'] == i['st_id'] and h['status'] == "rented":
                    print()




        elif n == 4:
            os.system('cls')

        elif n == 5:
            os.system('cls')
            amt = int(input("Enter amonut to add:"))
            i['wallet'] += amt
            input("Amount aded succesfully!!!")




        elif n == 6:
            os.system('cls')
            break








while True:
    os.system('cls')
    print("library")
    os.system('cls')
    op = int(input("1.Admin\n2.Student\n3.Exit\nEnter your option:"))
    if op == 1:
        while True:

            ad_id = (input("Enter ADMIN id:"))
            ad_pass = int(input("Enter AMDIN password:"))
            for i in admin_list:
                if i['ad_id'] == ad_id and i['ad_pass'] == ad_pass:
                    input("Login Succesfull")
                    admin(book_id)
                    book_id += 1
                    break
            break


    elif op == 2:
        os.system('cls')
        while True:
            os.system('cls')
            print("Student Menu")
            op_1 = int(input("1.New Student\n2.Exiisting Student\n3.exit"))
            if op_1 == 1:
                os.system('cls')
                st_name = input("Enter name:")
                st_pass = int(input("enter password:"))
                st_id = ('s' + str(100 + len(student_list) + 1))
                student_list.append(
                    {'name': st_name, 'st_id': st_id, 'st_pass': st_pass, 'wallet': 1500, 'status': 'wait'})
                input("Account Created")

            elif op_1 == 2:
                os.system('cls')
                try:
                    st_id = (input("Enter student id:"))
                    st_pass = int(input("Enter password:"))
                    for i in student_list:
                        if i['st_id'] == st_id and i['st_pass'] == st_pass:
                            if i['status'] == 'approved':
                                student(i)
                                break
                            elif i['status'] == 'wait':
                                input("Wait for admin approval!!!")
                                break
                    else:
                        input("No student found")
                except:
                    input("Invalid input")

            elif op_1 == 3:
                break

    elif op == 3:
        input('Thnak You')
        break
