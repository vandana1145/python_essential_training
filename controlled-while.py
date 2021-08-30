secret = 'Solitary Walker'
count = 0
word = ''
auth = False
max_attempt = 7

while word != secret:
    count += 1
    if count > max_attempt: break
    if count == 5: continue
    word = input(f'{count}: What is the secret handler? ')
else:
    auth = True


print("You're Authorized" if auth else "Calling the Deutsch Polizie.")