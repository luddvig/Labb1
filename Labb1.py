import csv

class Pokemon():
    # 13 attribut
    def __init__(self,number,name,type1,type2,total,hp,attack,defense,sp_attack,sp_defense,speed,generation,legendary):
        self.number = number
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.hp < other.hp

    def __gt__(self, other):
        return self.speed > other.speed

    def __add__(self, other):
        return int(self.attack) + int(other.attack)

    def __bool__(self):
        return self.legendary

    def __contains__(self, item):
        if item in self.number:
            return True
        else:
            return False


def skapa_egen_poke(number,name,type1,type2,total,hp,attack,defense,sp_attack,sp_defense,speed,generation,legendary):
    pokemon = Pokemon(number,name,type1,type2,total,hp,attack,defense,sp_attack,sp_defense,speed,generation,legendary)
    #print("Du har kallat på " + str(pokemon))
    return pokemon

ludde_poke = skapa_egen_poke(1,"Ludde","vatten","el",350,80,90,100,110,120,70,7,True)
adam_poke = skapa_egen_poke(2,"Adam","sten","drake",500,90,100,120,110,140,40,7,True)

if ludde_poke:
    print("Ja")
else:
    print("Nej")

def jmrf_pokes(poke1,poke2):
    print("Jämförelse av poke " + str(poke1) + " och poke " + str(poke2) + ".")
    if poke1 < poke2:
        print("Poke " + str(poke2) + " har " + str(poke2.hp) + " hp, det är mest.")
    else:
        print("Poke " + str(poke1) + " har " + str(poke1.hp) + " hp, det är mest.")
    if poke1 > poke2:
        print("Poke " + str(poke1) + " har " + str(poke1.speed) + " speed, det är mest.")
    else:
        print("Poke " + str(poke2) + " har " + str(poke2.speed) + " speed, det är mest.")
    attack=poke1+poke2
    print("De har tillsammans " + str(attack) + " attack.")
    if poke1 and poke2:
        print("Båda är legendary")
    elif poke1:
        print(str(poke1) + " är legendary")
    elif poke2:
        print(str(poke2) + " är legendary")
    else:
        print("Ingen är legendary")

a = jmrf_pokes(ludde_poke,adam_poke)

def pokes_fran_fil(fil):
    with open(fil, "r") as file:
        alla_pokes = csv.reader(file)
        pokes_list = list(alla_pokes)
    pokes = []
    for row in pokes_list:
        pokes.append(Pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                             row[7], row[8], row[9], row[10], row[11], row[12]))
    return pokes

pokes = pokes_fran_fil("pokemon.csv")

def hitta_poke(pokes_list, num):
    for poke in pokes_list:
        if num in poke:
            return poke

min_poke = hitta_poke(pokes,"200")
print(min_poke)
