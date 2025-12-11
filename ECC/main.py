from keyGenerator import keyGenerate
from encryption import Encrypt
from decryption import Decrypt


# 공개 키 역할 (with third party)
class publicKeys:
    def __init__(self, a, b, p, e1, e2):
        self.a = a
        self.b = b
        self.p = p
        self.e1 = e1
        self.e2 = e2


# ---- Bob의 키 생성
(a, b, e1, e2, d, p) = keyGenerate()

print(f"Bob이 생성한 공개 키\n"
      f"\na : {a}"
      f"\nb : {b}"
      f"\np : {p}"
      f"\ne1 : ({e1.x}, {e1.y})"
      f"\ne2 : ({e2.x}, {e2.y})"
      f"\n\n 비밀 키\n"
      f"d : {d}")

# 공개키 등록
# E(a, b), e1, e2는 공개, d는 개인 키
publicKey = publicKeys(a, b, p, e1, e2)




# ---- Alice의 암호화
plainText = 'I love Cryptography! ^_^'

# 공개 키를 이용해 암호화
cypherText = Encrypt(plainText, publicKey.a, publicKey.b, publicKey.p, publicKey.e1, publicKey.e2)




# ---- Bob의 복호화
# 개인 키를 사용하여 복호화
decryptedPlainText = Decrypt(cypherText, d)