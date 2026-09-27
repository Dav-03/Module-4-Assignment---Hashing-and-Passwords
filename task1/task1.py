import hashlib
import time
import csv
from pathlib import Path

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
        print("Different digest bytes: ", difference, " of 32 bytes")


def task1C(message, bits):
    digest_bytes = hashlib.sha256(message).digest()
    number = int.from_bytes(digest_bytes, "big")
    return number >> (256 - bits)

#print(task1C(b"Hello dudes",256))
    


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
            
            
            results_file = Path(__file__).with_name("results.csv")
            file_already_exists = results_file.exists()

            with open(results_file, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                if not file_already_exists:
                    writer.writerow([
                        "digest_bits",
                        "attempts",
                        "time_seconds",
                        "first_message",
                        "second_message",
                        "shared_truncated_hash"
                    ])

                writer.writerow([
                    bits,
                    attempts + 1,
                    elapsed_time,
                    seen[number],
                    message,
                    number
                ])
            return

        seen[number] = message
        attempts += 1
 

def run1D():
    i = 0
    while(i < 51):
        print(f"{i}")
        task1D(i)
        i+=1
 
    
def task1E(bits):
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
            
            
            results_file = Path(__file__).with_name("final_results.csv")
            file_already_exists = results_file.exists()

            with open(results_file, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                if not file_already_exists:
                    writer.writerow([
                        "digest_bits",
                        "attempts",
                        "time_seconds",
                        "first_message",
                        "second_message",
                        "shared_truncated_hash"
                    ])

                writer.writerow([
                    bits,
                    attempts + 1,
                    elapsed_time,
                    seen[number],
                    message,
                    number
                ])
            return

        seen[number] = message
        attempts += 1

def run1E():
    i = 8
    while(i < 51):
        print(f"{i}")
        task1E(i)
        i+=2






    
