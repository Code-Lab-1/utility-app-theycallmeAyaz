def vending_machine():
    # Define products and their prices
    A01 = {'product': 'kinder surprise-egg', 'price': 3.50, 'stock': 5, 'code': 'A01'}
    A02 = {'product': 'Bounty-coconut chocolate', 'price': 4.50, 'stock': 5, 'code': 'A02'}
    A03 = {'product': 'Snickers chocolate bar', 'price': 2.75, 'stock': 5, 'code': 'A03'}
    A04 = {'product': 'Juicy fruit Chewing gum', 'price': 2.75, 'stock': 5, 'code': 'A04'}

    B01 = {'product': 'Water', 'price': 1.50, 'stock': 10, 'code': 'B01'}
    B02 = {'product': 'Mango juice', 'price': 5, 'stock': 10, 'code': 'B02'}
    B03 = {'product': 'Pineapple-juice', 'price': 5, 'stock': 10, 'code': 'B03'}
    B04 = {'product': 'Strawberry-milkshake', 'price': 6.75, 'stock': 10, 'code': 'B04'}

    C01 = {'product': 'Lays salt chips', 'price': 4.75, 'stock': 5, 'code': 'C01'}
    C02 = {'product': 'Cheetos spicy chips', 'price': 5, 'stock': 5, 'code': 'C02'}
    C03 = {'product': 'Lays cheese flavoured chips', 'price': 4.75, 'stock': 5, 'code': 'C03'}
    C04 = {'product': 'Lays ketchup flavoured chips', 'price': 4.75, 'stock': 5, 'code': 'C04'}


    products = [A01,A02,A03,A04,
                B01,B02,B03,B04,
                C01,C02,C03,C04]

    # cash in machine
    cash_available = 0

    # display greeting message
    print('      *************** Greetings-User! ***************')
    # The vending machine is named to The Snakinator
    print('              Welcome to the The Snakinator!         ')
    print('      ***********************************************')
    

    # display products and prices
    def display_products():
        available_products = []
        for product in products:
            if product['stock'] >= 1:
                available_products.append(product)
        print('      **The following products are available:**\n')
        for product in available_products:
            print(f"       Product: {product['product']}, Price: {product['price']}, Item: {product['code']}\n")
        print('      ***********************************************')

    # display items in cart and total cost
    def display_cart(cart):
        print('      Cart:')
        total_cost = 0
        for item in cart:
            print(f"      {item['product']}, {item['price']}")
            total_cost += item['price']
        print(f"      Total cost: {total_cost}")
        cash_remaining = cash_available - total_cost
        print(f'      Cash remaining: {cash_remaining}')
        return total_cost

    # generate receipt
    def generate_receipt(cart):
        print("***********************************************")
        print('        Receipt:\n')
        total_cost = display_cart(cart)
        for item in cart:
            print(f"      {item['product']}, {item['price']} is dispensed")
        print(f"      Total cost: {total_cost}")
        cash_remaining = cash_available - total_cost
        print(f'      Change dispensed: {cash_remaining}')
        print("      Transaction complete!\n")
        print("***********************************************")

    # display welcome message
    print('      ***********************************************')
    print('''             *Get snacking with The Snakinator-
               the ultimate vending machine for 
                    all your snack needs!*''')
    print('      ***********************************************')
    print("          instructions to use the vending machine:")
    print('''        (1)Select a product by entering its code
                 (if product is available)''')
    print("        (2)Enter code exactly as it is(case-sensitive)")
    print("        (3)Enter Cash into the machine")
    print('''        (4)Enter c to continue shopping (c),
           Enter o to checkout (o)
           Enter e to exit the machine (e)
        (5)Once o is entered, confirm to purchase(y/n)
           Enter (y) to dispense items,change
           and transaction will be completed.
        (6)Want to exit the machine after buying/not buying anything?
           Enter (e) in product code selection 
           then enter (e) again to exit ""without buying or not buying anything""
           Don't worry your cash will be returned if you bought nothing ''')
    print('      ***********************************************')
    
    # create an empty cart
    cart = []

    is_done = False
    while not is_done:
    # display products and prices
        display_products()
    # prompt user to select a product
        selected = input('      Select product by code: ')

    # check if selection is a valid product
        selection_valid = False
        for product in products:
            if selected == product['code']:
                selection_valid = True
                selected_product = product
                break

        if selection_valid:
            # get price of selected product
            price = selected_product['price']
        # prompt user to insert cash until enough is inserted
            while cash_available < price:
                try:
                   cash_inserted = float(input('      Insert cash / ' + str(price - cash_available) + ' or amount: '))
                except ValueError:
                    print('      Invalid input. Please insert a valid amount of cash.')
                    continue
                cash_available += cash_inserted
        # dispense product and update stock
            print('      You selected this ' + selected_product['product'])
            selected_product['stock'] -= 1
            print('      Cash remaining: ' + str(cash_available))

        # add item to cart
            cart.append(selected_product)
        else:
            print('      Invalid selection. Please select a valid product.')

    # prompt user to continue shopping, checkout, or exit
        while True:
            a = input('      Would you like to continue shopping (c), checkout (o), or exit (e)?: ')
            if a == 'c':
                print("\n")
                break
            elif a == 'o':
            # display cart and total cost
                display_cart(cart)
            # prompt user to confirm purchase
                confirm = input('      Confirm purchase (y/n)?: ')
                if confirm == 'y':
                # generate receipt
                    generate_receipt(cart)
                # clear cart
                    cart = []
                # reset cash available
                    cash_available = 0
                    break
                elif confirm == 'n':
                    if cash_available > 0:
                        # Return user's cash
                        print(f'      Exiting the vending machine. Your change of ${cash_available} has been returned. Thank you for using The Snakinator!')
                    else:
                        print('      Exiting the vending machine. Thank you for using The Snakinator!')
                        is_done = True
                        break
                    # clear cart
                    cart = []
                # reset cash available
                    cash_available = 0
                    break
                else:
                    print('      Invalid input. Please enter y or n.')
            elif a == 'e':
                if cash_available > 0:
                    # Return user's cash
                    print(f'      Exiting the vending machine. Your change of ${cash_available} has been returned. Thank you for using The Snakinator!')
                else:
                    print('      Exiting the vending machine. Thank you for using The Snakinator!')
            # set is_done to True to exit the main loop
                is_done = True
                break
            else:
                print('      Invalid input. Please enter c, o, or e.')
vending_machine()
