# def of functions randomizing key and maj/min mode

import random

# bank of notes
notes_bank_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notes_bank_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

#sharp tonations
sharp_tonations_major = ("C", "G", "D", "A", "E", "B", "F#", "C#")
sharp_tonations_minor = ( "A", "E", "B", "F#", "C#", "G#", "A#")

#flat tonations
flat_tonations_major = ("F", "Bb", "EB", "Ab", "Db", "Gb", "Cb")
flat_tonations_minor = ("D", "G", "C", "F", "Bb", "Eb", "Ab")


#       ------       major function      ---------

def major_scale_function():
    random_place = random.randint(0, (len(notes_bank_sharp) / 2)-1) #key generator
    if random_place in sharp_tonations_major:
        major_scale = []
        major_scale_semitones = (0,2,4,5,7,9,11,12)
        for i in range(0,13):
            if i in major_scale_semitones: 
                note = notes_bank_sharp[random_place + i]
                major_scale.append(note)
                print(major_scale[0], "maj")
                return major_scale
            else:
                continue
    elif random_place in flat_tonations_major:
        major_scale = []
        major_scale_semitones = (0,2,4,5,7,9,11,12)
        for i in range(0,13):
            if i in major_scale_semitones: 
                note = notes_bank_flat[random_place + i]
                major_scale.append(note)
                print(major_scale[0], "maj")
                return major_scale
            else:
                continue



#       ------       minor function      ---------

def minor_scale_function():
    random_place = random.randint(0, (len(notes_bank_flat) / 2)-1) #key generator
    if random_place in sharp_tonations_minor:
        minor_scale = []
        minor_scale_semitones = (0,2,3,5,7,8,10,12)
        for i in range(0,13):
            if i in minor_scale_semitones:
                note = notes_bank_sharp[random_place + i]
                minor_scale.append(note)
                print(minor_scale[0], "min")
                return minor_scale
            else:
                continue
    elif random_place in flat_tonations_minor:
        minor_scale = []
        minor_scale_semitones = (0,2,3,5,7,8,10,12)
        for i in range(0,13):
            if i in minor_scale_semitones:
                note = notes_bank_flat[random_place + i]
                minor_scale.append(note)
                print(minor_scale[0], "min")
                return minor_scale
            else:
                continue

            

#       ------       random key generator function      ---------

def random_key_generator():
    

    # user can select maj/min or both mode
    print("Which mode you want to select?")
    print("1. = only major")
    print("2. = only minor")
    print("3. = both")
    user_choice = input("Type your choice: ")
    
    if user_choice == 1:
        major_scale_function()
    elif user_choice == 2:
        minor_scale_function()
    else:
        user_choice_mod = random.randint(0,1)
        if user_choice_mod == 1:
            major_scale_function()
        else:
            minor_scale_function()

    
    