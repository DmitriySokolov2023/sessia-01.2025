# Я смог реализовать сжатие с помощью метода KWE (он как раз для текстовых данных)

from collections import Counter

def keyword_encode(text, threshold=2): #threshold - это порог для сжатия, если слово встречается 2 или менее раза, то оно не заменяется индексом
    # Разбиваем текст на слова
    words = text.split()
    # Подсчитываем частоту появления каждого слова
    word_count = Counter(words)
    # Формируем список ключевых слов (слова, которые встречаются больше 'threshold' раз)
    keyword_list = []
    for word, count in word_count.items():
        if count >=threshold:
            keyword_list.append(word)
    # Создаём словарь для ключевых слов, где ключ - слово, а значение - его индекс
    keyword_dict = {}
    for idx, word in enumerate(keyword_list):
        keyword_dict[word] = idx
    # Заменяем каждое ключевое слово на его индекс, остальное оставляем без изменений
    encoded_text = []
    for word in words:
        if word in keyword_dict:
            encoded_text.append(str(keyword_dict[word]))
        else:
            encoded_text.append(word)
    return ' '.join(encoded_text), keyword_dict

# Функция для восстановления текста из сжатого
def keyword_decode(encoded_text, keyword_dict):
    # Переворачиваем словарь, чтобы по индексу получить слово
    reverse_dict = {}
    for word, idx in keyword_dict.items():
        reverse_dict[idx] = word

    # Разбиваем сжатый текст на слова
    encoded_words = encoded_text.split()

    # Восстанавливаем текст, заменяя индексы на соответствующие слова
    decoded_text = []
    for word in encoded_words:
        if word.isdigit():
            decoded_text.append(reverse_dict[int(word)])
        else:
            decoded_text.append(word)
    return ' '.join(decoded_text)

# Пример использования
text = "Проверка использования метода сжатия KWE  KWE сжимает текст, меняя слова на индексы. KWE - сжимает текст текст текст метод метод сжатия сжатия"

# Сжимаем текст (заменяем часто встречающиеся слова)
encoded_text, keyword_dict = keyword_encode(text, threshold=2)
print("Закодированный текст:")
print(encoded_text)

# Восстанавливаем текст из закодированного
decoded_text = keyword_decode(encoded_text, keyword_dict)
print("\nРасшифрованный текст:")
print(decoded_text)