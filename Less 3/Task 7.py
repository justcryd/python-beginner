slice_string = ['pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwawm'
                'bbiiigevfrualbsgijbvskfskwczlbervxkmsgtxrfxswmxsibffvaqrabgwxw'
                'cqzcrjiedsizjauufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujgbisagz'
                'swdaeebwerdcluoqvgajabbelaadswzdebwgxvdfaugqjazlwvzejdgleszsrl'
                'qxnsrkbkqcvgwekwsqezll']
slice_string = list(slice_string[0])
p_to_string = slice_string.index('p')
y_to_string = slice_string.index('y')
t_to_string = slice_string.index('t')
h_to_string = slice_string.index('h')
o_to_string = slice_string.index('o')
n_to_string = slice_string.index('n')
python_string = slice_string[p_to_string], slice_string[y_to_string], \
    slice_string[t_to_string], slice_string[h_to_string], \
    slice_string[o_to_string], slice_string[n_to_string]

print(''.join(python_string))
