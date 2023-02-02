ip_adresses = '192.168.1.1', '10.10.1.5', '8.8.8.8', '8.8.4.4'
wordlist = {123456, 'Password', 12345, 123456789, 'password1'}
result = {22: ("ssh", "OpenSSH 7.6"), 25: ("smtp", "Postfix smtpd"),
          80: ("http", "Nginx 1.14.0")}

print('ip_adresses', type(ip_adresses))
print('wordlist', type(wordlist))
print('result', type(result))
