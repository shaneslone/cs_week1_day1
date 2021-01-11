def csMakeItJazzy(chords):
    if len(chords) == 0:
        return chords
    for i, chord in enumerate(chords):
        if chord[len(chord) - 1] != "7":
            chords[i] = chord + "7"
    return chords

