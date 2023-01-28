new_set = {'sqlmap', 'IronWASP', 'Burp Suite', 'Nikto', 'ATSCAN', 'BruteXSS',
           'WFUZZ'}
new_set = tuple(reversed(sorted(new_set)))

print(str(new_set).replace('(', '').replace(')', ''))
