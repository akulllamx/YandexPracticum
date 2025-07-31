from operator import index


class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        original_text = original_text.lower()
        for letter in original_text:
            if letter in self.alphabet:
                index = self.alphabet.find(letter)
                shift_index = (index + shift) % len(self.alphabet)
                new_letter = self.alphabet[shift_index]
                result.append(new_letter)
            else:
                result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        result = []
        cipher_text = cipher_text.lower()
        for letter in cipher_text:
            if letter in self.alphabet:
                index = self.alphabet.find(letter)
                shift_index = (index - shift) % len(self.alphabet)
                new_letter = self.alphabet[shift_index]
                result.append(new_letter)
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Привет, как ты?',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))