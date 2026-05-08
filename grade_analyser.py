filename = input("Enter the name of the file that you would like to access: ")

with open(f"{filename}", "r") as f:
    lst = f.readlines()[1:]

lst = [line.strip().split(",") for line in lst]

clean_lst = []

for student in lst:
    stud_id = student
    grades = [float(i) for i in student[1:] if i.strip() != ""]
    avg = sum(grades)/len(grades)

    if avg >= 70:
        group = "1"
    elif avg >= 60:
        group = "2:1"
    elif avg >= 50:
        group = "2:2"
    elif avg >= 40:
        group = "3"
    else:
        group = "F"

    clean_lst.append([stud_id, f"{avg:.2f}", group])

out_file = filename + "_out.csv"

with open(out_file, "w") as f:
    for row in clean_lst:
        f.write(",".join(row) + "\n")
