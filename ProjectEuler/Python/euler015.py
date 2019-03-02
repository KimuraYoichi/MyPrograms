"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters

and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.

では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.

注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は 23 文字,
115 (one hundred and fifteen) は20文字と数える. なお, "and" を使用するのは英国の慣習.
"""

numlettersdic ={}

numlettersdic[1]='one'
numlettersdic[2]='two'
numlettersdic[3]='three'
numlettersdic[4]='four'
numlettersdic[5]='five'
numlettersdic[6]='six'
numlettersdic[7]='seven'
numlettersdic[8]='eight'
numlettersdic[9]='nine'
numlettersdic[10]='ten'
numlettersdic[11]='eleven'
numlettersdic[12]='twelve'
numlettersdic[13]='thirteen'
numlettersdic[14]='fourteen'
numlettersdic[15]='fifteen'
numlettersdic[16]='sixteen'
numlettersdic[17]='seventeen'
numlettersdic[18]='eighteen'
numlettersdic[19]='nineteen'
numlettersdic[20]='twenty'
numlettersdic[30]='thirty'
numlettersdic[40]='forty'
numlettersdic[50]='fifty'
numlettersdic[60]='sixty'
numlettersdic[70]='seventy'
numlettersdic[80]='eighty'
numlettersdic[90]='ninety'
numlettersdic[100]='hundred'
numlettersdic[1000]='thousand'
numlettersdic[1000000]='million'
numlettersdic[1000000000]='billion'
numlettersdic[1000000000000]='trillion'

def under100(n):
    under100numletters = ""
    if n < 21:
        under100numletters += numlettersdic[n]
    else:
        if n%10 == 0:
            under100numletters += numlettersdic[n]
        else:
            under100numletters += numlettersdic[int(n/10) * 10] +numlettersdic[n - int(n/10) * 10]
    return under100numletters


print(numlettersdic)
numletter = ""

for i in range(1, 1001):
    print(i)
    if i == 1000:
        numletter = numletter + 'onethousand'
        break
    else:
        if i < 100:
            numletter += under100(i)
        else:
            if i%100 == 0:
                numletter += under100(int(i / 100)) + numlettersdic[100]
            else:
                numletter += under100(int(i/100)) + numlettersdic[100] + 'and' + under100(i - int(i/100) * 100)


# print(numletter)
print(len(numletter))