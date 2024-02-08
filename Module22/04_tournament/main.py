# TODO здесь писать код
with open("first_tour.txt", "r") as f_in, open("second_tour.txt", "w") as f_out:
    k = int(f_in.readline())
    participants = []

    for line in f_in:
        surname, name, score = line.split()
        score = int(score)
        if score > k:
            participants.append((surname, name[0], score))

    participants.sort(key=lambda x: x[2], reverse=True)
    num_participants = len(participants)
    f_out.write(f"{num_participants}\n")

    for i, participant in enumerate(participants):
        surname, name, score = participant
        f_out.write(f"{i+1}) {name}. {surname} {score}\n")
f_in.close()
f_out.close()

first_t = open("first_tour.txt", "r")
second_t = open("second_tour.txt", "r")

print("Содержимое файла first_tour.txt: ")
for f_elem in first_t:
    print(f_elem)

print()
print("-"*10)

print("Содержимое файла second_tour.txt: ")
for s_elem in second_t:
    print(s_elem)
