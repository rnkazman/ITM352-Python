def get_character_frequencies(word):
    freq_dict = {}
    for character in word:
        character = character.lower()
        if character not in freq_dict:
            freq_dict[character] = 1
        else:
            freq_dict[character] += 1
    return freq_dict

dict = get_character_frequencies("Snow White and the Seven Dwarves")
print (dict)