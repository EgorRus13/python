alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end=False
while not should_end:
    text=input("Введи свое сообщение:").lower()
    text=list(text)
    shift=int(input("Введи сдвиг:"))

    if shift> len(alphabet):
        shift=shift%len(alphabet)
    elif shift<-len(alphabet):
        shift = shift % len(alphabet)