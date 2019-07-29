
def pluralize(word) :

    if word [-3:] == "ife" :
        return(word [:-3] + "ives")
    if word [-2:] == "sh" or word [-2:
        ] == "ch" :
        return(word + "es")
    if word [-2:] == "us":
        return(word [:-2] + "i")
    if word [-2:] == "ay" or word [-2:] == "oy" or word [-2:] =="ey" or word [-2:] == "uy":
        return(word + "s")
    if word [-1:] == "y" :
        return(word[:-1] + "ies")
    else:
        return (word + "s")

print(pluralize (raw_input("Enter a word: ")))
