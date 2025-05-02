season_episodes= ["HelpWanted", "ReefBlower", "Tea at the Treedome", "Bubblestand", "Ripped Pants", "Jellyfishing", "Plankton!", "Naughty Nautical Neighbors", "Boating School", "Pizza Delivery", "Home Sweet Pineapple", "Mermaid Man and Barnacle Boy", "Pickles", "Hall Monitor", "Jellyfish Jam", "Sandy's Rocket", "Squeaky Boots", "Nature Pants", "Opoosite Day", "Culture Shock", "F.U.N", "MuscleBob BuffPants", "Squidward the Unfriendly Ghost", "The Chaperone", "Employee of the Mpnth", "Scaredy Pants", "I Was a Teenage Gary", "SB-129", "Karate Choppers", "Sleepy Time", "Suds", "Valentine's Day", "The Paper", "Arrgh!", "Rock Bottom", "Texas", "Walking Small", "Fools In April", "Neptune's Spatula", "Hooky", "Memaid Man and Barnacle Boy II",
                  "Your Shoe's Untied", "Squid's Day Off","Something Smells","Bossy Boots","Big Pink Loser","Bubble Buddy","Dying for Pie","Imitation Krabs","Wormy","Patty Hype","Grandma's Kisses","Squidville", "Prehibernation Week", "Life of Crime", "Christmas Who?",
  "Survival of the Idiots",
  "Dumped",
  "No Free Rides",
  "I'm Your Biggest Fanatic",
  "Mermaid Man and Barnacle Boy III",
  "Squirrel Jokes",
  "Pressure",
  "The Smoking Peanut",
  "Shanghaied",
  "Gary Takes a Bath",
  "Welcome to the Chum Bucket",
  "Frankendoodle",
  "The Secret Box",
  "Band Geeks",
  "Graveyard Shift",
  "Krusty Love",
  "Procrastination",
  "I'm with Stupid",
  "Sailor Mouth",
  "Artist Unknown",
  "Jellyfish Hunter",
  "The Fry Cook Games",
  "Squid on Strike",
  "Sandy, SpongeBob, and the Worm",
  "The Algae's Always Greener",
  "SpongeGuard on Duty",
  "Club SpongeBob",
  "My Pretty Seahorse",
  "Just One Bite",
  "The Bully",
  "Nasty Patty",
  "Idiot Box",
  "Mermaid Man and Barnacle Boy IV",
  "Doing Time",
  "Snowball Effect",
  "One Krabs Trash",
  "As Seen on TV",
  "Can You Spare a Dime?",
  "No Weenies Allowed",
  "Squilliam Returns",
  "Krab Borg",
  "Rock-a-Bye Bivalve",
  "Wet Painters",
  "Krusty Krab Training Video",
  "Party Pooper Pants",
  "Chocolate with Nuts",
  "Mermaid Man and Barnacle Boy V",
  "New Student Starfish",
  "Clams",
  "Ugh",
  "The Great Snail Race",
  "Mid-Life Crustacean",
  "Born Again Krabs",
  "I Had an Accident",
  "Krabby Land",
  "The Camping Episode",
  "Missing Identity",
  "Plankton's Army",
  "The Sponge Who Could Fly",
  "SpongeBob Meets the Strangler",
  "Pranks a Lot"
]

with open('merged.txt', 'w') as outfile:
    for fname in season_episodes:
        path = "SpongeBob_SquarePants_Transcripts/"
        fname = fname.replace(" ", "")
        fname += ".txt"
        
        full_path = path + fname
        try:
            with open(full_path) as infile:
                for line in infile:
                    outfile.write(line)
        except:
            continue
