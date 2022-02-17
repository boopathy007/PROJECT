free_taxi = []
tax = []
cust_id  = 0
class taxi:
    def __init__(self,taxi_id):
        self.taxi_id = taxi_id
        
        self.free_time = 6
        self.current_pos = 'A'
        self.trip = []
        self.earning = 0



for i in range(1,6):
    create_taxi = taxi(i)
    tax.append(create_taxi)

while True:
    
    try:
        op = int(input("1.Book taxi\n2.View Taxi\n3.Exit\nEnter option:"))
    
        if op == 3:
            break
            
        elif op== 1:
                
                   
                        t_earn = 100
                        pickup = input("Enter Pickup point:")
                        if (pickup >= 'A' or pickup >= 'a') and (pickup<='F' or pickup <= 'f'):
                            drop = input("Enter Drop Point:")
                            if (drop >= 'A' or drop >= 'a') and (drop<='F' or drop <= 'f') and drop != pickup:
                                pick_time = int(input("Enter time:"))
                                for i in tax:
                                    if pick_time >= i.free_time and int(abs(ord(i.current_pos)-ord(pickup.upper()))<=(pick_time-i.free_time)):
                                        free_taxi.append(i)
                                
                                if free_taxi != []:
                                    earn = free_taxi[0].earning
                                    book_tax=free_taxi[0]
                                    dist = int(abs(ord(free_taxi[0].current_pos)-ord(pickup.upper())))
                                    for i in free_taxi:
                                        if earn <= i.earning and int(abs(ord(i.current_pos)-ord(pickup.upper()))) <= dist :
                                            dist =  int(abs(ord(i.current_pos)-ord(pickup.upper())))
                                            book_tax = i
                                            earn  = i.earning
                                    cust_id += 1
                                    book_tax.current_pos = drop.upper()
                                    distance = int(abs(ord(pickup)-ord(drop))) * 15 
                                    book_tax.free_time = book_tax.free_time + abs(ord(pickup)-ord(drop))
                                    
                                    t_earn = 100 + (distance-5)*10                                
                                    book_tax.earning += t_earn
                                    
                                    book_tax.trip.append({"customer_id":cust_id,"taxi_id":
                                                          book_tax.taxi_id,"pickup":pickup.upper(),"drop":drop.upper(),
                                                          "earning":t_earn})
                                                            
                                    print(book_tax.taxi_id,"has been booked")
                                    free_taxi = []
                                    
                                else:
                                    input("No free Taxi")
                            else:
                                input("Invalid option")
                        else:
                            input("Invalid option")
                        
                   
                    
        elif op == 2:
                print("TAXI ID".ljust(15),"CURRENT POS".ljust(20),"FREE TIME".ljust(15),"TRIP".ljust(10),"EARNING".ljust(15))
                print("-"*60)
                for i in tax:
                    print(str(i.taxi_id).ljust(15),i.current_pos.ljust(20),str(i.free_time).ljust(15),str(len(i.trip)).ljust(10),str(i.earning).ljust(15))
                print("-"*60)
                for i in tax:
                    print("TAXI ID:".rjust(35),i.taxi_id)
                    print("-"*70)
                    print("CUSTOMER ID".ljust(20),"PICKUP".ljust(15),"DROP".ljust(15),"EARNING".ljust(15))
                    print("-"*70)
                    if len(i.trip) == 0:
                        print("NO TRIP")
                    else:
                        for j in range(len(i.trip)):
                            print(str(i.trip[j]["customer_id"]).ljust(20),i.trip[j]["pickup"].ljust(15),i.trip[j]["drop"].ljust(15),str(i.trip[j]["earning"]).ljust(15))
                input()
    except:
        input("invalid input!!")

