# dateconvert.py
#  Convert a data in form "mm/dd/yyyy" to "month day, year"

def main():
    # get the date
    datestr = input("Enter a date (mm/dd/yyyy):")

    # split into components
    monthstr, daystr, yearstr = datestr.split("/")

    # convert monthStr to the month name
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    monthstr = months[int(monthstr)-1]
    # output result in month day, year format
    print("The converted data is:",monthstr,daystr+",", yearstr)


main()