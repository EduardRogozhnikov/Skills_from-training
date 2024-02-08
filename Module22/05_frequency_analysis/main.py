# TODO здесь писать код
from collections import Counter
import string

text_input = "Mama myla ramu"
text_write_file = open("text.txt", 'w')
text_write_file.write(text_input)
text_write_file.close()

text_new_file = open("text.txt", "r")

print("Содержимое файла text.txt:")
for t_elem in text_new_file:
    print(t_elem)

text_new_file.close()

with open("text.txt", "r") as f_in, open("analysis.txt", "w") as f_out:
    text = f_in.read().lower()
    text = "".join(c for c in text if c in string.ascii_lowercase)

    letter_freq = Counter(text)
    total_letters = sum(letter_freq.values())
    letter_freq = {letter: freq / total_letters for letter, freq in letter_freq.items()}
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))

    for letter, freq in sorted_letter_freq:
        f_out.write(f"{letter} {freq:.3f}\n")
f_out.close()
f_out_read = open("analysis.txt", "r")

print("Содержимое файла analysis.txt:")

for f_out_elem in f_out_read:
    print(f_out_elem)
f_out_read.close()
