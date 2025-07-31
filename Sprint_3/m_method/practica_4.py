class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        text = text.lower()
        if is_encrypt == True:
            for letter in text:
                if letter in self.alphabet:
                    index = self.alphabet.find(letter)
                    new_index = (index + shift) % len(self.alphabet)
                    new_letter = self.alphabet[new_index]
                    result.append(new_letter)
                else:
                    result.append(letter)
            return ''.join(result)
        else:
            for letter in text:
                if letter in self.alphabet:
                    index = self.alphabet.find(letter)
                    new_index = (index - shift) % len(self.alphabet)
                    new_letter = self.alphabet[new_index]
                    result.append(new_letter)
                else:
                    result.append(letter)
            return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))