def create_csv_file(persons):
    csv_file = open("person_list.csv", "w")
    csv_file.write("First name,Last name,Email,City\n")

    for person in persons:
        csv_file.write("%s,%s,%s,%s\n" % (person.first_name, person.last_name, person.email, person.city))

    csv_file.close()
