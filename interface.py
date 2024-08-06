from tkinter import *
from gtts import gTTS
from playsound import playsound

fenetre = Tk()
fenetre.title('Reste de la recette et de dépenses')
fenetre.geometry('640x480')

#RECETTE
label= Label(fenetre, text='Recette')
value = StringVar()
value.set('10 000 ')
recette = Entry (fenetre, textvariable=value)

#DEPENSE
label2= Label(fenetre, text='Dépenses')
value2 = StringVar()
value2.set('10 000 ')
depense = Entry (fenetre, textvariable=value2)
image = PhotoImage(file='image/icons8-plus-30.png')
label_image= Label(fenetre, image=image)
image1 = PhotoImage(file='image/icons8-minus-30.png')
label_image1= Label(fenetre, image=image1)

#RESTE
label3= Label(fenetre, text='Reste')
value3 = StringVar()
entree3 = Entry (fenetre, textvariable=value3)

#Fonction de liste d'ajout de dépense
depenses_list= []
def ajout_liste(event=None):
    global total_depense
    nouvelle_depense= int(value2.get().replace(' ', ''))
    depenses_list.append(nouvelle_depense)
    total_depense= sum(depenses_list)
    print(total_depense)

#Fonction enlever le dernier  élément de la liste
def soustraire_liste(event=None):
    if depenses_list:
        global total_depense
        derniere_depense= depenses_list.pop()
        total_depense= sum(depenses_list)
        print(derniere_depense)
        print(total_depense)


#Fonction calculer le reste avec un audio
def resultat_final():
    recette= int(value.get().replace(' ', ''))
    reste= recette - total_depense
    if reste > 0:
        print(total_depense)
        recette = str(recette)
        reste= str(reste)
        print(reste)
        value3.set(reste)
        mytext=f'Le reste de votre argent est {reste} ariary'
        langage='fr'
        myobj=gTTS(text=mytext, lang=langage, slow=False)
        myobj.save("resultat.mp3")
        playsound("resultat.mp3")
    elif reste == 0:
        value3.set(reste)
        mytext=f'Vous avez dépensez tous votre argent'
        langage='fr'
        myobj=gTTS(text=mytext, lang=langage, slow=False)
        myobj.save("resultat.mp3")
        playsound("resultat.mp3")
    else:
        reste=int(reste)
        reste=-reste
        reste=str(reste)
        value3.set(reste)
        global label4
        label4=Label(fenetre,text='Dette')
        label4.place(x=10, y=80)
        mytext=f' Vos dépenses sont plus grand que la recette, vous devez encore payer {reste} ariary en plus'
        langage='fr'
        myobj=gTTS(text=mytext, lang=langage, slow=False)
        myobj.save("resultat.mp3")
        playsound("resultat.mp3")        

#fonction réinitialiser
def reinitialiser():
    global total_depense
    total_depense=0
    depenses_list.clear()
    value.set('0')
    value2.set('')
    value3.set('0')
    if 'label4' in globals():
        label4.place_forget()

bouton=Button(fenetre, text='Résultat', command=resultat_final)
label_image.bind("<Button-1>", ajout_liste)
label_image1.bind('<Button-1>', soustraire_liste)
bouton1=Button(fenetre,text='Réinitialiser', command=reinitialiser)



label.place(x=10, y=20)
label2.place(x=10, y=50)
label3.place(x=10, y= 80)
bouton.place(x=30, y= 110)
bouton1.place(x=150, y=110)
recette.place(x=90, y=20)
depense.place(x=90, y=50)
label_image.place(x=270, y=48)
label_image1.place(x=300, y=48)
entree3.place(x=90, y=80)

fenetre.mainloop()