# Problem 3.1


song_duration_in_seconds = int(input("Enter song duration in seconds: "))
minutes = song_duration_in_seconds // 60
remaining_seconds = song_duration_in_seconds % 60

print(f"The song duration is {minutes} minutes and {remaining_seconds} seconds.")
