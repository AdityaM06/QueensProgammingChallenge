import rsa

class Cipher:
    def __init__(self):
        # Make keys
        self.publicKey, self.privateKey = rsa.newkeys(256)
        # Hold another public key for decryption
        self.encryptKey = None

    def addKeyFromString(self, s : str):
        s = s.replace("(", "").replace(")", "").split(", ")
        for i in range(len(s)):
            s[i] = int(s[i])
        self.encryptKey = rsa.PublicKey(s[0], s[1])

    def getPublicKey(self) -> str:
        return str(self.publicKey).replace("PublicKey", "")

    def decrypt(self, msg):
        return rsa.decrypt(msg, self.privateKey)

    def encrypt(self, msg):
        return rsa.encrypt(msg, self.encryptKey)