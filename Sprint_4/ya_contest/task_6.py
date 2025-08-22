import random
import string

class MarsURLEncoder:
    def __init__(self):
        self.prefix = "https://ma.rs/"
        self.url_map = {}
        self.chars = string.ascii_letters + string.digits
        self.code_length = 7

    def _generate_code(self):
        """Генерирует случайный код из разрешённых символов"""
        return ''.join(random.choice(self.chars) for _ in range(self.code_length))

    def encode(self, long_url: str) -> str:
        """Кодирует длинную ссылку в короткую"""
        code = self._generate_code()
        while code in self.url_map:
            code = self._generate_code()
        self.url_map[code] = long_url
        return self.prefix + code

    def decode(self, short_url: str) -> str | None:
        """Декодирует короткую ссылку обратно"""
        code = short_url.replace(self.prefix, "")
        return self.url_map.get(code)


# ==== Пример использования ====
encoder = MarsURLEncoder()

long_url = "https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html"
short_url = encoder.encode(long_url)
print("Короткая:", short_url)   #https://ma.rs/X7NYIol

decoded = encoder.decode(short_url)
print("Декод:", decoded)