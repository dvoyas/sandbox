class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

        self.is_alive = True


class Knight(Warrior):
    def __init__(self, attack):
        #self.health = health
        self.attack = attack+2
        super().__init__(self)

def fight(unit_1, unit_2):
    first = True
    while unit_1.health > 0:
        if unit_2 <= 0:
            return True
        elif first:
            unit_1.attack -= 1
            unit_2.health -= 1
            first = False
        else:
            unit_2.attack -= 1
            unit_1.health -= 1
            first = True
    return True

if __name__ == '__main__':
    #Theese "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")