import nacl.utils
from nacl.public import PrivateKey, Box
# Encoded Curve25519 public key.
# skbob = PrivateKey.generate()
# pkbob = skbob.public_key
# skalice = PrivateKey.generate()
# pkalice = skalice.public_key
# bob_box = Box(encrypt_private_key, encrypt_public_key)
# alice_box = Box(skalice, pkbob)
# encrypted = bob_box.encrypt(message, nonce)
# plaintext = alice_box.decrypt(encrypted)
# print(plaintext.decode('utf-8'))

encrypt_private_key = PrivateKey.generate()
decrypt_public_key = encrypt_private_key.public_key
decrypt_private_key = PrivateKey.generate()
encrypt_public_key = decrypt_private_key.public_key


encrypt_box = Box(encrypt_private_key, encrypt_public_key)
decrypt_box = Box(decrypt_private_key, decrypt_public_key)

# message = b"Kill all humans"
# encrypted = encrypt_box.encrypt(message)
# print(encrypted)
#
# plaintext = decrypt_box.decrypt(encrypted)
# print(plaintext.decode('utf-8'))