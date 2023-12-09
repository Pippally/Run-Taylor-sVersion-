import csv, sys

print("""
.----------------------------------------------------------------------------.
| ____              _____ _ _             _____           _            _     |
||  _ \ _   _ _ __ |  ___(_) |_          |_   _|_ _ _   _| | ___  _ __( )___ |
|| |_) | | | | '_ \| |_  | | __|  _____    | |/ _` | | | | |/ _ \| '__|// __||
||  _ <| |_| | | | |  _| | | |_  |_____|   | | (_| | |_| | | (_) | |    \__ \|
||_| \_\\__,_|_| |_|_|_  |_|\__|           |_|\__,_|\__, |_|\___/|_|    |___/|
|\ \   / /__ _ __ ___(_) ___  _ __                  |___/                    |
| \ \ / / _ \ '__/ __| |/ _ \| '_ \                                          |
|  \ V /  __/ |  \__ \ | (_) | | | |                                         |
|   \_/ \___|_|  |___/_|\___/|_| |_|                                         |
'----------------------------------------------------------------------------'""")

#required task 1 - read the data from the CSV file
def read_data():
    data = []
    with open('TaylorSwiftData.csv', 'r', encoding='utf-8') as TayTayData:
        spreadsheet = csv.DictReader(TayTayData)
        for row in spreadsheet:
            data.append(row)
    return data

read_data()



#Required task 3 = return a total
#For my project i'm totalling the entire time it would take to listen to all of Taylor's music
def discographylength():
    data = read_data()
    tracklengths = []
    for row in data:
        allsongs = int(row['duration_ms'])
        tracklengths.append(allsongs)
        total = sum(tracklengths)
    #code below to convert total of track lenghts into days, minutes, hours and seconds
    convertedlength = total
    convertedlength_s = int(convertedlength/1000)
    convertedlength_m = int(convertedlength_s/60)
    convertedlength_h = int(convertedlength_m/60)
    convertedlength_d = int(convertedlength_h/24)
    #variables for print statement
    days = convertedlength_d
    hours = convertedlength_h%24
    mins = convertedlength_m%60
    secs = convertedlength_s%60
    print(f'The total run time of Taylor Swift\'s entire discography is {days} day, {hours} hours, {mins} minutes and {secs} seconds - that\'s a lot of Tay Tay, happy listening!')



#Calling the function
discographylength()

print("   ")
answer = input("Running for that long is crazy! Do you want to show the length of specific albums? (Y/N) :- ").upper()
if answer == "Y":
    ###################################################################################

    #showing the length of specific albums
    #Demonstrating Required task 2: Collect data into a list
    file_path = 'TaylorSwiftData.csv'

    # Specify the albums to include when calculating the total track length
    # Backslash escapes the apostrophe within the string to avoid breaking the code
    # Only using Taylor's Version's instead of Stolen Version's because Boo You Scooter Braun
    # Not including live tour playlists etc

    target_albums = ['1989 (Taylor\'s Version) [Deluxe]', '1989 (Taylor\'s Version)', 'Speak Now (Taylor\'s Version)'
                     ,'Midnights (3am Edition)', 'Midnights',
                     'Red (Taylor\'s Version)', 'Fearless (Taylor\'s Version)',
                     'evermore (deluxe version)', 'evermore', 'folklore (deluxe version)',
                     'folklore', 'Lover', 'reputation', 'Taylor Swift' ]
    target_albums2 = ['1989 (Taylor\'s Version) [Deluxe]', 'Speak Now (Taylor\'s Version)'
                     ,'Midnights (3am Edition)', 'Red (Taylor\'s Version)', 'Fearless (Taylor\'s Version)',
                     'evermore (deluxe version)', 'folklore (deluxe version)', 'Lover', 'reputation', 'Taylor Swift' ]

    def calculate_total_track_length(file_path, target_albums):
        # Dictionary to store track lengths for each album
        album_lengths = {album: 0 for album in target_albums}
        # Open the CSV file and read data
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Skip the header
            header = next(csv_reader, None)

            # Iterate through rows and calculate total track length for each album
            for row in csv_reader:
                album = row[2]
                song_length_milliseconds = int(row[17])

                # Check if the album is in the specified list
                if album in target_albums:
                    album_lengths[album] += song_length_milliseconds


        return album_lengths



    #Call the function and assign it to a variable)
    calculate_total_track_length(file_path, target_albums)
    result = calculate_total_track_length(file_path, target_albums)

    print('The length of each Taylor Swift Album is...')

    # Print each key-value pair with converted milliseconds into hours, minutes, and seconds
    for album, total_length in result.items():
        convertedlength_s = int(total_length / 1000)
        convertedlength_m = int(convertedlength_s / 60)
        convertedlength_h = int(convertedlength_m / 60)


        # Calculate remaining hours, minutes, and seconds
        hours = convertedlength_h % 24
        mins = convertedlength_m % 60
        secs = convertedlength_s % 60

        print(f"{album}:  {hours} hours, {mins} minutes, {secs} seconds")


##################################################################################

def check_input(user_input, correct_options):
    return user_input in correct_options

# Define the list of correct options
correct_options = ["Y"]

while True:
    print(" ")
    user_input1 = input('Would you like to know the best tracks to run along to for your work out based on desired run speed? (Y/N) : ').upper()
    if check_input(user_input1, correct_options):
        print(" ")
        print("Okay, I like your STYLE...")
        print("   ")
        options = ['1989 (Taylor\'s Version) [Deluxe]', 'Speak Now (Taylor\'s Version]','Midnights (3am Edition)',
                   'Red (Taylor\'s Version)', 'Fearless (Taylor\'s Version', 'evermore (deluxe version)',
                   'folklore (deluxe version)', 'Lover', 'reputation', 'Taylor Swift']

        print("Choose one of the following options:")
        print(" ")
        # Display choices to the user
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print(" ")
        # Take user input
        user_choice1 = input("Enter the number corresponding to your choice: ")
        # Check if the entered value is a valid choice
        if user_choice1.isdigit() and 1 <= int(user_choice1) <= len(options):
            selected_option1 = options[int(user_choice1) - 1]
            print(f"You selected: {selected_option1}")
        break  # Exit the loop if the input is correct
    else:
        print("Okay, YOU'RE ON YOUR OWN KID. BYE!")
        print(" ")
        sys.exit()

#Ask if they want a slow jog, a moderate run or a fast paced work out
print('  ')
print('What level of speed are you going for?')
print('  ')
print("Choose one of the following options:")
print('  ')
workout_options = ['Slow', 'Moderate', 'Fast']
for i, option in enumerate(workout_options, start=1):
    print(f"{i}. {option}")
print(" ")

user_choice2 = input("Enter the number corresponding to your choice: ")
if user_choice1.isdigit() and 1 <= int(user_choice2) <= len(workout_options):
    selected_option2 = workout_options[int(user_choice2) - 1]
    print(f"You selected: {selected_option2}")

print("  ")
print(f'So you want to do a {selected_option2} workout using songs from {selected_option1}...')
print('Here are the tracks I would reccomend:')
print("   ")

def song_selection():
    data = read_data()
    recommendedtracks = []
    a = int(user_choice1)-1
    album_choice = target_albums2[a]

    if int(user_choice2) == 1 :
        for row in data:
            if row["album"] == album_choice and int(row["tempo"]) < 122 and int(row["tempo"]) >= 95 and float(row["energy"]) <=0.7:
                recommendedtracks.append(row["name"])

    elif int(user_choice2) == 2:
        for row in data:
            if row["album"] == album_choice and int(row["tempo"]) < 150 and int(row["tempo"]) >= 122:
                recommendedtracks.append(row["name"])

    elif int(user_choice2) == 3:
         for row in data:
            if row["album"] == album_choice and int(row["tempo"]) >= 150 and float(row["danceability"]) >= 0.4 and float(row["energy"]) >= 0.5:
                recommendedtracks.append(row["name"])

    for i in recommendedtracks:
        print(i)

song_selection()






