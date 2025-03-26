import pygame
import time
import random

# Alustetaan pygame
pygame.init()

# Värit
valkoinen = (255, 255, 255)
musta = (0, 0, 0)
punainen = (213, 50, 80)
vihreä = (0, 255, 0)
sininen = (50, 153, 213)

# Näytön koko
leveys = 600
korkeus = 400

# Peli-ikkuna
ruutu = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('Matopeli 🐍')

kello = pygame.time.Clock()

# Madon palojen koko
mato_blokin_koko = 10
nopeus = 15

# Fontit
fontti = pygame.font.SysFont("bahnschrift", 25)
pistefontti = pygame.font.SysFont("comicsansms", 20)

def pisteet(pisteet):
    arvo = pistefontti.render("Pisteet: " + str(pisteet), True, musta)
    ruutu.blit(arvo, [0, 0])

def mato(maton_palat):
    for pala in maton_palat:
        pygame.draw.rect(ruutu, vihreä, [pala[0], pala[1], mato_blokin_koko, mato_blokin_koko])

def viesti(msg, väri):
    teksti = fontti.render(msg, True, väri)
    ruutu.blit(teksti, [leveys / 6, korkeus / 3])

def peli():
    peli_päällä = True
    peli_loppu = False

    x = leveys / 2
    y = korkeus / 2

    x_muutos = 0
    y_muutos = 0

    maton_pituus = 1
    maton_palat = []

    omena_x = round(random.randrange(0, leveys - mato_blokin_koko) / 10.0) * 10.0
    omena_y = round(random.randrange(0, korkeus - mato_blokin_koko) / 10.0) * 10.0

    while peli_päällä:

        while peli_loppu:
            ruutu.fill(valkoinen)
            viesti("Pelaa peli uudestaan!  Enter = Uudestaan, Esc = Lopeta", punainen)
            pisteet(maton_pituus - 1)
            pygame.display.update()

            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_ESCAPE:
                        peli_päällä = False
                        peli_loppu = False
                    if tapahtuma.key == pygame.K_RETURN:
                        peli()

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                peli_päällä = False
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    x_muutos = -mato_blokin_koko
                    y_muutos = 0
                elif tapahtuma.key == pygame.K_RIGHT:
                    x_muutos = mato_blokin_koko
                    y_muutos = 0
                elif tapahtuma.key == pygame.K_UP:
                    y_muutos = -mato_blokin_koko
                    x_muutos = 0
                elif tapahtuma.key == pygame.K_DOWN:
                    y_muutos = mato_blokin_koko
                    x_muutos = 0

        # Tarkistetaan reunat
        if x >= leveys or x < 0 or y >= korkeus or y < 0:
            peli_loppu = True

        x += x_muutos
        y += y_muutos
        ruutu.fill(sininen)

        pygame.draw.rect(ruutu, punainen, [omena_x, omena_y, mato_blokin_koko, mato_blokin_koko])
        maton_palat.append([x, y])
        if len(maton_palat) > maton_pituus:
            del maton_palat[0]

        # Osuma omaan häntään
        for pala in maton_palat[:-1]:
            if pala == [x, y]:
                peli_loppu = True

        mato(maton_palat)
        pisteet(maton_pituus - 1)

        pygame.display.update()

        if x == omena_x and y == omena_y:
            omena_x = round(random.randrange(0, leveys - mato_blokin_koko) / 10.0) * 10.0
            omena_y = round(random.randrange(0, korkeus - mato_blokin_koko) / 10.0) * 10.0
            maton_pituus += 1

        kello.tick(nopeus)

    pygame.quit()
    quit()

peli()
