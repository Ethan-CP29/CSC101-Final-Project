
import Binge_Class

time_of_recent_drink = []
all_students = []
drinker_students = []
def summary():
    for record in time_of_recent_drink:
        print(record)
    for students in all_students:
        print(students)
    for drinkers in drinker_students:
        print(drinkers)
def highest_incident_rate_recent():
    highest = 0
    for record in all_students:
        if record.percentage > highest:
            highest = record.percentage
    print("Highest Percentage is ",highest," %")
    per_thousand = round(1000/float(highest))
    print("This means for every 1000 people ", per_thousand, "are affected by binge drinking")

def most_likely():
    highest = 0
    i=0
    for record in time_of_recent_drink:
        if record.percentage > highest:
            highest = record.percentage
            i = record
    print("Of 2024,",i.group,"had the highest percentage with", i.percentage,"%")
    print(i)

def average_percentage():
    total_men = 0
    count_men = 0
    total_women = 0
    count_women = 0
    for record in time_of_recent_drink:
        if record.group == 'Cis Men':
            total_men += record.percentage
            count_men += 1
        else:
            total_women += record.percentage
            count_women += 1
    for student in all_students:
        if student.group == 'Cis Men':
            total_men += student.percentage
            count_men += 1
        else:
            total_women += student.percentage
            count_women += 1
    for drinkers in drinker_students:
        if drinkers.group == 'Cis Men':
            total_men += drinkers.percentage
            count_men += 1
        else:
            total_women += drinkers.percentage
            count_women += 1
    avg_men = round(total_men/float(count_men),2)
    avg_women = round(total_women/float(count_women),2)
    print("Mean percentage Women:", avg_women)
    print("Mean Percentage Men:", avg_men)


def main():
    try:
        with open("CalPoly_BingeDrinking.txt", 'r') as file:
            for line in file:
                if not line.startswith('#') and line.strip():
                    if line.startswith('Recent'):
                        line1 = line.split(',')
                        category = line1[0]
                        year = line1[1]
                        term = line1[2]
                        metric = line1[3]
                        group = line1[4]
                        time = line1[5]
                        percent = float(line1[6])
                        time_of_recent_drink.append(Binge_Class.DrinkingInfo(category,year,term,metric,group,time,percent))
                    if line.startswith('Student'):
                        line1 = line.split(',')
                        category = line1[0]
                        year = line1[1]
                        term = line1[2]
                        metric = line1[3]
                        group = line1[4]
                        time = line1[5]
                        percent = float(line1[6])
                        all_students.append(Binge_Class.DrinkingInfo(category,year,term,metric,group,time,percent))
                    if line.startswith('Drinkers'):
                        line1 = line.split(',')
                        category = line1[0]
                        year = line1[1]
                        term = line1[2]
                        metric = line1[3]
                        group = line1[4]
                        time = line1[5]
                        percent = float(line1[6])
                        drinker_students.append(Binge_Class.DrinkingInfo(category,year,term,metric,group,time,percent))
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
