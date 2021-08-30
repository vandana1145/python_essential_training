class Frog:
    talk = 'turr turr'
    move = 'jump jump'

    def sound(self):
        print(f'Froggy talks {self.talk}')

    def walk(self):
        print(f'Froggy moves {self.move}')


def main():
    froggy = Frog()
    froggy.sound()
    froggy.walk()

if __name__ == '__main__': main()