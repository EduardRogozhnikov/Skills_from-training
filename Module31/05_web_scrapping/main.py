# TODO здесь писать код
import re
import requests
import json


# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
    text_list = []
# По итогу вы так же получаете код сайта в виде одной строки

    for element in re.findall(r'<h3.*>(.*)</h3>', text):
        text_list.append(element)

    print(text_list)


response = requests.get("http://www.columbia.edu/~fdc/sample.html")  # Можно и через input


with open("examples_2.html", "w+") as f_2:
    f_2.write(response.text)
    text_2 = f_2.read()
    text_list_2 = []

for element in re.findall(r'<h3.*>(.*)</h3>', text_2):
    text_list_2.append(element)

print(text_list)

