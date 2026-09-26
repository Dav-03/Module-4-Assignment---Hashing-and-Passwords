import hashlib
import time

# Task 1A
messages = [b"Hello dudes", b"Hello ", b"hi"]
def task1A():
    for message in messages:
        digest = hashlib.sha256(message).hexdigest()
        print(digest)


#Task 1B
def task1B():
    for message in messages:
        if len(message) == 0:
            continue

        message1 = bytearray(message)
        message2 = bytearray(message1)
        message2[0] ^= 0b01000000

        bytes1 = hashlib.sha256(message1).digest()
        bytes2 = hashlib.sha256(message2).digest()

        hex1 = bytes1.hex()
        hex2 = bytes2.hex()

        difference = 0

        for byte1, byte2 in zip(bytes1, bytes2):
            if byte1 != byte2:
                difference += 1

        print("-----")
        print("Original message:", bytes(message1))
        print("Changed message: ", bytes(message2))
        print("Hash 1: ", hex1)
        print("Hash 2: ", hex2)
        print("Different digest bytes: ", difference, "of of 32 bytes")



def task1C(message, bits):
    bytes = hashlib.sha256(message).digest()
    number = int.from_bytes(bytes, "big")
    return number >> (256 - bits)

#print(task1C(b"Hello dudes", 100))
    


def task1D(bits):
    seen = {}
    attempts = 0
    startTimer = time.perf_counter()

    while True:
        message = f"message-{attempts}".encode()
        number = task1C(message, bits)

        if number in seen:
            elapsed_time = time.perf_counter() - startTimer

            print("Collision found was found")
            print("First message:", seen[number])
            print("Second message:", message)
            print("Shared hash:", number)
            print("Attempts:", attempts + 1)
            print("Time:", elapsed_time, "seconds")

            return

        seen[number] = message
        attempts += 1
        

#task1D(40)
        
    
    
    
    
    

#def task1E():

#def task1F():

#def task1G():

#def task1H():

#def task1I():

#def task1J():



    
