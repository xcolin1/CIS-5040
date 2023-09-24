professors = {}

while True:
    name = input("Enter the professor's name (or Q to quit to see current rattings): ")
    if name == "Q":
        break
    course = input("Enter the course number: ")
    if course not in professors:
        professors[course] = {}
    ranking = int(input("Enter your ranking for this professor (1-10): "))
    if name not in professors[course]:
        professors[course][name] = []
    professors[course][name].append(ranking)

averages = {}
for course, profs in professors.items():
    averages[course] = {}
    for name, rankings in profs.items():
        avg_ranking = sum(rankings) / len(rankings)
        averages[course][name] = avg_ranking

print("Average professor rankings by course:")
for course, profs in averages.items():
    print(f"Course {course}:")
    for name, avg_ranking in sorted(profs.items(), key=lambda x: -x[1]):
        print(f"{name}: {avg_ranking:.2f}")