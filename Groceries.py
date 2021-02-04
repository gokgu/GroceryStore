import GroceryStore.store_service as store_service

# You can buy these items, but you should be able to afford them for the total cost :)
items_to_purchase = {
    'candy': 7,
    'toy': 15,
    'paper': 8,
    'coffee': 3,
    'socks': 7
}

def application_start():
    customer_money_real = False
    while not customer_money_real:
        customer_money = input('How much money do you have: ')
        if customer_money.isdigit():
            customer_money = int(customer_money)
            customer_money_real = True

    items_price_added_to_cart = []
    customer_shopping = False

    while not customer_shopping:
        add_item_to_cart = input('What item would you like to add to your cart? ')

        # Check if key exists
        if add_item_to_cart.lower() in items_to_purchase:
            items_price_added_to_cart.append(items_to_purchase.get(add_item_to_cart))
            print(f'You currently have {len(items_price_added_to_cart)} items in your cart.')
        else:
            print('Item is not at this store')
            continue

        keep_shopping = input('Do you wish to continue shopping? (Y = yes, N = no) ')

        if keep_shopping.lower().strip() == 'n':
            customer_shopping = True

    store_service.purchase_items(customer_money_arg=customer_money, items=items_price_added_to_cart)

application_start()