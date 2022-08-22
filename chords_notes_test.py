import random
from all_about_key import*

# bank of notes
notes_bank_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notes_bank_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

#sharp tonations
sharp_tonations_major = ("C", "G", "D", "A", "E", "B", "F#", "C#")
sharp_tonations_minor = ( "A", "E", "B", "F#", "C#", "G#", "A#")


flat_tonations_major = ("F", "Bb", "EB", "Ab", "Db", "Gb", "Cb")
flat_tonations_minor = ("D", "G", "C", "F", "Bb", "Eb", "Ab")



#       ------       chords_notes_test function      ---------

def chord_notes_function():

    #calling random_key_generator function
    key_scale = random_key_generator()
    print(key_scale)
    first_note = key_scale[0]
    # print(first_note)
    
    #checking index of 1st note
    index = notes_bank_sharp.index(first_note)
    # print(index)

    #checking mode of key_scale
    note_check = notes_bank_sharp[index + 4]
    if note_check in key_scale:
        mode = "major"
    else:
        mode = "minor"

    print("Type notes of",key_scale[0], mode, "chord is: ")

    #major/minor input text
    if mode == "major":
        s1 = input("Enter key: ")
        s3 = input("Enter major third: ")
        s5 = input("Enter perfect fifth: ")
    elif mode == "minor":
        s1 = input("Enter key: ")
        s3 = input("Enter minor third: ")
        s5 = input("Enter perfect fifth: ")

    if s1 == key_scale[0] and s3 == key_scale[2] and s5 == key_scale[4]:
        print("Great!")
        print(s1, "  -->  ", key_scale[0])
        print(s3, "  -->  ", key_scale[2])
        print(s5, "  -->  ", key_scale[4])
    else:
        print("Wrong!")
        print(s1, "  -->  ", key_scale[0])
        print(s3, "  -->  ", key_scale[2])
        print(s5, "  -->  ", key_scale[4])