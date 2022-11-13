import random
life=10
length=3

answer=random.randint(100,999)
answer=str(answer)

while life:
    is_guessed=False
    print("="*10)
    print("Hp:",life)
    guess=input("Predlojenie")
    if len(guess)!=3 or not guess.isdigit():
        print("Число от 100 до 999, пожалуйста!")
        continue