import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts}")

    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1