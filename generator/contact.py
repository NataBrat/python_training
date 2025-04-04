import getopt
import os
import random
import string
import sys
import jsonpickle
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = ".\data\contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    result = prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])
    # Заменяем двойные пробелы и удаляем пробелы в конце для уменьшения падений теста
    return result.replace("  ", " ").rstrip()

testdata = [Contact(firstname="", lastname="", address="", home="", mobile="",
                    work="", email1="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 10),
            address=random_string("address", 10),
            home=random_string("home", 10),
            mobile=random_string("mobile", 10),
            work=random_string("work", 10),
            email1=random_string("email_1", 10),
            email2=random_string("email_2", 10),
            email3=random_string("email_3", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))