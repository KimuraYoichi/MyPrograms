"""
次の情報が与えられている.

    1900年1月1日は月曜日である.
    9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
    2月は28日まであるが, うるう年のときは29日である.
    うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.

20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?

"""

from datetime import *

inputlist = []
for yy in range(100):
    for mm in range(1, 13):
        yyyy = 1901 + yy
        ystr = str(yyyy)
        mstr = str(mm)
        inputlist.append(ystr + '/' + mstr + '/1')

print(inputlist)
output = []

yobi = ["月", "火", "水", "木", "金", "土", "日"]

for user_input_date in inputlist:
    try:
        a = datetime.strptime(user_input_date, '%Y/%m/%d')
        if a.weekday() == 6:
            output.append(user_input_date)
            print("{}は{}曜日です".format(user_input_date, yobi[a.weekday()]))
    except ValueError:
        print("誤った日付です")
#     user_input_date = input("your date :")
# else:
#     sys.exit(1)

print(output)
print(len(output))
