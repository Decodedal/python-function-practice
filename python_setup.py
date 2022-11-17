def greeting():
    print('Greetings user')

def pack(item_one, iten_two, item_three):
    myItems = [item_one, iten_two, item_three]
    return myItems

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    for lunch in list:
        if lunch == list[0]:
            print(f"first i eat {lunch}")
        else:
            print(f"next I eat {lunch}")    

    
        

eat_lunch(['chicken','some roastbeef','a pizza'])
eat_lunch([])     