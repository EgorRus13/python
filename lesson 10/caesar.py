alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
simvols=['(',')',',','.',' ','?','!']

should_end=False
while not should_end:
    text=input("Введи свое сообщение:").lower()
    text=list(text)
    shift=int(input("Введи сдвиг:"))

    if shift> len(alphabet):
        shift=shift%len(alphabet)
    elif shift<-len(alphabet):
        shift = shift % -len(alphabet)

    cipher_text=''
    for letter in text:
        if letter in simvols:
            cipher_text+=letter
        else:
            position=alphabet.index(letter)
            if position+shift>len(alphabet):
                new_pisition=position+shift-len(alphabet)
            elif position + shift<0:
                new_pisition = position + shift + len(alphabet)
            else:
                new_pisition = position + shift
                cipher_text+=alphabet[new_pisition]
    print(cipher_text)

