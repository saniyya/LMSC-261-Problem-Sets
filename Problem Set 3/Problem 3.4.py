# Problem 3.4


song_duration = int(input("Enter song duration: "))

if song_duration < 2:
    print(f"Short Song")

elif 2 >= song_duration <= 4:
    print(f"Medium Song")

else:
    print(f"Long Song")