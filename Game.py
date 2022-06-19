import pygame as pg
import pygamebg
import random
(sirina, visina) = (400, 450) # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina,"Nastavi niz")
prozor.fill(pg.Color("sky blue"))
srce = pg.image.load("srce.png")
zivot=pg.transform.scale(srce,(40,40))

zivoti = 3 # trenutni broj života
poeni = 0 # trenutni broj poena
operacija=["+","-"] # lista oeracija iz koje se bira kasnije bira operator za niz
pozicija_tacnog=0 # pozicija tacnog koja ce se kasnije promeniti
lista_odgovora=[0,0,0] # pocetna lista odgovora

def tekst_levo(x, y, tekst, velicina):
    font = pg.font.SysFont("Arial", velicina) #font kojim će biti prikazan broj poena
    tekst = font.render(tekst, True, pg.Color("blue"))
    prozor.blit(tekst, (x, y))
def tekst_centar(x, y, tekst, velicina): 
    font = pg.font.SysFont("Arial", velicina) #font kojim će biti prikazan niz i ponudjeni odgovori
    tekst = font.render(tekst, True, pg.Color("blue"))
    (sirina_teksta, visina_teksta) = (tekst.get_width(), tekst.get_height())
    (x, y) = (x - sirina_teksta // 2, y - visina_teksta // 2)
    prozor.blit(tekst, (x, y))
    
def crtaj_izraz(): # funkcija koja prikazuje niz i ponudjene odgovore na ekranu
    global pozicija_tacnog
    x=random.randint(1,100) # prvi clan niza 
    a=random.randint(1,100) # biranje vrednosti od koje zavise ostali clanovi niza
    operator=operacija[random.randint(0,1)] #bira se operator iz liste operacija
    if operator=="+": # racunanje clanova niza i rezultata(tj.cetvrtog clana niza ili tacnog odgovora)ako je opetator="+"
        y=x+a # drugi clan  niza
        z=x+2*a # treci clan niza
        rezultat=x+3*a # cetvrti clan niza i tacan odgovor
    if operator=="-": # racunanje clanova niza i rezultata(tj.cetvrtog clana niza ili tacnog odgovora)ako je opetator="-"
        y=x-a # drugi clan  niza
        z=x-2*a # treci clan niza
        rezultat=x-3*a # cetvrti clan niza i tacan odgovor
    netacan1=rezultat+random.randint(1,20) # odredjivanje prvog netacnog odgovora
    netacan2=rezultat-random.randint(1,20) # odredjivanje drugog netacnog odgovora
    pozicija_tacnog=random.randint(0,2) # odredjivanje na kojoj poziciji ce biti tacan rezultat tj.da li ce tacan odgovor biti pod a, b ili c
    pozicija_netacan1=0
    pozicija_netacan2=0
    while pozicija_netacan1==pozicija_tacnog: # odredjivanje na kojoj poziciji ce biti prvi netacan odgovor tj.da li ce tacan odgovor biti pod a, b ili c(a vec je odredjena pozicija tacnog rezultata)
        pozicija_netacan1=random.randint(0,2)
    while pozicija_netacan2==pozicija_tacnog or pozicija_netacan2==pozicija_netacan1: #odredjivanje na kojoj poziciji ce biti drugi netacan odgovor tj.da li ce tacan odgovor biti pod a, b ili c(a vec je odredjena pozicija tacnog rezultata i prvog netacnog odgovora)
        pozicija_netacan2=random.randint(0,2)
    lista_odgovora[pozicija_tacnog]=rezultat # stavljanje tacnog odgovora(rezultata) na poziciju tacnog
    lista_odgovora[pozicija_netacan1]=netacan1 # stavljanje prvog netacnog odgovora na poziciju prvog netacnog
    lista_odgovora[pozicija_netacan2]=netacan2 # stavljanje drugog netacnog odgovora na poziciju drugog netacnog
    tekst_centar(sirina // 2, visina // 3, str(x)+","+str(y)+","+str(z)+","+"___", 60) #ispis izraza na prozoru
    tekst_centar(sirina // 2, visina // 3 + 70, "a." + str(lista_odgovora[0]), 50) #ispis prvog ponudjenog odgovora (odgovora pod a)
    tekst_centar(sirina // 2, visina // 3 + 120, "b." + str(lista_odgovora[1]), 50) #ispis drugog ponudjenog odgovora (odgovora pod b)
    tekst_centar(sirina // 2, visina // 3 + 170, "c." + str(lista_odgovora[2]), 50) #ispis treceg ponudjenog odgovora (odgovora pod c)
def crtaj():
    global poeni,zivoti
    prozor.fill(pg.Color("sky blue"))
    if zivoti > 0:   # ako igra nije završena
        # prikazujemo broj poena
        tekst_levo(10, 10, "Поени: " + str(poeni), 30)
        # prikazujemo preostale živote (iscrtavanjem umanjenih sličica srca)
        for i in range(1, zivoti + 1):
            prozor.blit(zivot, (sirina - 5 - i*zivot.get_width(), 5))
        # iscrtavamo niz i odgovore sve dok je broj zivota veci od 0
        crtaj_izraz()
 
    else:            # ako igra jeste završena
        tekst_centar(sirina // 2, visina // 2, "КРАЈ! БРОЈ ПОЕНА: " + str(poeni), 40)  # prikazujemo rezultat

def obradi_dogadjaj(dogadjaj):
    global poeni,zivoti
    if dogadjaj.type==pg.KEYDOWN: #dogadjaj koji se izvrsava ako se pritegne slovo na tastaturi
        if dogadjaj.key==pg.K_a: #ako se pritegne slovo a
            if pozicija_tacnog==0: #ako je pozicija tacnog odgovora u listi odgovora jednaka 0 i pritegne se a na tastaturi, broj poena se uvecava za 1 i igrica se nastavlja
                poeni+=1
                return True
            else: #ako se pritegne b ili c na kojima su netacni ogdovori(tj. na pozijama 1 i 2 u listi odgovora su netacni odgovori), broj zivota se umanjuje za jedan i igrica se nastavlja(naravno ako je broj zivota i dalje veci od 0)
                zivoti-=1
                return True
        elif dogadjaj.key==pg.K_b: #ako se pritegne slovo b
            if pozicija_tacnog==1: #ako je pozicija tacnog odgovora u listi odgovora jednaka 1 i pritegne se b na tastaturi, broj poena se uvecava za 1 i igrica se nastavlja
                poeni+=1
                return True
            else: #ako se pritegne a ili c na kojima su netacni ogdovori(tj. na pozijama 0 i 2 u listi odgovora su netacni odgovori), broj zivota se umanjuje za jedan i igrica se nastavlja(naravno ako je broj zivota i dalje veci od 0)
                zivoti-=1
                return True
        elif dogadjaj.key==pg.K_c: #ako se pritegne slovo c
            if pozicija_tacnog==2: #ako je pozicija tacnog odgovora u listi odgovora jednaka 2 i pritegne se c na tastaturi, broj poena se uvecava za 1 i igrica se nastavlja
                poeni+=1
                return True
            else: #ako se pritegne a ili b na kojima su netacni ogdovori(tj. na pozijama 0 i 1 u listi odgovora su netacni odgovori), broj zivota se umanjuje za jedan i igrica se nastavlja(naravno ako je broj zivota i dalje veci od 0)
                zivoti-=1
                return True
    return False

    
# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.event_loop(crtaj,obradi_dogadjaj)

