# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        result = func()

        username = result['name']
        sh_username = username[0] + '*' * (len(username)-2) + username[-1] if len(username) > 1 else username

        password = result['password']
        sh_password = '*' * len(password)

        return {
            'name': sh_username,
            'password': sh_password
        }

    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())