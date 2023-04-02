from musikbox import MusikBox

pleer=MusikBox()

while True:
    pleer.play()
    guess=input("Cho yclishal?: ")
    pleer.check(guess)
    print("Ochkov:", pleer.get_score())