creds = ('__init__', '127.0.0.1', 'admin', 'SupermAn', 'ClOwN',
         'http://site.com', 'humorist', 'https://example.com',
         '192.168.12.101', 12345, 'https://yandex.ru')

logins = ('Logins:', creds[2], creds[6])
passwords = ('Passwords:', creds[3], creds[4])
ips = ('IP:', creds[1], creds[-3])
hosts = ('Hosts:', creds[5], creds[7])

print('\n'.join(logins), '\n')
print('\n'.join(passwords), '\n')
print('\n'.join(ips), '\n')
print('\n'.join(hosts))
