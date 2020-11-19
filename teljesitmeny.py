from megoldas import Megoldas
import itertools

def main():
    m: Megoldas = Megoldas("dijazas.txt")
    print (f'A(z) { m.elso.nap }. napon az első fuvar { m.elso.hossz } km hosszú volt.')
    print (f'A(z) { m.utolso.nap }. napon az utolsó fuvar { m.utolso.hossz } km hosszú volt.')
    for w in m.szabadnap:
        print(f'A futár ezen a napon tarotott pihenő napot: { w }. ')
    print(f'{m.legtobbfuvar.index(max(m.legtobbfuvar))} napon volt a legtöbb' )
    for x, i in zip(m.km, range(1,8)):
        print(f'A(z) {i} napon {x} km-t tekert')
    #bekert = int(input("Kérem adjon meg egy km-t"))
    print(f'A(z)  km {m.ar(int(input("kérem a km-t ")))} ft-ba kerül')
    print(m.osszertek)
    m.write()
if __name__ == "__main__":
    main()