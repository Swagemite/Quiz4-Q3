while True:
  uinput = input('Enter a word: ')
  if uinput == 'stop':
    break
  elif 'p' in uinput:
    print('True this sting has p')
  else:
    print('This does not contain p')