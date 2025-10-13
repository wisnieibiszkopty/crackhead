from cesear.Cesar import Cesar
from cesear.caesarCipherCrack import *
from vigenere.Vigenere import Vigenere


def cesar_main():
    message = input('message: ')
    key = input('key: ')
    mode = input('encrypt/decrypt [e/d]:')

    cesar = Cesar()

    if mode == 'e':
        encryption = cesar.encrypt(message, int(key))
        print(encryption)
    elif mode == 'd':
        decryption = cesar.decrypt(message, int(key))
        print(f'decrypted message {decryption}')

def cesarcesar():
    #cesar_main()

    crackCaesarCipher('dTfceoiZiołdc')

    # W dniu swojej śmierci Juliusz Cezar prawie pokrzyżował plany spiskowców. Jego żona bardzo źle się czuła i miała bardzo krwawe sny. Poprosiła go o pozostanie w domu, ale ostatecznie Juliusz zdecydował się pojawić na obradach senatu. Nawet w drodze na obrady otrzymał list z ostrzeżeniem, ale spieszył się i schował go na później.
    #crackCaesarCipher(
    #   '0iEŃJWiŚXÓKĘKiTNJĘSĆJiwWŁJWŚŹińĘŹĄSiRSĄXJĘiRÓLSŹZaÓXĄMiRŁĄŃZiŚRJŚLÓXĆPXliwĘHÓiaÓŃĄiCĄSEŹÓiŻŁĘiŚJFiĆŹWMĄiJiNJĄMĄiCĄSEŹÓiLSXĄXĘiŚŃZli4ÓRSÓŚJMĄiHÓiÓiRÓŹÓŚUĄŃJĘiXiEÓNW,iĄŁĘiÓŚUĄUĘĆŹŃJĘiwWŁJWŚŹiŹEĘĆZEÓXĄMiŚJFiRÓKĄXJDiŃĄiÓCSĄEĄĆIiŚĘŃĄUWliżĄXĘUiXiESÓEŹĘiŃĄiÓCSĄEZiÓUSŹZNĄMiŁJŚUiŹiÓŚUSŹĘaĘŃJĘN,iĄŁĘiŚRJĘŚŹZMiŚJFiJiŚĆIÓXĄMiHÓiŃĄiRPŻŃJĘKl')

    # Z kodu Cezara korzystano nawet w 1915 roku. Armia Imperium Rosyjskiego posługiwała się nim jako zamiennikiem dla jej bardziej skomplikowanych szyfrów, które były zbyt trudne do opanowania dla rosyjskiego wojska, dzięki czemu niemieccy i austriaccy kryptoanalitycy nie mieli większych problemów z odczytaniem tych wiadomości.
    #crackCaesarCipher(
    #    'P2ćhYn29ZpŚkŚ2ćhkpólmŚfh2fŚńZm2ń2śżśx2khćn526kębŚ2BęjZkbnę2KhlóclćbZah2jhlenabńŚeŚ2lbŹ2fbę2cŚćh2pŚębZffbćbZę2YdŚ2cZc2UŚkYpbZc2lćhęjdbćhńŚfóWą2lpóŻkiń,2ćmikZ2Uóeó2pUóm2mknYfZ2Yh2hjŚfhńŚfbŚ2YdŚ2khlóclćbZah2ńhclćŚ,2YpbŹćb2WpZęn2fbZębZWWó2b2ŚnlmkbŚWWó2ćkójmhŚfŚdbmóWó2fbZ2ębZdb2ńbŹćlpóWą2jkhUdZęiń2p2hYWpómŚfbZę2móWą2ńbŚYhęhłWb5')


def vigenere_main():
    vigenere = Vigenere()
    vigenere.run()

def vigenerevigenere():
    vigenere_main()

def main():
    #cesarcesar()
    vigenerevigenere()


if __name__ == '__main__':
    main()