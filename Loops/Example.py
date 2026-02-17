def get_character_frequencies(word):
    freq_dict = {}
    for character in word:
        character = character.lower()
        if character not in freq_dict:
            freq_dict[character] = 1
        else:
            freq_dict[character] += 1
    return freq_dict

mydict = get_character_frequencies("Snow White and the Seven Dwarves")

# Sort by keys (alphabetically)
print("Sorted by keys (alphabetically):")
sorted_by_keys = dict(sorted(mydict.items()))
print(sorted_by_keys)