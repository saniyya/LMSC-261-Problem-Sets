#Problem 3.5


bps = int(input("Enter BPM: ")) / 60
duration_of_song = int(input("Enter song duration in seconds: "))
total_beats = 0
seconds = 1

while(seconds <= duration_of_song):
    total_beats += bps
    print(f"At second {seconds}, total beats: {total_beats}")
    seconds += 1