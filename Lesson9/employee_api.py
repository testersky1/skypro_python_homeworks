import requests


class ApiEmployee:

    def __init__(self, url) -> None:
        self.url = url

    def auth2(self, login="leonardo", password="leads"):
        body = {
          "username": login,
          "password": password
        }
        response = requests.post(self.url + '/auth/login', json=body)
        return response.json()["userToken"]

    def get_list_employee2(self, params=None):
        response = requests.get(self.url + '/employee' + params)
        return response

    def add_new_employee2(self, body):
        headers = {'x-client-token': self.auth2()}
        response = requests.post(self.url + '/employee/', headers=headers, json=body)
        return response

    def get_new_employee2(self, id):
        response = requests.get(self.url + '/employee/' + str(id))
        return response

    def change_new_employee2(self, id, new_body):
        headers = {'x-client-token': self.auth2()}
        response = requests.patch(self.url + '/employee/' + str(id), headers=headers, json=new_body)
        return response