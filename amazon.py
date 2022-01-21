import os
import time



cart = []

order = []

merchat_pro_selled=[]

catagory = {'mobiles','fashion','electronics'}

customer = [{'name':'boopathy','password':1234,'id':'c101','wallet':1000000},
            {'name':'harish','password':1234,'id':'c102','wallet':10000000}]

vendor = [{'username':'vignesh','password':1234,'status':'approved','id':'m110'},
          {'username':'vetri','password':1234,'status':'approved','id':'m111'},
          {'username':'mani','password':1234,'status':'approved','id':'m112'},
          {'username':'tamil','password':1234,'status':'approved','id':'m113'},
          {'username':'kathir','password':1234,'status':'approved','id':'m114'}
          ]

product = [{'id':'m110','catagory':'mobiles','name':'iqoo','spec':['ROM: 128GB','RAM: 4GB','COLOUR : BLUE','SIM : Dual SIM'],'price':27000,'quantity':5},
           {'id':'m110','catagory':'fashion','name':'shoe','spec':['Colour: black','size: 7 - 9','Material Type: Synthetic','Heal Type: Flat'],'price':700,'quantity':20},
           {'id':'m110','catagory':'electronics','name':'airpods','spec':['Ear placement : In Ear','Colour : Black','Weigth : 50grm'],'price':2500,'quantity':20},
           {'id':'m111','catagory':'mobiles','name':'redmi','spec':['ROM: 64GB','RAM: 8GB','COLOUR : BLACK','SIM : Dual SIM'],'price':19000,'quantity':5},
           {'id':'m111','catagory':'fashion','name':'shampoo','spec':['Liquid Volume : 800ml','Product Benefits : Anti hair loss,Anti-drandruff'],'price':450,'quantity':10},
           {'id':'m111','catagory':'electronics','name':'laptop','spec':['CPU : AMD processor','OS : windows 11','Colour : Silver'],'price':42000,'quantity':10},
           {'id':'m112','catagory':'mobiles','name':'samsung','spec':['ROM: 128GB','RAM: 4GB','COLOUR : BLUE','SIM : Dual SIM'],'price':12000,'quantity':5},
           {'id':'m112','catagory':'fashion','name':'puma','spec':['Fabric composition : 60% cotton','Relaxe Fit'],'price':1500,'quantity':10},
           {'id':'m113','catagory':'electronics','name':'printer','spec':['Connector : App,wifi,USB','Sheet size : A4,B5,A6,DL'],'price':15000,'quantity':10},
           {'id':'m113','catagory':'mobiles','name':'apple','spec':['ROM: 128GB','RAM: 4GB','COLOUR : BLUE','SIM : Dual SIM'],'price':1500000,'quantity':5},
           {'id':'m113','catagory':'electronics','name':'camara','spec':['Connectivity Type : Wireless','Room Type : Offie,Garage,Kitchen'],'price':3000,'quantity':20},
           {'id':'m114','catagory':'fashion','name':'trimmer','spec':['Colour : Silver','Material : Metal','Size : 1mm - 5mm'],'price':2000,'quantity':10}
           ]

order = []

def admin():

    while True:
        os.system('cls')
        print("   Welcome to Admin menu   ")
        print("---------------------------")

        ad_op = int(input("1.Add/Remove Merchant\n2.Approve Merchent Request\n3.Veiw merchent list\n4.Exit\nEnter the option:"))

        if ad_op == 1:
            os.system('cls')
            print("    Merchent Review Menu     ")
            print("-----------------------------")
            
            try:
                a_r_op = int(input("\n1.Add Merchent\n2.Remove Merchent\n3.Exit\nEnter the option:"))
            
                if a_r_op == 1:
                    os.system('cls')
                    new_merch('approved')
                    print("Merchant added succesfull")
                
                elif a_r_op == 2:
                    os.system("cls")
                    if len(vendor) == 0:
                        input("No merchant!press 'enter' to continue")
                    else:
                        print("      Merchent list    ")
                        print("-----------------------")
                        for i in range(len(vendor)):
                            print((i+1),'.Name:',vendor[i]['username'],'\n  Merchent ID:',vendor[i]['id'],sep="")
                        r_id = (input('Enter merchent ID to remove:'))
                        for i in vendor:
                            if i['id'] == r_id:
                                vendor.remove(i)
                                print(r_id,"merchant has been removed from factory")
                                if vendor == []:
                                    input("No more vendor left!! Press enter to continue")
                                    break
                                else:
                                    op_1 = int(input("Do you want to remove more merchant\n1.Yes\n2.No"))
                                    if op_1 == 1:
                                        pass
                                    elif op_1 == 2:
                                        break

                        input("\npress 'enter' to continue")
                

                elif a_r_op == 3:
                    os.system('cls')
                    input("Thank you!!")
                    break
            except:
                os.system('cls')
                print("Wrong Option")
                input("press 'ENTER' to continue")
                
        elif ad_op == 2:
            os.system('cls')
            z = 0
            print(" Merchent Request Menu")
            print("-----------------------")
            if len(vendor) == 0:
                input("No merchent!!! press enter to continue")
            elif len(vendor)>=1:
                for i in vendor:
                    if i['status'] == 'pending':
                        z += 1
                if z == 0:
                    input("No Vendor.press 'ENTER' to contibue")
                else:
                    for i in vendor:
                        os.system('cls')
                        print(" Merchent Request Menu")
                        print("-----------------------")

                        if i['status'] == 'pending':
                            print("\nMerchent name:",i['username'])
                            n= int(input("Type 1 to Approve\nType 2 to Reject\nEnter option:"))
                            if n == 1:
                                i['status'] = 'approved'
                                print("merchant",i['username'],"request has been approved")
                                input()
                            elif n == 2:
                                i['status'] = 'rejected'
                                print("merchant",i['username'],"request has been rejected ")
                                input()
        elif ad_op == 3:
            os.system('cls')
            if vendor == []:
                input("No Merchent!press enter to continue")
            else:
                print("Merchent List")
                for i in range(len(vendor)):
                    print((i + 1), '.', vendor[i]['username'], sep="")
                input("Press 'Enter' to continue")


        elif ad_op == 4:
            os.system('cls')
            input("    ThankYou!")
            break

def new_merch(status ='pending'):
    os.system('cls')
    id = 'm' + str(100 + len(vendor))
    while True:
        os.system('cls')
        print("New Merchent Registration")
        new_mer_name = input("Enter name:")
        print("Your Merchat ID: ",id)
        print("(Note your merchant id for further access)")

        new_mer_pass = int(input("Create Password:",))
        con_pass = int(input("Confirm Your Password:"))
        if con_pass == new_mer_pass:
            vendor.append({'username':new_mer_name,'password':new_mer_pass,'status':status,'id':id})

            if status == 'pending':
                print('\n',new_mer_name,"your request has been submitted.Wait for admin approval")
            elif status == 'approved':
                print('\n',new_mer_name,'has been registered as an merchent')
            input("\nPress enter to continue")
            break
        elif con_pass != new_mer_pass:
            os.system('cls')
            input("Password didn't matched!! Try again !! \n Press enter to continue")

def merchent(product):

    while True:
        os.system('cls')
        try:
            mer_op = int(input("\tMerchent Menu\n1.New Merchent\n2.Existing Merchent\n3.Exit\nEnter the option:"))
        except:
            input("Wrong Option")

        if mer_op == 1:
            os.system('cls')
            new_merch()

        elif mer_op == 2:
            os.system('cls')
            print("   Merchent Menu   ")
            print("-------------------")
            try:
                u_id = input("Enter Merchent ID:")
                u_pass = int(input("Enter password:"))
            except:
                os.system('cls')
                print("Wrong Input")
                input("press Enter to continue")
            for i in vendor:

                if u_id == i['id'] and u_pass == i['password']:

                    if i['status'] == 'rejected':
                        input("Your Account has been disabled.Contact admin\npress enter to continue")
                        break

                    elif i['status'] == 'pending':
                        input("Your account is not approved yet!\npress enter to continue")
                        break

                    elif i['status'] == 'approved':
                        while True:
                            os.system('cls')
                            print("     Welcome to Merchent Menu     ")
                            print("----------------------------------")
                            print("1.Add product\n2.Remove Product\n3.Statictics\n4.Exit")

                            mer_menu_op = int(input("Enter Your Choice:"))
                            if mer_menu_op == 1:
                                mer_add_pro(i)
                            elif mer_menu_op == 2:
                                mer_rem_pro(i)
                            elif mer_menu_op == 3:
                                mer_statics(i,product)

                            elif mer_menu_op == 4:
                                os.system('cls')
                                print("\tThank You")
                                input(("\nPress 'ENTER' to Exit"))
                                break
                        break




        elif mer_op == 3:
            break

def mer_add_pro(i):
    os.system('cls')
    while True:
        os.system('cls')
        print("   Load Stock  ")
        print("---------------")
        mer_id = i['id']
        try:
            pro_cat = input("Type the catagory of product\n1.Mobiles\n2.Fashion\n3.Electronics\nType the catagory:").lower()
            if pro_cat in catagory:
                pro_name = input("Name of the product: ")
                pro_price = int(input("Price of product:"))

                pro_quant = int(input("Quantity of the product:"))

                pro_spc = input("Specification of product(use '-' to print in next line):").split("-")

                product.append({'id':mer_id,'catagory':pro_cat,'name':pro_name,'spec':pro_spc,'price':pro_price,'quantity':pro_quant})
                print(pro_name,'has been succefully added to your',pro_cat,'list')
                input("Press enter to continue")

                os.system('cls')

                mor_pro = int(input("\nWant to add more products\n1.yes\n2.no\nEnter option:"))

                if mor_pro == 1:
                    os.system('cls')
                    pass
                elif mor_pro == 2:
                    os.system('cls')
                    input("Thank You!!\nPress enter to continue")
                    break

            elif pro_cat not in catagory:
                input("Wrong Catagory!! press enter to continue")

        except:
            input('Wrong option!! Press enter to continue')

def mer_rem_pro(i):
    os.system('cls')
    mer_id = i
    while True:
        ok = False
        os.system('cls')
        for j in product:
            if j['id'] == i['id']:
                ok = True
        if ok:
            print("Product Remove Menu")
            print("-------------------")
            cat = ''
            print("Catogory of your products")
            co = 0
            for j in range(len(product)):
                if product[j]['id'] == mer_id['id']:
                    if product[j]['catagory'] not in cat:
                        co += 1
                        cat += product[j]['catagory']
                        print((co),'.',product[j]['catagory'])
            try:
                n = input("Type the catagory or '0' to exit:").lower()
                if n == '0':
                    break
                else:
                    if n in catagory:
                        co = 0
                        cat = ''
                        os.system('cls')
                        print("List of products in",n,'catagory')
                        for j in range(len(product)):
                            if product[j]['id'] == mer_id['id']:
                                if product[j]['catagory'] == n and n not in cat:

                                    co += 1
                                    print(co,'.',product[j]['name'])
                        try:
                            po_op = input("Enter the name of the product:")
                            for j in range(len(product)):
                                if product[j]['id'] == mer_id['id']:
                                    if product[j]['name'] == po_op:
                                        if product[j]['quantity'] == 0:
                                            print("There are no product")
                                            print("Do you want to remove this item from the list\n1.yes\n2.No")
                                            re_op = int(input("Enter the option:"))
                                            if re_op == 1:
                                                product.remove(product[j])
                                                print("Product Removed Succefull")

                                                con = int(input("Do you Want to remove more product\n1.Yes\n2.No\nEnter the option:"))
                                                if con == 1:
                                                    pass
                                                elif con == 2:
                                                    break
                                            elif re_op == 2:
                                                pass
                                        elif product[j]['quantity'] > 0:
                                            print('Quantity of',product[j]['name'],'is',product[j]['quantity'])

                                            try:
                                                re = int(input("Enter the quantity of product to remove:"))
                                                product[j]['quantity'] -= re
                                                print("succefully removed")
                                                con = int(input("Do you Want to remove more product\n1.Yes\n2.No\nEnter the option:"))
                                                if con == 1:
                                                    pass
                                                elif con == 2:
                                                    break
                                                print()

                                            except:
                                                input("Wrong Option!! Press ENTER to continue")

                        except:
                            input("Wrong input!!Press Enter to continue")
                    else:
                        input("Wrong Option")

            except:
                input(("Wrong Input!!press entr to continue"))
        else:
            input("No produt avilable!! Add new produts\nPress 'ENTER' to continue")

def mer_statics(i,product):
    os.system('cls')
    while True:
        os.system('cls')
        print("\tMerchant Staticsts Menu")
        sta_op = int(input("1.Product Avilability\n2.Produt Selled\n3.Exit\nEnter the option:"))
        if sta_op == 1:
            co = 0
            print("Product Name             Quantity")
            for j in product:

                if i['id'] == j['id']:
                    co += 1
                    print(co,'.',j['name'],"        ",j['quantity']   )
            g = int(input("1.Add quantity\n2.Remove quantity\n3.Exit"))
            if g == 1:
                p_name = input("enter product name:")
                qt = int(input("Enter Quantity:"))
                for j in product:
                    if j['id'] ==  i['id'] and j['name'] == p_name:
                        j['quantity'] += qt
                        input("Product added")
                        break

            elif g == 2:
                p_name = input("enter product name:")
                qt = int(input("Enter Quantity:"))

                for j in product:
                    if j['id'] == i['id'] and j['name'] == p_name:
                        if qt >= j['quantity']:
                            product.remove(j)
                            input("Produtc removed")
                        elif qt < j['quantity']:
                            j['quantity'] -= qt
                            input("Product removed")
                            break

            elif g== 3:
                break
            input("press enter to continue")
        elif sta_op == 2:

            c= False
            for k in merchat_pro_selled:
                if k['id'] == i['id']:
                    c = True
            if c:
                os.system('cls')
                print(('      product sell report '))
                print("------------------------------")
                print("Name of product            quantity             buyer           paid amount           order number")
                for k in merchat_pro_selled:
                    if k['id'] == i['id']:
                        print(k['name'],'         ',k['quantity'],'          ',k['buyer'],'          ',k['paid'],'       ',k['ord_id'])
                input("Press enter conyinue")
            else:
                input("No products have sold!!!\n press enter to continue")


        elif sta_op  == 3:
            break

def cart_(n,prod,qt):

    cart.append({'cu_id':n['id'],'mer_id':prod['id'],'product':prod['name'],'price':prod['price'],'quantity':qt})

    input('Item added to cart succefully.')
    return


def show_product(n,ord_id):
    os.system('cls')

    while True:

        os.system('cls')
        print("                          AMAZON                            ")
        print("------------------------------------------------------------")

        print("\nShop Product")
        co = 0
        for i in product:
            co += 1
            print(co,'.',i['name'])
        pro = input("Enter the product name to but or '0' to exit :")
        if pro == '0':
            break
        else:
            c = True
            for i in product:
                if pro == i['name']:
                    prod = i
                    os.system('cls')
                    os.system('cls')
                    print("                          AMAZON                            ")
                    print("------------------------------------------------------------")
                    print("Product Name:", i['name'])
                    print("Specification:")
                    for j in i['spec']:
                        print("           ", j)
                    print("Price:", i['price'])
                    print("------------------------------------------------------------")

                    if i['quantity'] == 0:
                        input("Out of stock!! press enter to continue")
                        break

                    elif i['quantity'] > 0:
                        while True:
                            os.system('cls')
                            print("                          AMAZON                            ")
                            print("------------------------------------------------------------")
                            print("Product Name:", i['name'])
                            print("Specification:")
                            for j in i['spec']:
                                print("           ", j)
                            print("Price:", i['price'])
                            print("------------------------------------------------------------")

                            op_1 = int(input(
                                "\n1.Add to cart           2.Buy now      3.Previous Menu\n\nEnter the option:"))
                            if op_1 == 1:
                                if cart != []:
                                    for j in cart:
                                        if n['id'] == j['cu_id'] and i['name'] == j['product'] and j[
                                            'mer_id'] == i['id']:

                                            qt = int(input("Enter quantity to add:"))
                                            if qt > i['quantity']:
                                                print("Only", i['quantity'], 'available')
                                                input("Press enter to continue")
                                                break
                                            elif qt <= i['quantity']:
                                                if (j['quantity'] + qt) > i['quantity']:
                                                    print("Only", i['quantity'], 'available')
                                                    input("Press enter to continue")
                                                    break
                                                elif (j['quantity'] + qt) <= i['quantity']:
                                                    j['quantity'] += qt
                                                    input('Item added to cart succefully.')
                                                    break
                                        elif n['id'] == j['cu_id'] and i['name'] == j['product'] and j[
                                            'mer_id'] != i['id']:
                                            qt = int(input("Enter quantity to add:"))
                                            if qt > i['quantity']:
                                                print("Only", i['quantity'], 'available')
                                                input("Press enter to continue")
                                                break
                                            elif qt <= i['quantity']:

                                                cart.append({'cu_id': n['id'], 'mer_id': prod['id'],
                                                             'product': prod['name'], 'price': prod['price'],
                                                             'quantity': qt})
                                                input("Product added to cart succesfully")
                                                break
                                        elif n['id'] == j['cu_id'] and i['name'] != j['product']:
                                            qt = int(input("Enter quantity to add:"))
                                            if qt > i['quantity']:
                                                print("Only", i['quantity'], 'available')
                                                input("Press enter to continue")
                                                break
                                            elif qt <= i['quantity']:

                                                cart.append({'cu_id': n['id'], 'mer_id': prod['id'],
                                                             'product': prod['name'], 'price': prod['price'],
                                                             'quantity': qt})
                                                input("Prouct added to cart succesfully")
                                                break
                                elif cart == []:
                                    qt = int(input("Enter quantity to add:"))

                                    if qt > i['quantity']:
                                        print("Only", i['quantity'], 'available')
                                        input("Press enter to continue")
                                        break
                                    else:
                                        cart.append(
                                            {'cu_id': n['id'], 'mer_id': prod['id'],
                                             'product': prod['name'],
                                             'price': prod['price'], 'quantity': qt})

                                    input('Item added to cart succefully.')


                            elif op_1 == 2:

                                while True:

                                    qty = int(input("Enter the quatntity:"))

                                    if qty <= i['quantity']:
                                        for t in cart:
                                            if n['id'] == t['cu_id'] and i['name'] == t['product']:
                                                if qty <= t['quantity']:
                                                    t['quantity'] -= qty
                                                    break
                                                elif qty >= t['quantity']:

                                                    cart.remove(t)
                                                    break

                                        print("Total amount to pay:", qty * i['price'])
                                        op_2 = input("Confirm Place order(y,n)")
                                        if op_2 == 'y':
                                            if n['wallet'] < i['price']:
                                                v = input("Insufficient balance!!!\n1.Add money 2.exit")
                                                if v == '1':
                                                    amt = int(input("Enter amount to add money:"))
                                                    n['wallet'] += amt
                                                elif v == '2':
                                                    break
                                            mon = int(input("Enter the amount to pay:"))
                                            if mon <= n['wallet'] and mon == qty * i['price']:
                                                n['wallet'] -= (qty*i['price'])

                                                print("Wait for order confirmation")
                                                ord_id += 1
                                                time.sleep(2)
                                                for k in vendor:
                                                    if i['id'] == k['id']:
                                                        c = k
                                                order.append({'cu_id': n['id'], 'mer_id': i['id'],
                                                              'mer_name': k['username'], 'buyer': n['name'],'quantity': qty,
                                                              'ord_id': ord_id, 'name': i['name'],
                                                              'paid': (qty * i['price'])})
                                                merchat_pro_selled.append(
                                                    {'id': i['id'], 'name': i['name'], 'quantity': qty,
                                                     'paid': (qty * i['price']), 'ord_id': ord_id,
                                                     'buyer': n['name']})
                                                input("Order Place")
                                                i['quantity'] -= qty
                                                break
                                            elif  mon > n['wallet']:
                                                input("insufficient account balance")
                                                break

                                    elif qty > i['quantity']:
                                        print("Only",i['quantity'],"availalbe")
                                        input()
                                        pass





                                break

                            elif op_1 == 3:
                                c = False
                                break

            if c == False:
                break




def new_customer():
    os.system('cls')

    print("    Create new account   ")
    print("-------------------------")
    cus_name = input("Enter Your Name:")
    cus_pass = int(input("Create Password:"))
    print('c'+str(100 + len(customer) +1)+' is your Customer ID')
    customer.append({'name':cus_name,'password':cus_pass,'id': ('c'+str(100 + len(customer) +1)),'wallet':10000})

    input("Your Account has been created succesfull!!!\npress enter to continue")

def customer_login():
    while True:
        ord_id = 100
        os.system('cls')
        print("   Amazon   ")
        print("------------")
        print("Customer Menu")
        acc_ = int(input("1.New user\n2.Existing user\n3.Exit\nEnter Option:"))
        if acc_ == 1:
            new_customer()
        elif acc_ == 2:
            os.system('cls')
            print("        Customer Menu      ")
            print("---------------------------")
            cus_id = input("Enter Customer ID:")
            cus_pass = int(input("Enter Password:"))


            for n in customer:
                if n['id'] == cus_id and  n['password'] == cus_pass:

                    os.system('cls')
                    print("------------------------------")
                    print("       Login Succesfull       ")
                    print("------------------------------")
                    time.sleep(1)
                    while True:

                        os.system('cls')
                        print("            AMAZON            ")
                        print("------------------------------")

                        op_2 = int(input("1.Home Page\n2.Cart\n3.Order\n4.Log Out\nEnter the option:"))
                        if op_2 == 1:

                            show_product(n,ord_id)
                            ord_id += 1


                        elif op_2 == 2:
                            os.system('cls')
                            if cart == []:
                                input("You don't have any item in your cart!!\npress enter to continue")
                            else:
                                k = False
                                for i in cart:
                                    if i['cu_id'] == n['id']:
                                        k = True


                                if k:
                                    while True:
                                        os.system('cls')
                                        total = 0
                                        co = 0
                                        print("                  Your Cart                  ")
                                        print("-----------------------------------------------")
                                        print("Product Name         Quantity        price")
                                        print("-----------------------------------------------")
                                        for c in cart:
                                            if c['cu_id'] == n['id']:
                                                co += 1
                                                print(c['product'],'                    ',c['quantity'],'          ',c['price'] )
                                                total += c['quantity']*c['price']
                                        print("-----------------------------------------------")
                                        print("Total item :",co,'           Toal price:',total)

                                        op = int(input("\n1.Remove product\n2.Add product\n3.Buy product\n4.Main Menu\nEnter option:"))
                                        if op == 1:
                                            re_pro = input('enter the product name:')
                                            for i in cart:
                                                if i['cu_id'] == cus_id and re_pro == i['product']:
                                                    qt = int(input("Enter quantity to remove:"))
                                                    if  qt > i['quantity']:
                                                        print('only',i['quantity'],'avilabe in your cart')
                                                    elif qt <= i['quantity']:
                                                        i['quantity'] -= qt
                                                        if i['quantity'] == 0:
                                                            cart.remove(i)

                                                    input("Product removed succesfully from your cart")
                                                    break
                                        elif op == 2:
                                            ad_pro = (input("Enter the product name:"))
                                            for c in cart:
                                                if c['cu_id'] == cus_id and ad_pro == c['product']:
                                                    qt_ = int(input("Enter quantity to add:"))
                                                    for b in product:
                                                        if b['name'] == ad_pro:

                                                            if b['quantity'] >= (c['quantity'] + qt_):
                                                                c['quantity'] += qt_
                                                                input("\nProduct added succesfully to the cart")
                                                                break
                                                            elif b['quantity'] < (c['quantity'] + qt_):
                                                                print("\nOnly",b['quantity'],b['name'],'avilable ')
                                                                input("\nPress enter to continue")
                                                                break
                                        elif op == 3:
                                            for i in cart:
                                                if i['cu_id'] == n['id']:
                                                    for k in product:
                                                        if i['mer_id'] == k['id']:
                                                            if k['name'] == i['product']:
                                                                if i ['quantity'] <= k['quantity']:
                                                                    ord_id  += 1


                                                                    order.append({'cu_id': n['id'], 'mer_id': i['mer_id'],

                                                                                  'quantity': i['quantity'],
                                                                                  'ord_id': ord_id,'buyer':n['name'] ,'name': i['product'],
                                                                                  'paid': (i['quantity']* k['price'])})
                                                                    merchat_pro_selled.append(
                                                                        {'id': i['mer_id'], 'name': i['product'],
                                                                         'quantity': i['quantity'],
                                                                         'paid': (i['quantity'] * i['price']), 'ord_id': ord_id,
                                                                         'buyer': n['name']})
                                                                    cart.remove(i)
                                                                    k['quantity'] -= i['quantity']
                                                                elif i ['quantity'] > k['quantity']:
                                                                    print("only",k['quantity'],"avilable")
                                                                    input()
                                                                    break
                                            input("Wait for order confirmation")
                                            time.sleep(2)
                                            input("Order placed")
                                            break


                                        elif op == 4:
                                            break


                        elif op_2 == 3:
                            os.system('cls')
                            k = False
                            for i in order:
                                if i['cu_id'] == n['id']:
                                    k = True
                            if k:
                                os.system('cls')
                                print("                   YOUR ORDER                  ")
                                print("-----------------------------------------------")
                                print("Product Name         Quantity        paid            order ID")
                                print("-----------------------------------------------")
                                for i in order:
                                    if i['cu_id'] == n['id']:
                                        print(i['name'],'         ',i['quantity'],'       ',i['paid'],'             ',i['ord_id'])
                                op_3 = int(input("1.Cancel order\n2.exit\nEnter option:"))
                                if op_3 == 1:
                                    cd = int(input("enter order id:"))
                                    for i in order:
                                        if i['cu_id'] == n['id'] and i['ord_id'] == cd:
                                            for j in product:
                                                if j['id'] == i['mer_id'] and j['name'] == i['name']:
                                                    j['quantity'] += i['quantity']
                                                    order.remove(i)
                                                    for k in merchat_pro_selled:
                                                        if k['id'] == j['id'] and k['name'] == j['name'] and k['buyer'] == i['buyer']:
                                                            merchat_pro_selled.remove(k)
                                                            break
                                                    input("Order cancelled")




                                elif op_3 == 2:
                                    break

                            else:
                                os.system('cls')
                                print("                   YOUR ORDER                  ")
                                print("-----------------------------------------------")
                                print("You did't ordered any product")
                                input("\nPress enter to continue")


                        elif op_2 == 4:
                            input("Succesfully logged out!! press enter to continue")
                            break






        elif acc_ == 3:
            os.system('cls')
            input("Thank You !! Press Enter To continue")
            break








while True:
    os.system('cls')

    op = int(input("\tAMAZON\n1.Admin\n2.Merchent\n3.Customer\n4.Exit\nEnter your choise:"))
    if op == 1:
        admin()
    elif op == 2:
        merchent(product)
    elif op == 3:
        customer_login()
    elif op == 4:
        os.system('cls')
        print("Thank You")
        break
    else:
        print("Wrong Option")




