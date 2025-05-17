#1: add 'ing' to the end of every word, and 'ly' to the end of every word that already ends with 'ing'. Words must be ATLEAST 3 letters long
endAdd = 'ing'
endAdd2 = 'ly'

x = 'Abd'

if len(x) <= 3:
    print(x)
elif x[-3:len(x)] != 'ing':
    print(x + endAdd)
elif x[-3:] == 'ing':
    print(x + endAdd2)