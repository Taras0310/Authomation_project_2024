import requests
import os

class Github:
    def __init__(self):
        self.base_url = 'https://api.github.com'
        self.github_token = os.getenv("GITHUB_TOKEN")

    def get_user(self, username):
        r = requests.get(f'{self.base_url}/users/{username}' )


class Github:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}' )

        body = r.json()

        return body

    def search_repo(self, name):
        r= requests.get(f'{self.base_url}/search/repositories?q={name}')
        body = r.json()

        return body

    def update_user_info(self,   **kwargs):
        data = {}

        for elem in kwargs:
            data[elem] = kwargs[elem]

        r = requests.patch(f'{self.base_url}/user', headers= {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github+json"
        }, json=data)
        r.raise_for_status()# якщо запит успішний продовжить виконання, ні - поверне помилку
        body = r.json()
        return body

    def get_repo(self,  owner, name):
        r = requests.get(f'{self.base_url}/repos/{owner}/{name}')
        body = r.json()
        r.raise_for_status()
        return body

    def update_repo(self, owner,  current_name, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = current_name#загалом параметр імені обов'язковий, але я зочу шоь можна було оновити декілька значень за раз, тому зразу перевіряю чи є ім'я в kwards якщо ні ставлю поточне

        data = {key: value for key, value in kwargs.items()}

        r = requests.patch(f'{self.base_url}/repos/{owner}/{current_name}', headers={
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github+json"
        }, json=data)
        #r.raise_for_status()  # якщо запит успішний продовжить виконання, ні - поверне помилку ЩЕ ДО ВИКОНАННЯ ASSERT
        return r

    def delete_repo(self,  owner, name):
        data = {}
        r = requests.delete(f'{self.base_url}/repos/{owner}/{name}', headers={
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github+json"
        }, json=data)
        return r # <class 'requests.models.Response'> спеціальний клас з бібліотеки requsest

    def create_repo(self,  **kwargs):
        if 'name' not in kwargs:
            raise ValueError("The 'name' parameter is required.")

        data = {key: value for key, value in kwargs.items()}

        r = requests.post(f'{self.base_url}/user/repos', headers={
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github+json"
        }, json=data)
        #r.raise_for_status()  # якщо запит успішний продовжить виконання, ні - поверне помилку ЩЕ ДО ВИКОНАННЯ ASSERT
        return r

        r= requests.get(f'https://api.github.com/search/repositories?q={name}')
        body = r.json()

        return body

