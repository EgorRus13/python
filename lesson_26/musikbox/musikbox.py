from random import choice
import playsound

class MusikBox:
    def __init__(self):
        self.__score=0
        self.__variants="bcehIsy"
        self.__sequence=choice(self.__variants)
        print(self.__sequence)

    def play(self):
        for letter in self.__sequence:
            playsound.playsound(f"sounds/{letter}.mp3")


    def __next(self):
        __dlina=len(self.__sequence)+1
        self.__sequence=""
        for _ in range(__dlina):
            self.__sequence+=choice(self.__variants)


    def check(self,predpolojenie):
        if self.__sequence==predpolojenie.lower().strip():
            playsound.playsound(f"sounds/correct.wav")
            self.__score+=1
            self.__next()
        else:
            self.__score-=0.5
            playsound.playsound(f"sounds/incorrect.wav")

    def get_score(self):
        return self.__score

