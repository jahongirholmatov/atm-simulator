parol = 2026
limit = 3
balans = 5000

def balance():
    print(f"Sizning balansingiz: {balans} so'm")

def pulQushish(pul):
    global balans
    balans += pul
    print(f"{pul} so'm balansingizga qo'shildi. Hozirda {balans} so'm mavjud.")

def pulYechish(pul):
    global balans
    if pul > balans:
        print("Balansda yetarli mablag‘ yo‘q!")
    else:
        balans -= pul
        print(f"{pul} so'm balansingizdan yechildi. Hozirda {balans} so'm qoldi.")

while limit > 0:
    user_parol = int(input("Parolni kiriting: "))
    
    if user_parol == parol:
        print("\nXush kelibsiz ATM ga!\n")
        print("1. Balansni ko‘rish")
        print("2. Pul qo‘shish")
        print("3. Pul yechish")
        tanlov = int(input("Tanlovingizni kiriting (1-3): "))
        
        match tanlov:
            case 1:
                balance()
            case 2:
                pul = int(input("Qancha pul qo‘shmoqchisiz?: "))
                pulQushish(pul)
            case 3:
                pul = int(input("Qancha pul yechmoqchisiz?: "))
                pulYechish(pul)
            case _:
                print("Bunday operatsiya yo‘q! 1-3 oralig‘ida son kiriting.")
        break
    else:
        limit -= 1
        print(f"Parol noto‘g‘ri. {limit} ta urinishingiz qoldi.")

if limit == 0:
    print("Karta bloklandi! Siz 3 marta noto‘g‘ri parol kiritdingiz.")