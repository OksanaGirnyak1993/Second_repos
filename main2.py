import random
def get_number_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
       return[]
    
    un_numbers = set()

    while len(un_numbers) < quantity:
        random_num = random.randint(min, max)

        un_numbers.add(random_num)

    return sorted(list(un_numbers))

lot_num = get_number_ticket(1, 100, 6)
print("Lot_num", lot_num)        
         
     


