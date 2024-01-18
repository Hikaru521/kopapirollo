import random

def jatek(c_player):
    lehet = ['Kő!', 'Papír!', 'Olló!']
    c_gep = random.choice(lehet)
    print(f"A gép választása: {c_gep}")
    print(f"A player választása: {c_player}")
    if c_player == c_gep:
        print("Döntetlen!")
    elif (c_player == 'Kő!' and c_gep == 'Olló!') or \
            (c_player == 'Olló!' and c_gep == 'Papír!') or \
            (c_player == 'Papír!' and c_gep == 'Kő!'):
        print("Nyertél!")
    else:
        print("A gép nyert!")
