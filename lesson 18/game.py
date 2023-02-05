import easygui as ez
import random
def rock_paper_scissors():
    r="img/kamen.png"
    p="img/noz.png"
    s="img/list.png"

    vtm=random.choice([r,p,s])
    x=ez.buttonbox(title="tyt game",
                 msg="viberi",
                 images=[r,p,s],
                 choices=("nazad",)
                 )
    if x==s and vtm==s:ez.msgbox(msg="nichia")
    elif x==p and vtm==p:ez.msgbox(msg="nichia")
    elif x==r and vtm==r:ez.msgbox(msg="nichia")
    elif x==r and vtm==s:ez.msgbox(msg="win")
    elif x==s and vtm==r:ez.msgbox(msg="lose")
    elif x==r and vtm==p:ez.msgbox(msg="lose")
    elif x==p and vtm==r:ez.msgbox(msg="win")
    elif x==p and vtm==s:ez.msgbox(msg="lose")
    else:
        msg=("win")




def guess_the_number():
    ez.msgbox('Здесь будет игра "Угадай число"')




def guess_the_number():
    a=random.randint(1,100)
    m=ez.integerbox(
  msg='otgadau chislo',
  title='От нуля до ста',
  lowerbound=1,
  upperbound=100,
    )
    while a !=m:
        if m >a:
            m=ez.integerbox(
                msg=f'chislo menshe {m}',
                title='От нуля до ста',
                lowerbound=1,
                upperbound=100,
                image="img/bolbshe.png"
            )
        else:
            m=ez.integerbox(
                msg=f'chislo bolshe{m}',
                title='От нуля до ста',
                lowerbound=1,
                upperbound=100,
                image="img/menbshe.png")




games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = ez.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()










