with open("static/hnr1.abc", "r") as raw_data:
    song_line = ""
    # Read each line in the file and check for the characters which denote each piece of information we require
    # Store the information as a variable and add it to the song_line
    # Once we find a new song (by detecting the line contains X:), wipe out the temp_title variable
    for line in raw_data:
        if "X:" in line:
            temp_title = ""
            song_index = line[2:-1:]
            song_line += (song_index + "...")
        elif "T:" in line:
            # Check if T: already exists in our temp_title variable, meaning we have already captured the title for this
            # song. If found, continue out of the loop (skipping the else statement on line 58)
            if "T:" in temp_title:
                continue
            else:
                # If T: was not found in the temp_title, then capture it in temp_title as is and in title with the
                # correct formatting
                temp_title = line
                title = line[2:-1:]
                song_line += (title + "...")
        elif "M:" in line:
            key_sig = line[2:-1:]
            song_line += ("Key Sig: " + key_sig + "...")
        elif "K:" in line:
            time_sig = line[2::]
            song_line += ("Time Sig: " + time_sig)
    print(song_line)
"""
with open("static/hnr1.abc", "r") as musicfile:
    title=''
    for line in musicfile:
        if line.startswith('X'):
            id=line
            title+=line
"""
        
"""
if f.mode == "r":
    fl =f.readlines()
    for x in fl:
        if x.startswith("X"):
            print(x)
        elif x.startswith("T"):
            print(x)
        elif x.startswith("M"):
            print("Time sig:", x)
        elif x.startswith("K"):
            print("Key sig:", x)
"""