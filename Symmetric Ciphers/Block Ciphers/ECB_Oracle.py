import requests
import threading

url = f"https://aes.cryptohack.org/ecb_oracle/encrypt/"

size = 0
info = ""

cryptend = "}".encode().hex()
end = ""
threadnum = 32
hex = ""
check = False
print(cryptend)

def threadAttempt(start):
    global end
    global hex
    global check
    global threadnum
    for a in range(0,pow(16,2)//threadnum):
        if check:
            break
        r = requests.get(f"{url}{(64 - len(end)-2)*'0'}{end}{'{:02x}'.format(a+start)}")
        data = r.json()
        if data["ciphertext"][0:64] == hex:
            print(f"{url}{(64 - len(end) - 2) * '0'}{end}{'{:02x}'.format(a + start)}")
            end += '{:02x}'.format(a+start)
            check = True
            break


threads = []
while end[-2:] != cryptend:
    r = requests.get(f"{url}{(64 - len(end)-2)*'0'}")
    data = r.json()
    hex = data["ciphertext"][0:64]
    check = False
    for thr in range(threadnum):
        thread = threading.Thread(target=threadAttempt, args=(thr*pow(16,2)//threadnum,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(bytes.fromhex(end))



print(bytes.fromhex(end))
