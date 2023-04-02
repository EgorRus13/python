from user import User
u1=User("Русяев","Егор","EgorRus13","12345")
u2=User()

users=[u1,u2]
l=input("Login: ")
p=input("Password: ")
for u in users:
    if u.log_in(l,p):
        print("You log_inid.")
    current_user=u