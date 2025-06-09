import re

#names of episodes from season 1 - 4
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
  ,"Fear of a Krabby Patty",
  "Shell of a Man",
  "The Lost Mattress",
  "Krabs vs. Plankton",
  "Have You Seen This Snail?",
  "Skill Crane",
  "Good Neighbors",
  "Selling Out",
  "Funny Pants",
  "Dunces and Dragons",
  "Mermaid Man and Barnacle Boy VI: The Motion Picture",
  "Enemy In-Law",
  "Patrick SmartPants",
  "SquidBob TentaclePants",
  "Krusty Towers",
  "Mrs. Puff, You're Fired",
  "Ghost Host",
  "Wishing You Well",
  "Karate Island",
  "Whale of a Birthday",
  "All That Glitters",
  "New Leaf",
  "Once Bitten",
  "Bummer Vacation",
  "Wigstruck",
  "Squidtastic Voyage",
  "That's No Lady",
  "The Thing",
  "Hocus Pocus",
  "Driven to Tears",
  "Rule of Dumb",
  "Born to Be Wild",
  "Best Frenemies",
  "The Pink Purloiner",
  "Squid Wood"
]

spongebob_s8_to_s13 = [
    # Season 8
    "Accidents Will Happen", "The Other Patty",
    "Drive Thru", "The Hot Shot",
    "A Friendly Game", "Sentimental Sponge",
    "Frozen Face‑Off",
    "Squidward's School for Grown‑Ups", "Oral Report",
    "Sweet and Sour Squid",
    # Season 9
    "Extreme Spots", "Squirrel Record", "Patrick-Man!", "Gary's New Toy",
    "License to Milkshake", "Squid Baby", "Little Yellow Book", "Bumper to Bumper",
    "Eek, an Urchin!", "Squid Defense", "Jailbreak!", "Evil Spatula",
    "It Came from Goo Lagoon", "Safe Deposit Krabs", "Plankton's Pet",
    "Don't Look Now", "Seance Schmeance", "Kenny the Cat", "Yeti Krabs",
    "SpongeBob You're Fired", "Lost in Bikini Bottom", "Tutor Sauce", "Squid Plus One",
    "The Executive Treatment", "Company Picnic", "Pull Up a Barrel", "Sanctuary!",
    "What's Eating Patrick?", "Patrick! the Game", "The Sewers of Bikini Bottom",
    "SpongeBob LongPants", "Larry's Gym", "The Fish Bowl", "Married to Money",
    "Mall Girl Pearl", "Two Thumbs Down", "Sharks vs. Pods", "CopyBob DittoPants",
    "Sold!", "Lame and Fortune", "Goodbye, Krabby Patty?", "The Whole Tooth",

    # Season 10
    "Whirly Brains", "Mermaid Pants", "Unreal Estate", "Code Yellow",
    "Mimic Madness", "House Worming", "Snooze You Lose", "Krusty Katering",
    "SpongeBob's Place", "Plankton Gets the Boot", "Life Insurance", "Burst Your Bubble",
    "Plankton Retires", "Trident Trouble", "The Incredible Shrinking Sponge",

    # Season 11
    "Spot Returns", "The Check-Up", "Spin the Bottle", "There's a Sponge in My Soup",
    "Man Ray Returns", "Larry the Floor Manager", "The Legend of Boo-Kini Bottom",
    "No Pictures Please", "Stuck on the Roof", "Krabby Patty Creature Feature",
    "Teacher's Pests", "Sanitation Insanity", "Bunny Hunt", "Squid Noir",
    "ScavengerPants", "Cuddle E. Hugs", "Patnocchio", "Chatterbox Gary",
    "Don't Feed the Clowns", "Drive Happy", "Old Man Patrick", "Fun-Sized Friends",
    "Grandmum's the Word", "Doodle Dimension", "Moving Bubble Bass", "High Sea Diving",
    "Bottle Burglars", "My Leg!", "Ink Lemonade", "Mustard O' Mine", "Shopping List",
    "Whale Watching", "Krusty Kleaners", "Call the Cops", "Surf N' Turf",
    "Goons on the Moon", "Appointment TV", "Karen's Virus", "The Grill is Gone",
    "The Night Patty", "Bubbletown", "Squirrel Jelly", "The String", "Jolly Lodgers",
    "ChefBob", "Plankton Paranoia", "Library Cards",

    # Season 12
    "FarmerBob", "Gary & Spot", "The Nitwitting", "The Ballad of Filthy Muck",
    "The Krusty Slammer", "Pineapple RV", "Gary's Got Legs", "King Plankton",
    "Plankton's Old Chum", "Stormy Weather", "Swamp Mates", "One Trick Sponge",
    "The Krusty Bucket", "Squid's on a Bus", "Sandy's Nutty Nieces",
    "Insecurity Guards", "Broken Alarm", "Karen's Baby", "Shell Games",
    "Senior Discount", "Mind the Gap", "Dirty Bubble Returns", "Jolly Lodgers",
    "Biddy Sitting", "SpongeBob's Big Birthday Blowout", "SpongeBob in RandomLand",
    "SpongeBob's Bad Habit", "Handemonium", "Breakin'", "Boss for a Day",
    "The Goofy Newbie", "The Ghost of Plankton", "My Two Krabses",
    "Knock Knock, Who's There?", "Pat Hearts Squid", "Lighthouse Louie",
    "Hiccup Plague", "A Cabin in the Kelp", "The Hankering", "Who R Zoo?",
    "Kwarantined Krab", "Plankton's Intern", "Patrick's Tantrum",
    "Bubble Bass's Tab", "Kooky Cooks", "Escape from Beneath Glove World",
    "Krusty Koncessionaires", "Dream Hoppers",

    # Season 13
    "A Place for Pets", "Lockdown for Love", "Under the Small Top", "Squidward's Sick Daze",
    "Goofy Scoopers", "Pat the Dog", "Something Narwhal This Way Comes", "C.H.U.M.S.",
    "SpongeBob's Road to Christmas", "Potato Puff", "There Will Be Grease",
    "The Big Bad Bubble Bass", "Sea-Man Sponge Haters Club", "Food PBFFT! Truck",
    "Upturn Girls", "Say Awww!", "Patrick the Mailman", "Captain Pipsqueak",
    "Plane to Sea", "Squidferatu", "Slappy Daze", "Welcome to Binary Bottom",
    "You're Going to Pay... Phone", "A Skin Wrinkle in Time", "Abandon Twits",
    "Wallhalla", "Salty Sponge", "Karen for Spot", "Arbor Day Disarray",
    "Ain't That the Tooth", "Ma and Pa's Big Hurrah", "Yellow Pavement",
    "The Flower Plot", "SpongeBob on Parade", "Delivery to Monster Island",
    "Ride Patrick Ride", "Hot Crossed Nuts", "Sir Urchin and Snail Fail",
    "Friendiversary", "Mandatory Music", "Dopey Dick", "Plankton and the Beanstalk",
    "My Friend Patty", "FUN-Believable", "Spatula of the Heavens",
    "Gary's Playhouse", "Swimming Fools", "The Goobfather", "SquidBird",
    "Allergy Attack!", "Big Top Flop", "Sandy, Help Us!"
]


with open('old_spongebob.txt', 'w') as outfile:
    for fname in season_episodes:
        fname = re.sub(r'[\W_]', '', fname)
        fname += ".txt"
        path = "SpongeBob_SquarePants_Transcripts/"
        
        
        full_path = path + fname
        try:
            with open(full_path) as infile:
                for line in infile:
                    outfile.write(line)
        except:
            continue
        
with open('new_spongebob.txt', 'w') as outfile:
    for fname in spongebob_s8_to_s13 :
        fname = re.sub(r'[\W_]', '', fname)
        fname += ".txt"
        path = "SpongeBob_SquarePants_Transcripts/"
        
        
        full_path = path + fname
        try:
            with open(full_path) as infile:
                for line in infile:
                    outfile.write(line)
        except:
            continue