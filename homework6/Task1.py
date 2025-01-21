text = (
    'Etiam tincidunt neque erat, quis molestie '
    'enim imperdiet vel. Integer urna nisl, '
    'facilisis vitae semper at, dignissim vitae libero'
)
words = text.split()
update_text = []
for value in words:
    if ',' in value or '.' in value:
        ttt = f'{value[:-1]}ing{value[-1]}'
        update_text.append(ttt)
    else:
        ttt = f'{value}ing'
        update_text.append(ttt)
print(update_text)
print(' '.join(update_text))

