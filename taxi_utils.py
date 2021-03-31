from IPython.display import Markdown
from IPython.display import display

def md(input):
    display(Markdown(input))

def step(input):
    return md(f"✅ *{input}*")

def kv(key, value):
    return md("**{}** : {}".format(key, value))