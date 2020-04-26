# -*- coding: utf8 -*-
"""
Функция  транслитерации тувинского кириллического текста в яналиф, принятого в Туве до 1945 года.
Таблица соответствия алфавитов: Д. А. Монгуш. "Тувинский алфавит и его совершенствование
Вопросы совершенствования алфавитов тюркских языков СССР" — М.: «Наука», 1972. — С. 140—148.
Автор: Иргит Валерий
"""


def yanalif(text):
    yan_alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'ƣ', 'h', 'i', 'j', 'ɉ', 'k', 'l', 'm', 'n', 'ꞑ', 'o', 'ө', 'p', 'r',
               's', 'ş', 't', 'u', 'v', 'x', 'y', 'z', 'ƶ', 'ь']

    tuv_alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'ң', 'о', 'ө', 'п', 'р', 'с',
               'т', 'у', 'ү', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    idx_alf = {0: 0, 1: 1, 2: 25, 3: 7, 4: 3, 5: 4, 6: 5, 7: 29, 8: 28, 9: 9, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15,
               15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 23, 22: 24, 23: 27, 24: 5, 25: 26, 26: 21,
               27: 2, 28: 22, 29: 22, 30: 30, 31: 30, 32: 30, 33: 4, 34: 30, 35: 30}


    def ru_position(arr, word):
        """Получаем индекс кирилического алфавита"""
        try:
            return arr.index(word)
        except:
            return 0

    def idx_position(idx_ru):
        """Извлекаем соответствие idx_alf"""
        return idx_alf[idx_ru]

    new_text = []
    for i in text:
        if i.isalpha():
            if i.isupper():
                i = (i.lower())
                idx_ru = ru_position(tuv_alf, i)
                yan_pos = idx_position(idx_ru)
                i = yan_alf[yan_pos]
                i = i.upper()
                new_text.append(i)
            else:
                idx_ru = ru_position(tuv_alf, i)
                yan_pos = idx_position(idx_ru)
                i = yan_alf[yan_pos]
                new_text.append(i)
        else:
            new_text.append(i)

    text = ''.join(new_text)
    return text

