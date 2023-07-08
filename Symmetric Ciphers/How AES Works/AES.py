import refMethods as e

N_ROUNDS = 10

alpha = []

def encrypt(key, plaintext):
    global alpha
    round_keys = e.expand_key(key, N_ROUNDS)

    #convert plaintext to state matrix
    state = e.bytes2matrix(plaintext)

    # Initial add round key step
    state = e.add_round_key(state, round_keys[0])

    for i in range(N_ROUNDS-1):
        state = e.sub_bytes(state, sbox=e.s_box)
        state = e.shift_rows(state)
        state = e.mix_columns(state)
        state = e.add_round_key(state, round_keys[i+1])

    # Run final round (skips the MixColumns step)
    state = e.sub_bytes(state, sbox=e.s_box)
    state = e.shift_rows(state)
    state = e.add_round_key(state, round_keys[N_ROUNDS])

    # Convert state matrix to ciphertext
    ciphertext = e.matrix2bytes(state)
    alpha = state
    return ciphertext


def decrypt(key, ciphertext):
    round_keys = e.expand_key(key, N_ROUNDS) # Remember to start from the last round key and work backwards through them when decrypting

    # Convert ciphertext to state matrix
    state = e.bytes2matrix(ciphertext)

    # Initial add round key step
    state = e.add_round_key(state, round_keys[N_ROUNDS])

    for i in range(N_ROUNDS - 1, 0, -1):
        state = e.inv_shift_rows(state)
        state = e.sub_bytes(state, sbox=e.inv_s_box)
        state = e.add_round_key(state, round_keys[i])
        state = e.inv_mix_columns(state)


    # Run final round (skips the InvMixColumns step)
    state = e.inv_shift_rows(state)
    state = e.sub_bytes(state, sbox=e.inv_s_box)
    state = e.add_round_key(state, round_keys[0])

    # Convert state matrix to plaintext
    plaintext = e.matrix2bytes(state)

    return plaintext

#plaintext and keyword must be 16 characters long atm
plaintext = "crypto{MYAES128}"
keyword = "obama's mother!!"

#convert keyword to bytes
key = bytes(keyword, 'utf-8')

#encrypt plaintext using key
encr = encrypt(key, bytes(plaintext, 'utf-8'))
print("encr: " + str(encr))

#decrypt ciphertext using key
decr = decrypt(key, encr)
print("decr: " + str(decr))

