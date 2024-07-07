import requests, os

def get_prs():
    username = os.environ['github_username']
    token = os.environ['github_token']
    url = 'https://api.github.com/repos/MSIDDEMO/projectDemo/pulls'
    data = requests.get(url, auth=(username,token))
    print(data.json())

if __name__ == '__main__':
    get_prs()
