#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s[:2])
    ampm = s[8:]

    if ampm == "AM":
        if hour == 12:
            hour = '00'
        else:
            hour = '0' + str(hour)
    else:
        if hour < 12:
            hour = str(hour + 12)
        else:
            hour = str(hour)

    converted = hour + s[2:8]
    return converted


s = input()

result = timeConversion(s)

print(result)
