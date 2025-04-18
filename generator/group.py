from textwrap import indent

import jsonpickle
import os
import random
import string
import getopt
import sys
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = ".\data\groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# добавлен .replace("`", "") и .replace("'", "") для уменьшения количества падений теста при создании группы
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation.replace("'", "").replace("`", "") + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace("'", "").replace("`", "")


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name",10),
          header=random_string("header", 20),
          footer=random_string("footer", 30))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))