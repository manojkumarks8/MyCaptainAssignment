import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(info_list)


if __name__ == '__main__':
    condition = True
    student_num = 1
    while condition:
        student_info = input("Enter student #{} information in the following format(Name Age Contact_no Email_id): "
                             "".format(student_num))
        print("Entered info: ", student_info)

        student_info_list = student_info.split(' ')
        print("Entered split up info: ", str(student_info_list))

        print("The entered info:\nName: {}\nAge: {}\nContact_no.: {}\nEmail_id: {}"
              "".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        ch_check = input("Is the entered info correct? (yes/no): ")
        if ch_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input("Enter Yes/No if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
            else:
                print("Enter valid statement")
        elif ch_check == "no":
            print("Re-enter")
