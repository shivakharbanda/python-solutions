def main():
    months = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    while True:
        try:
            date = input("Date:")
            if "/" in date:
                month, date, year = format1(date)
            elif "," in date:
                month, date, year = format2(date, months)
                if month == 'false':
                    raise ValueError('Wrong Format or Invalid Date')
            else:
                raise ValueError('Wrong Format or Invalid Date')
        except ValueError:
            pass

        else:
            if int(month) >=1 and int(month) <= 12 and int(date) <= 31:
                if int(month) < 10 and int(month) > 0:
                        month = "0" + str(month)
                if int(date) < 10 and int(date) > 0:
                        date = "0" + str(date)
                try:
                    print(f"{year}-{month}-{date}")
                    break
                except NameError:
                    print(f"{year}-{month}-{date}")
                    break
            else:
                continue


def format1(date):
    month = 0
    day = 0
    year = 0

    date = date.split("/")

    month = date[0]
    day = date[1]
    year = date[2]

    return month, day, year

def format2(date, months):
    date = date.split(" ")

    month = 0
    day = 0
    year = 0

    month = date[0].title()
    day = date[1].replace(",", "")
    year = date[2]

    if month in months:
        month = months[month]

    else:
        return 'false', 'false', 'false'

    return month, day, year




main()