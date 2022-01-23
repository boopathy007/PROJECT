import os
from operator import  itemgetter as it
import datetime
book_id = 100
gap = " "*3
rent_history,book_cart,books,rent_list= [],[],[],[]

fine_history = []
student_list =[{'name': "boopathy", 'st_id':"s101" , 'st_pass': 123, 'wallet':1500,'status':"approved",'fine':0}]
admin_list = [{'name':'boopathy','ad_id':'a101','ad_pass':123}]

def renbook(i,bk_id):
    for j in books:
        if j['book_id'] == bk_id and j['status'] == 'available':
            if j['quantity'] > 0 :
                if i['wallet'] >= 500:
                    rent_date = datetime.date.today()
                    delta = datetime.timedelta(days=15)
                    due_date = (rent_date + delta)
                    rent_list.append(
                        {'book_id': j['book_id'],'due_date':due_date,'due_days':15 ,'cost': j['cost'], 'st_id': i['st_id'], 'fine': 0, 'reason': 'book issued',
                         'book_name': j['book_name'], 'quantity': 1, 'rent_date': rent_date, 'return_date': '','extend_date':2})
                    rent_history.append(
                        {'book_id': j['book_id'], 'cost': j['cost'], 'due_days':15,'due_date':due_date ,'st_id': i['st_id'], 'fine': 0, 'reason': 'book issued',
                         'book_name': j['book_name'], 'quantity': 1, 'rent_date': rent_date, 'return_date': '','extend_date':2})
                    print(j['book_name'], 'has been rented')
                    print("Issue date:",rent_date)
                    print("Due date:",due_date)

                    j['quantity'] -= 1
                    if j['quantity'] == 0:
                        j['status'] = 'rented'
                    input()
                    break
                elif i['wallet'] < 500:
                    input("You can rent a book!!! Your account balance is low")


            elif j['quantity'] == 0 or j['status'] == 'rented':
                input("All book rented!!!")
                break
        elif j['book_id'] == bk_id and j['status'] and j['status'] == 'rented':
            input("All book rented!!!")
            break

def admin(book_id):
    os.system('cls')
    while True:

        os.system('cls')
        print("-" * 20)
        print("".ljust(5),"ADMIN MENU")
        print("-" * 20)
        print('1.Add book\n2.Modify book\n3.View all book\n4.Search book\n5.Add admin or student\n6.Book issue history\n8.Exit')
        op_1 = int(input("\nEnter your option:"))
        if op_1 == 1:
            os.system('cls')
            print("-"*20)
            print("".ljust(5),"ADD BOOKS")
            print("-"*20)
            book_id += 1
            os.system('cls')

            book_name = input("Enter book name:")
            book_author = input("Enter book auhtor name:")
            cost_book = int(input("Cost of book:"))
            quantity = int(input("Enter quantity:"))
            books.append({'book_name': book_name, 'author': book_author, 'cost': cost_book, 'book_id': book_id,
                          'quantity': quantity, 'status': 'available'})
            print("-" * 20)
            print("Book added to list succefully")
            print("-" * 20)
            input()

        elif op_1 == 2:
            os.system('cls')
            print("-" * 100)
            print("".ljust(30),"BOOK DETAILS MODIFY")
            print("-" * 100)

            while True:
                os.system('cls')

                books.sort(key= it('book_id'))
                print('Name of book'.ljust(30),'Author Name'.ljust(15),'BookId'.ljust(10),'Avilable Quantity'.ljust(25),'Price'.ljust(10))
                print("-" * 100)
                for i in books:
                    print(i['book_name'].ljust(30),i['author'].ljust(15),str(i['book_id']).ljust(10),str(i['quantity']).ljust(25),str(i['cost']).ljust(10))
                print("-" * 100)
                op_2 = int(input("\nEnter book id to modify or '0' to exit:"))
                if op_2 == 0:
                    break

                elif op_2 != 0:


                    for i in books:
                        if op_2 == i['book_id']:

                            op_3 = int(input(
                                "1.Add quantity\n2.Remove quantity\n3.Change price\n4.Remove book\nEnter option"))
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
                                    books.remove(i)
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
        elif op_1 == 3:

            os.system('cls')
            print("".ljust(30),"BOOK MENU")
            print("-"*100)
            print('Name of book'.ljust(30),'Author Name'.ljust(20),'Bookid'.ljust(10),'Avilable quantity'.ljust(25),'status'.ljust(15))
            print("-" * 100)

            b = books
            b.sort(key=it('book_name'))
            for y in b:
                print(y['book_name'].ljust(30),y['author'].ljust(20),str(y['book_id']).ljust(10),str(y['quantity']).ljust(25),y['status'].ljust(15))
            input()
        elif op_1 == 4:
            os.system('cls')
            print("-" * 100)
            print("".ljust(30),"SEARCH BOOK")
            print("-" * 100)
            g = False
            op_4 = int(input("\nEnter book id:"))
            os.system('cls')
            for i in books:
                if op_4 == i['book_id']:
                    os.system('cls')
                    print("-" * 100)
                    print("".ljust(35),"BOOK DETAILS")
                    print("-" * 100)
                    print('Name of book'.ljust(30),'Author Name'.ljust(15),'Bookid'.ljust(10),'Avilable quantity'.ljust(25))
                    print("-" * 100)
                    print(i['book_name'].ljust(30),i['author'].ljust(15),str(i['book_id']).ljust(10),str(i['quantity']).ljust(25))
                    break
            for i in rent_list:
                if i['book_id'] == op_4:
                    g = True
            print("\n")
            print("-" * 100)
            print("".ljust(35),"CURRENT ISSUE HISTORY")
            print("-"*100)
            if g:
                print('Student ID'.ljust(15),'Book Name'.ljust(30),'Issue Date'.ljust(15),'Due Date'.ljust(15),'Retrun Date'.ljust(20))
                print("-" * 100)
                for i in rent_list:
                    if i['book_id'] == op_4:
                        print(i['st_id'].ljust(15),i['book_name'].ljust(30),str(i['rent_date']).ljust(30),str(i['due_date']).ljust(30),str(i['return_date']).ljust(30))

            elif g == False:
                print("".ljust(35),"*"*10,"NO ISSUE","*"*10)

            print("\n")
            print("-" * 100)
            print("".ljust(40),"PREVIOUS ISSUE HISTORY")
            print("-" * 100)
            o = False
            for i in rent_history:
                if i['book_id'] == op_4:
                    o = True
            if o:
                print('Student ID'.ljust(15),'Book Name'.ljust(30),'Issue Date'.ljust(15),'Due Date'.ljust(15),
                      'Retrun Date'.ljust(15),'Fine'.ljust(10),'Reason'.ljust(30))
                print("-" * 100)
                for i in rent_history:
                    if i['book_id'] == op_4:
                        print(i['st_id'].ljust(15),i['book_name'].ljust(30),str(i['rent_date']).ljust(15),str(i['due_date']).ljust(30),
                        str(i['return_date']).ljust(15),str(i['fine']).ljust(10),i['reason'].ljust(30))

            elif o == False:
                print("".ljust(35),"*"*10,'NO ISSUE','*'*10)

            input("\nPress enter to contiue")

        elif op_1 == 5:
            os.system('cls')
            while True:
                os.system('cls')
                print("-" * 20)
                print("".ljust(5),"ADMIN MENU")
                print("-" * 20)
                op_5 = int(input("1.Add Admin\n2.Approve student request\n3.Add student\n4.Exit\n.Enter option"))
                if op_5 == 1:
                    os.system('cls')
                    print("-" * 20)
                    print("NEW ADMIN".ljust(8))
                    print("-" * 20)
                    ad_name = input("Enter name:")
                    ad_pass = int(input("enter password:"))
                    ad_id = ('a' + str(100 + len(admin_list) + 1))
                    print("Your ID:", ad_id)
                    admin_list.append({'name': ad_name, 'ad_id': ad_id, 'ad_pass': ad_pass})
                    input("Admin Added")

                elif op_5 == 2:
                    c = False
                    for l in student_list:
                        if l['status'] == 'wait':
                            c = True
                    if c:
                        os.system('cls')
                        print("-" * 50)
                        print("Student Approve List")
                        print("-"*50)
                        print('Student name'.ljust(15),'Status'.ljust(15),'student id'.ljust(15))
                        print("-" *50)
                        for l in student_list:
                            if l['status'] == 'wait':
                                print(l['name'].ljust(30), l['status'].ljust(15),l['st_id'].ljust(15))
                        ap_id = input(("\nEnter student id to approve or '0' to exit"))
                        if ap_id == '0':
                            break
                        elif ap_id != '0':
                            for l in student_list:
                                if l['st_id'] == ap_id and l['status'] == 'wait':
                                    l['status'] = 'approved'
                                    input("\nStudent request approved")
                                    break

                    elif c == False:
                        print("Student Approve List")
                        print("-" * 50)
                        print(str('*'*5,"No request",'*'*5).ljust(10))
                        input()

                        break

                elif op_5 == 3:

                    os.system('cls')
                    st_name = input("Enter name:")
                    st_pass = int(input("enter password:"))
                    st_id = ('s' + str(100 + len(student_list) + 1))
                    print("Your ID:", st_id)
                    student_list.append({'name': st_name, 'st_id': st_id, 'st_pass': st_pass,'fine':0,'wallet': 1500,'status':"apparoved"})
                    input("Student Added")

                elif op_5 == 4:
                    break

        elif op_1 == 6:
            os.system('cls')
            a = []
            print("-" * 110)
            print("".ljust(35),"BOOK ISSUE HISTORY")
            print("-"*110)
            print('Student ID'.ljust(15),'Book Name'.ljust(15),'Issue Date'.ljust(15),'Due Date'.ljust(15),'Retrun Date'.ljust(15),'Fine'.ljust(15),'Reason'.ljust(15))
            print("-" *110)
            if rent_history == []:
                print("No issue history!!!")
            elif rent_history != []:
                for i in rent_history:

                    print(i['st_id'].ljust(15),i['book_name'].ljust(15),str(i['rent_date']).ljust(15),str(i['due_date']).ljust(15),str(i['return_date']).ljust(15),str(i['fine']).ljust(15),i['reason'].ljust(15))


            input("\npress enter to contiue")

        elif op_1 == 8:
            os.system('cls')
            input("Thank you")
            break


def student(i,books):
    os.system('cls')
    print("-" * 40)
    print("".ljust(15),"STUDENT MENU")
    print("-"*40)
    while True:
        os.system('cls')
        n = int(input("1.Book Menu\n2.Cart\n3.Return book\n4.View fine\n5.Add Amount\n6.Extend Return time\n7.Exit\nEnter option:"))
        if n == 1:
            os.system('cls')
            while True:

                os.system('cls')
                if books == []:
                    print("".ljust(35),"BOOK MENU")
                    print("-" * 90)
                    input(str("*"*5,"NO BOOK AVAILABLE","*"*5).ljust(30))
                    print("-" * 90)
                    break
                elif books != []:
                    os.system('cls')
                    print("-" * 90)
                    print("".ljust(35),"BOOK MENU")
                    print("-"*90)
                    print('Name of book'.ljust(30),'BookId'.ljust(10),'Avilable Quantity'.ljust(30),'Status'.ljust(15))
                    print("-" * 90)
                    km = 1
                    for j in books:
                        print(km,'.',j['book_name'].ljust(30),str(j['book_id']).ljust(10),str(j['quantity']).ljust(30),j['status'].ljust(15))
                        km += 1
                    print("-" * 90)
                    bk_id = int(input("\nEnter book ID to rent or '0' to exit:"))
                    if bk_id == 0:
                        break
                    elif bk_id != 0:
                        if book_cart == []:
                            for l in books:
                                if l['book_id'] == bk_id and l['quantity'] >= 1:
                                    if rent_list == []:
                                        book_cart.append(
                                        {'book_id': l['book_id'], 'book_name': l['book_name'],
                                        'cost': l['cost'],
                                        'st_id': i['st_id']})
                                        input("Book Added to Cart")
                                        break
                                elif l['quantity'] == 0:
                                    input("All book rented")



                        elif book_cart != []:
                            count = 0
                            for h in book_cart:
                                if h['st_id'] == i['st_id']:
                                    count += 1
                            if count < 3:
                                for l in books:
                                    if l['book_id'] == bk_id:
                                        g = False
                                        for h in book_cart:
                                            if h['st_id'] == i['st_id'] and h['book_id'] == bk_id:
                                                g = True
                                                break
                                        if g:
                                            input("You have this book in your cart!!!")
                                            break
                                        elif g == False:
                                            if rent_list == []:
                                                if l['status'] == 'available' and l['quantity'] > 0:
                                                    book_cart.append(
                                                    {'book_id': l['book_id'], 'book_name': l['book_name'],
                                                     'cost': l['cost'],
                                                     'st_id': i['st_id']})
                                                    input("Book Added to Cart")



                                            elif rent_list != []:
                                                for hj in rent_list:
                                                    if hj['book_id'] == bk_id:
                                                        input("You have issued this book!!")
                                                        break


                                    elif l['status'] == 'rented' or l['quantity'] == 0:
                                        input('book rented!!')
                            elif count == 3:
                                input("You have 3 book in your cart!!!!")
                                break

        if n == 2:
            os.system('cls')
            if book_cart == []:
                print("-" * 45)
                print("".ljust(10),"BOOK CART")
                print("-" * 45)
                print("".ljust(8),"*" * 5, "NO BOOKS IN CART", "*" * 5)
                input()
            elif book_cart != []:
                nj = False
                for kl in book_cart:
                    if kl['st_id'] == i['st_id']:
                        nj = True
                if nj == False:
                    os.system('cls')
                    print("-" * 45)
                    print("".ljust(15),"BOOK CART")
                    print("-" * 45)
                    print(str("*"*5,"NO BOOKS IN CART","*"*5).ljust(15))
                    input()
                elif nj == True:
                    os.system('cls')
                    while True:
                        os.system('cls')
                        print("".ljust(15),"BOOK CART")
                        print("-" * 45)
                        print("STUDENT ID".ljust(15), "BOOK NAME".ljust(15), "BOOK ID".ljust(10), )
                        print("-" * 45)

                        c = False
                        for j in book_cart:
                            if i['st_id'] == j['st_id']:
                                c = True
                        if c:
                            for j in book_cart:
                                if i['st_id'] == j['st_id']:
                                    print(j['st_id'].ljust(15), j['book_name'].ljust(15), str(j['book_id']).ljust(10))
                            print("-" * 45)
                        elif c == False:
                            print("".ljust(8),"*"*5,"NO BOOKS IN CART","*"*5)
                            input()
                            break

                        jk = int(input("\n1.Issue Book\n2.Remove Book\n3.Exit\nEnter your option:"))
                        if jk == 1:
                            for j in book_cart:
                                if i['st_id'] == j['st_id']:
                                    renbook(i, j['book_id'])
                                    book_cart.remove(j)


                        elif jk == 2:

                            op_2 = int(input("\nEnter book id to remove:"))
                            for j in book_cart:
                                if i['st_id'] == j['st_id'] and j['book_id'] == op_2:
                                    book_cart.remove(j)
                                    input("Book removed from cart!!!")
                                    break

                        elif jk == 3:
                            break

        elif n == 3:
            os.system('cls')
            while True:
                os.system('cls')
                print("-" * 60)
                print("".ljust(20),"STUDENT MENU")
                print("-" * 60)
                b =False
                op_2 = int(input("1.Retrun book\n2.Lost Book\n3.exit\nEnter option:"))

                if op_2 == 1:
                    for k in rent_list:
                        if k['st_id'] == i['st_id']:
                            b = True
                    if b== False:
                        print("-" * 60)
                        print("STUDENT MENU".ljust(15))
                        print("-" * 60)
                        input("No books has been issued".ljust(15))
                        print("-" * 60)
                        input()
                        continue
                    elif b == True:
                        os.system('cls')
                        print("-"*60)

                        print('Name of book'.ljust(15),'Bookid'.ljust(15),'Issue Date'.ljust(15),'Due Date'.ljust(15))
                        print("-"*60)
                        for j in rent_list:
                            if j['st_id'] == i['st_id']:
                                print(j['book_name'].ljust(15),str(j['book_id']).ljust(15),str(j['rent_date']).ljust(15),str(j['due_date']).ljust(15))
                        print("-" * 60)
                        bok_id = int(input("\nEnter Book id to return:"))
                        re_date = input("Enter Date(y/m/d):")
                        temp_re = re_date.split("/")


                        for j in rent_list:
                            if j['st_id'] == i['st_id'] and j['book_id'] == bok_id:
                                re_dt = datetime.date(int(temp_re[0]), int(temp_re[1]), int(temp_re[2]))

                                no_days = (re_dt - j['rent_date']).days

                                if (no_days-1)<= j['due_days']:
                                    for u in books:
                                        if u['book_id'] == bok_id:
                                            u['quantity'] += 1
                                            rent_history.append({'book_id': j['book_id'], 'reason': 'book returned',
                                                                 'book_name': j['book_name'],'due_date':j['due_date'],'due_days':j['due_days'],
                                                                 'cost': j['cost'], 'st_id': i['st_id'], 'fine': 0,
                                                                  'quantity': 1,
                                                                 'rent_date': j['rent_date'],
                                                                 'return_date': re_date})
                                            rent_list.remove(j)

                                            u['status'] = "available"
                                            input("Book Return Succefully!!!!")
                                            break


                                elif (no_days-1) > j['due_days']:
                                    t_fine = 0
                                    fine = 2
                                    c = (no_days - j['due_days'])
                                    if c <= 10:
                                        t_fine += c * 2
                                    elif c > 10:
                                        de = int(c / 10)
                                        for o in range(de):

                                            t_fine += 10 * fine
                                            if (c % 10) <= 10:
                                                t_fine += (c % 10) * (fine + 2)
                                            elif c % 10 > 10:
                                                c = c % 10
                                            fine += 2
                                    d = int(0.8 * j['cost'])
                                    if t_fine <= d:
                                        t_fine = t_fine

                                    elif t_fine > d:
                                        t_fine = d
                                    print("You have to pay", t_fine, 'as a fine for late subbmisiion of book')
                                    pa_fine = int(input("1.Pay by cash\n2.Pay with wallet\nEnter option:"))
                                    if pa_fine == 1:
                                        ca = int(input("Enter amount:"))

                                        for k in books:
                                            if k['book_id'] == j['book_id']:
                                                k['quantity'] += 1
                                                fine_history.append(
                                                    {'st_id': i['st_id'], 'book_name': j['book_name'],
                                                     'book_id': j['book_id'],'due_date':j['due_date'] ,
                                                     'rent_date': j['rent_date'],
                                                     'reason': 'late subbmission', 'return_date': re_date,
                                                     'fine': t_fine})
                                                rent_history.append(
                                                    {'book_id': j['book_id'], 'reason': 'late subbmission',
                                                     'book_name': j['book_name'], 'cost': j['cost'],'due_date':"2022/01/30" ,
                                                     'st_id': i['st_id'],
                                                     'fine': t_fine,
                                                     'rent_date': "2022/01/15", 'return_date': re_date})
                                                input("Fine paid succefully")
                                                rent_list.remove(j)
                                                if k['status'] == 'rented':
                                                    k['status'] = 'available'
                                                break

                                        break

                                    elif pa_fine == 2:

                                        if t_fine <= i['wallet'] :
                                            i['wallet'] -= t_fine
                                            fine_history.append({'st_id': i['st_id'], 'book_id': j['book_id'],'book_name':j['book_name'],
                                                                 'rent_date': j['rent_date'],'due_date':j['due_date'] ,'due_days':j['due_days'],
                                                                 'reason': 'late subbmission', 'return_date': re_date,
                                                                 'fine': t_fine})

                                            rent_history.append(
                                                {'book_id': j['book_id'], 'reason': 'late subbmission',
                                                 'book_name': j['book_name'], 'cost': j['cost'],'due_days':j['due_days'],
                                                 'st_id': i['st_id'], 'fine': t_fine,'due_date':"2022/01/30",
                                                 'book_name': j['book_name'], 'quantity': 1, 'rent_date': "2022/01/15",
                                                 'return_date': re_date})
                                            for k in books:
                                                if k['book_id'] == j['book_id']:
                                                    k['quantity'] += 1
                                                    input("Fine paid succefully")
                                                    rent_list.remove(j)
                                                    if k['status'] == 'rented':
                                                        k['status'] = 'available'
                                                        break

                                            break
                                        elif t_fine > m['wallet']:
                                            input("Wallet amount low!!! Add cash!!")

                                            break


                elif op_2 == 2:
                    os.system('cls')
                    l_bk = int(input("\nEnter lost book ID:"))

                    for j in rent_list:
                        if j['st_id'] == i['st_id'] and j['book_id'] == l_bk :
                            print("Book cost:",j['cost'])
                            pay = int(0.5*j['cost'])
                            print("You have to pay 50% of book amount(",pay,"):")
                            p = int(input("1.Pay by cash\n2.Pay by wallet"))
                            if p== 1:
                                for f in books:
                                    if f['book_id'] == j['book_id']:
                                        rent_history.append({'book_id': j['book_id'], 'reason': 'book lost',
                                                             'book_name': j['book_name'], 'due_date': j['due_date'],
                                                             'due_days': j['due_days'],
                                                             'cost': j['cost'], 'st_id': i['st_id'], 'fine': pay,
                                                             'quantity': 1,
                                                             'rent_date': j['rent_date'],
                                                             'return_date': re_date})
                                        if f['quantity'] == 0:
                                            books.remove(f)
                                            break



                                fine_history.append(
                                    {'st_id': j['st_id'],'due_date':j['due_date'] ,'book_name':j['book_name'] ,'book_id': j['book_id'], 'rent_date': j['rent_date'],
                                     'reason': 'lost book', 'return_date': "-",'due_date':j['due_date'] ,'due_days':j['due_days'],
                                     'fine': pay})
                                rent_list.remove(j)
                                input("Fine paid succefully")
                                break

                            elif p==2:
                                if pay <= i['wallet']:
                                    i['wallet'] -= pay
                                    rent_history.append({'book_id': j['book_id'], 'reason': 'book lost',
                                                         'book_name': j['book_name'], 'due_date': j['due_date'],
                                                         'due_days': j['due_days'],
                                                         'cost': j['cost'], 'st_id': i['st_id'], 'fine': pay,
                                                         'quantity': 1,
                                                         'rent_date': j['rent_date'],
                                                         'return_date': re_date})
                                    fine_history.append(
                                    {'st_id': j['st_id'], 'due_date':j['due_date'] ,'book_name':j['book_name'],'book_id': j['book_id'], 'rent_date': j['rent_date'],
                                     'reason': 'lost book', 'reason': 'lost book', 'return_date': "-",'due_date':"30/1/2022",'due_days':j['due_days'] ,
                                     'fine': pay})
                                    rent_list.remove(j)
                                    input("Fine paid succefully")
                                    break
                                elif pay > i['wallet']:
                                    input("Wallet balance low!!!")
                                    break


                elif op_2 == 3:
                    os.system('cls')
                    break

        elif n == 4:
            os.system('cls')
            b = False
            print("-" * 130)
            print("".ljust(60),"FINES")
            print("-" * 130)
            print('Student ID'.ljust(15),'Book Name'.ljust(15),'Issue Date'.ljust(15),'Due Date'.ljust(15),'Retrun Date'.ljust(15),'Fine'.ljust(15),' Reason'.ljust(15))
            print("-" * 100)
            for d in fine_history:
                if d['st_id'] == i['st_id']:
                    b = True
            if b:
                for d in fine_history:
                    if d['st_id'] == i['st_id']:
                        print(d['st_id'].ljust(15),d['book_name'].ljust(15),str(d['rent_date']).rjust(15),str(d['due_date']).rjust(15),str(d['return_date']).rjust(15),
                              str(d['fine']).ljust(15),d['reason'].ljust(15))
                print("-" * 100)
                input("\nPress enter to continue".ljust(60))

            elif b== False:
                input("No fine history")

        elif n == 5:
            os.system('cls')
            print("Current Balance:",i['wallet'])
            amt = int(input("Enter amonut to add:"))
            i['wallet'] += amt
            input("Amount aded succesfully!!!")

        elif n == 6:
            os.system('cls')
            for k in rent_list:
                if k['st_id'] == i['st_id']:
                    b = True
            if b == False:
                print("-" * 60)
                print("".ljust(15),"STUDENT MENU")
                print("-" * 60)
                print("".ljust(10),"No books has been issued")
                input()
                continue
            elif b == True:
                os.system('cls')
                print("-" * 80)
                print("".ljust(25),"STUDENT MENU")
                print("-" * 80)


                print('StudentID'.ljust(15),'Name of book'.ljust(15), 'Bookid'.ljust(15), 'Issue Date'.ljust(15), 'Due Date'.ljust(15))
                print("-" * 80)
                for j in rent_list:
                    if j['st_id'] == i['st_id']:
                        print(j['st_id'].ljust(15),j['book_name'].ljust(15), str(j['book_id']).ljust(15), str(j['rent_date']).ljust(15),
                              str(j['due_date']).ljust(15))

                print("-" * 80)
                bok_id = int(input("\nEnter Book id to to extend date:"))

                for j in rent_list:
                    if j['st_id'] == i['st_id'] and j['book_id'] == bok_id:
                        if j['extend_date'] == 0:
                            input("\nYou have reched maxinum number extend limit!!!")
                            print('Return the book on:',j['due_date'])
                            input("Press enter to contiue")
                            break
                        elif j['extend_date'] != 0:

                            re = j['due_date']
                            j['due_date'] = (j['due_date'] + datetime.timedelta(days=15))
                            print("\nReturn date extend from ",re,' to ',j['due_date'])
                            j['extend_date'] -= 1
                            j['due_days'] += 15
                            input("Press enter to contiue")
                            break

        elif n == 7:
            os.system('cls')
            break



while True:
    os.system('cls')

    print("-"*20)
    print("".ljust(5),"LIBRARY")
    print("-" * 20)
    op = int(input("1.Admin\n2.Student\n3.Exit\nEnter your option:"))
    if op == 1:
        while True:
            os.system('cls')
            print("-" * 20)
            print("".ljust(5),"ADMIN LOGIN")
            print("-" * 20)
            ad_id = (input("Enter ADMIN id:"))
            ad_pass = int(input("Enter AMDIN password:"))
            for i in admin_list:
                if i['ad_id'] == ad_id and i['ad_pass'] == ad_pass:
                    input("\nLogin Succesfull")
                    admin(book_id)
                    book_id += 1
                    break
            break


    elif op == 2:
        os.system('cls')
        while True:
            os.system('cls')
            print("-" * 20)
            print("".ljust(5),"STUDENT LOGIN".ljust(8))
            print("-" * 20)
            op_1 = int(input("1.New Student\n2.Exiisting Student\n3.exit\nEnter option:"))
            if op_1 == 1:
                os.system('cls')
                print("-" * 20)
                print("".ljust(2),"NEW STUDENT LOGIN")
                print("-" * 20)
                st_name = input("Enter name:")
                st_pass = int(input("enter password:"))
                st_id = ('s' + str(100 + len(student_list) + 1))
                print("Your student id:",st_id)
                student_list.append(
                    {'name': st_name, 'st_id': st_id, 'st_pass': st_pass, 'wallet': 1500, 'status': 'wait'})
                input("Account Created")

            elif op_1 == 2:
                os.system('cls')
                print("-" * 20)
                print("".ljust(5),"STUDENT LOGIN")
                print("-" * 20)
                st_id = (input("Enter student id:"))
                st_pass = int(input("Enter password:"))
                for i in student_list:
                    if i['st_id'] == st_id and i['st_pass'] == st_pass:
                        if i['status'] == 'approved':
                            input("\nLogin succesfull!!")
                            student(i,books)
                            break
                        elif i['status'] == 'wait':
                            print("-" * 20)
                            print("STUDENT LOGIN".ljust(8))
                            print("-" * 20)

                            input("Wait for admin approval!!!")
                            break
                else:
                    print("-" * 20)
                    print("STUDENT LOGIN".ljust(8))
                    print("-" * 20)
                    input("No student found".ljust(4))
                    print("-" * 20)

            elif op_1 == 3:
                break

    elif op == 3:
        print('*'*5,'Thank You','*'*5)
        break



