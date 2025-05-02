season1 = ["HelpWanted", "ReefBlower", "Tea at the Treedome", "Bubblestand", "Ripped Pants"]

with open('', 'w') as outfile:
    for fname in season1:
        path = "SpongeBob_SquarePants_Transcripts/"
        fname = fname.replace(" ", "")
        fname += ".txt"
        
        file_path = path + fname
        with open(file_path) as infile:
            for line in infile:
                outfile.write(line)