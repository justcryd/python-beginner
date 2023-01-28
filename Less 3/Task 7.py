slice_string = ['pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwawm'
                'bbiiigevfrualbsgijbvskfskwczlbervxkmsgtxrfxswmxsibffvaqrabgwxw'
                'cqzcrjiedsizjauufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujgbisagz'
                'swdaeebwerdcluoqvgajabbelaadswzdebwgxvdfaugqjazlwvzejdgleszsrl'
                'qxnsrkbkqcvgwekwsqezll']
word = list(slice_string[0])
word2 = word
letter_one = word[0]
letter_two = word[50]
letter_tree = word[100]
letter_four = word[150]
letter_five = word[200]
letter_six = word[250]

word = [letter_one, letter_two, letter_tree, letter_four, letter_five,
        letter_six]

del word2[1:50]
del word2[2:51]
del word2[3:52]
del word2[4:53]
del word2[5:54]
del word2[6:]

print(''.join(word))
print(''.join(word2))

# slice_string = list(slice_string[0])
# p_to_string = slice_string.index('p')
# y_to_string = slice_string.index('y')
# t_to_string = slice_string.index('t')
# h_to_string = slice_string.index('h')
# o_to_string = slice_string.index('o')
# n_to_string = slice_string.index('n')
# python_string = slice_string[p_to_string], slice_string[y_to_string], \
#    slice_string[t_to_string], slice_string[h_to_string], \
#    slice_string[o_to_string], slice_string[n_to_string]

# print(''.join(python_string))
