
# import rsa
 
# class TestObject(rsa.PublicKey):
#     def __init__(self):
#         self.a = "a"


# # generate public and private keys 
# publicKey, privateKey = rsa.newkeys(256)



# # this is the string that we will be encrypting
# message = "hello geeks"
 
# # rsa.encrypt method is used to encrypt
# encMessage = rsa.encrypt(message.encode(),
#                          publicKey)
 
# print("KEY\n")
# s = str(publicKey).replace("PublicKey(", "").replace(")", "")
# print(s)
# print("")


# s = s.split(", ")
# rsa.PrivateKey()

# print("original string: ", message)
# print("encrypted string: ", encMessage)
 
# # the encrypted message can be decrypted using private key
# decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
# print("decrypted string: ", decMessage)


import pickle, rsa

pubKey, privKey = rsa.newkeys(512)

arr = ['1', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3', '2']
test = ['1', '2', '3', '4', '5', '6']

a = "1"

while a:
    print(a[2:])
    a = a[2:]
