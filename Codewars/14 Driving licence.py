def driver(data):
    months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    driving_number = ""
    driving_number += data[2][:5]
    while len(driving_number) < 5:
        driving_number += "9"
    driving_number += data[3][-2]
    month_num = months.get(data[3][3:6])
    if data[4] == "F":
        month_num += 50
        driving_number += str(month_num)
    elif month_num < 10:
        str_month_num = "0" + str(month_num)
        driving_number += str_month_num
    else:
        driving_number += str(month_num)
    driving_number += str(data[3][0:2])
    driving_number += str(data[3][-1])
    driving_number += str(data[0][0])
    if data[1] == "":
        driving_number += "9"
    else:
        driving_number += str(data[1][0])
    driving_number += "9AA"
    driving_number = driving_number.upper()
    return driving_number


#GIBBS862131J9-9AA
driver(["Johanna", "", "Gibbson", "13-Dec-1981", "F"])

#SMITH001010JJ9AA
driver(["John", "James", "Smith", "01-Jan-2000", "M"])

#LEE9980902-1AR9AA
driver(["Andrew", "Robert", "Lee", "02-September-1981", "M"])