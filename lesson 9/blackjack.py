import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = 'y'
while is_game=="y":
    cards_c = [random.choice(cards)]
    cards_p = [random.choice(cards)]
    score = 0
    get_card = "y"
    while get_card == "y":
        cards_p.append(random.choice(cards))
        if sum(cards_p)>21 and 11 in cards_p:
            """если туз в руке и сумма>21"""
            for i in range(0, len(cards_p)):
                if cards_p[i]==11:
                    cards_p[i] = 1
                    break
        score=sum(cards_p)
        print(f"Твоя рука:{cards_p},Очков: {score} ")
        print("Первая карта ИИ: ",cards_c[0])
        if score>21:
            get_card="n"
        else:
            get_card=input("y-взять карту, n-остановиться: ")

    while sum(cards_c)<17:
        cards_c.append(random.choice(cards))
    if sum(cards_c) > 21 and 11 in cards_c:
        """если туз в руке и сумма>21"""
        for i in range(0, len(cards_c)):
            if cards_c[i] == 11:
                cards_c[i] = 1
                break
    score_cards_c=sum(cards_c)
    print("="*10)
    print(f"Твоя итоговая рука:{cards_p}.Счёт очков: {score}")
    print(f"Итоговая рука ИИ:{cards_c}.Счёт очков: {score_cards_c}")
    if score>21 and score_cards_c>21:
        print("Ничья!")
    elif score>21:
        print("Ты проиграл")
    elif score_cards_c>21:
        print("ИИ проиграл. Ты выиграл!")
    elif score==score_cards_c:
        print("Ничья")
    elif score>score_cards_c:
        print("Победа")
    else:
        print("Проиграл")
    is_game=input("Играем дальше y-да,n-нет")