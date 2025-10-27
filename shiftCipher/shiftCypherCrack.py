from shiftCipher.ShiftCipher import *


def bruteForceShiftCypher(cipher: str):
    shift = ShiftCipher()

    for i in range(2, len(cipher)-1):
        decrypted_message = shift.decrypt(cipher, i)
        print(f"i={i}, decrypted_message={decrypted_message}")


if __name__ == "__main__":
    bruteForceShiftCypher("S azmlyeaft roz dnpąar lzseełźsóćtw a mwpeirteaonwdidęoo wppyor dzjoeebssnttya cwłhia.atnwDiyoa p.daos ozwłaanmiaen ifar aig mneinet uz aopdeswznyifar obweaznpeigeoczteeńkssttwua .d oŁ asmziyef rsui ęp ogzow")