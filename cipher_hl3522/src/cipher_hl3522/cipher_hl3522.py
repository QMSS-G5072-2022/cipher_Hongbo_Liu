def cipher(text, shift, encrypt=True):
    '''
    The Caesar cipher is one of the simplest and most widely known encryption techniques. In short, each letter is           replaced by a letter some fixed number of positions down the alphabet. Apparently, Julius Caesar used it in his         private correspondence.
    ---------
    Input:
    text: string letter text
    shift: The number of position each letter shift up or down the alphabet
    encrypt: True; The cipher function shift the letters down the alphabet
          False; The cipher function shift the letters up the alphabet
    ---------
    Output: 
    New text after the cipher function
    ---------
    Example:
    Input="test"
    cipher(text = Input, shift = 1, encrypt=True)
    "uftu"
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text