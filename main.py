unit_price = {'water': 3.69, 'elec': 27.22}

emax_spending = [100]
wmax_spending = [100]        

if emax_spending == []:
    while True:
        try:
            espending = float(input("how much would you like to spend on elec this month? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            emax_spending.append(espending)
            eamount = emax_spending[0] / unit_price['elec']
            print(round(eamount, 2), "kwh left this month")
            break
    
else:
    eamount = emax_spending[0] / unit_price['elec']
    print(round(eamount,2), "kwh left this month")

if wmax_spending == []:
    while True:
        try:
            wspending = float(input("how much would you like to spend on water this month? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            wmax_spending.append(wspending)
            wamount = wmax_spending[0] / unit_price['water']
            print(round(wamount, 2), "litres left this month")
            break

else: 
    wamount = wmax_spending[0] / unit_price['water']
    print(round(wamount,2), "litres left this month")

while True:
    try:
        print("""
            What would you like to do?
            1. Update max spending for elec (month)
            2. Update max spending for water (month)
            3. Update daily elec usage 
            4. Update daily water usage 
            5. Check water & electricty remaining for the month 
            6. Check total expenditure so far (month)
            7. Suggestions to reduce usage 
            8. Exit
        """)
        choice = int(input("Please make a choice 1/2/3/4/5/6/7/8: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue    
    if choice == 1:
        print("Update max spending for electricity! (month)")
        while True:
            try:
                espending = float(input("how much would you like to spend on elec this month? "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:                 
                emax_spending.append(espending)
                eamount = emax_spending[-1] / unit_price['elec']    
                print(round(eamount, 2), "kwh left this month")
                break
            
    elif choice == 2:
        print("Update max spending for water! (month)")
        while True:
            try:
                wspending = float(input("how much would you like to spend on water this month? "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                wmax_spending.append(wspending)
                wamount = wmax_spending[-1] / unit_price['water']
                print(round(wamount, 2), "litres left this month")
                break   
            
    elif choice == 3:
        
        print("Update daily electricity usage")
        print("""
            Please select appliance:
            1. Television
            2. Air-condition 
            3. Computer 
            4. Exit 
              """)
        appliance = int(input("Please enter input 1/2/3/4: "))
        if appliance == 1:
            print("Television")
        elif appliance == 2:
            print("Air-condition")
        elif appliance == 3:
            print("Computer")
        elif appliance == 4:
            print("Exit")
        elif ValueError:
            print("Sorry, I didn't understand that.")            
        else:
            print("Sorry, I didn't understand that.")

        
    elif choice == 4:
        print("Update daily water usage")
    elif choice == 5:
        print("Check water & electricty remaining for the month") 
    elif choice == 6:
        print("Check total expenditure so far (month)")
    elif choice == 7:
        print("Suggestions to reduce usage ")
    elif choice == 8:
        print("end")
        break
    else:
        print("Sorry, I didn't understand that.")








