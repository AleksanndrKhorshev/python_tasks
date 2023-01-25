# txt = ['ешгапьабво', 'врпп', 'енрпжабврп', 'абв', 'гон', 'абвкрт', 'лавкб']
# txt_filter = filter(lambda x: 'абв' not in x, txt)
# print(list(txt_filter))

number = int(input('Введите количество слов '))
txt = []
for i in range(number):
    list_number = str(input(f'Введите текст {i+1} '))
    txt.append(list_number)
print('Исходный текст: ' + str(list[txt]))
txt_filter = filter(lambda x: 'абв' not in x, txt)
print('Отфильтрованный текст: ' + str(list(txt_filter)))
