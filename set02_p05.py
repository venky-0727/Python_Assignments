# Student Report Card
def report(name, *marks, **details):
    print(f"{'Student':<10}:{name}")

    for key, value in details.items():
        print(f"{key:10}: {value}")

    # print(f"{'Marks':<10}:{marks}") (10,20,30,40)
    # print(f"{'Marks':<10}:", *marks) 10 20 30 40 
    print(f"{'Marks':<10}: {','.join(map(str, marks))}") #10, 20, 30, 40
    total = sum(marks)
    print(f"{'Total':<10}: {total}")
    print(f"{'Average':<10}: {total/len(marks)}")

    if total/len(marks) >= 40 :
        print(f"{'Result':<10}: PASS")
    else: 
        print(f"{'Result':<10}: FAIL")


report("Priya", 85, 92, 78, 90, section="A", year=2)