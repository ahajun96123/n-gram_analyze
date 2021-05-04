def mk_trigram(text):
    text = text.lower()
    text = text.split('.')
    print(text)
    trigramCnt = {}
    for i in range(len(text)):
        temp = text[i].strip()
        print(temp)
        for j in range(len(temp)-2):
            temps = ''.join(temp[j:j+3])
            temps = temps.replace(' ', '_')
            trigramCnt[temps] = trigramCnt.get(temps, 0) + 1
    return trigramCnt


f = open(r'C:\Users\lichen\Desktop\국민대\21(4학년)\빅데이터최신기술\text\RAW2169-CORE.TXT', 'r')
line = f.readlines()    #list
f.close()

f_tri = open(r'C:\Users\lichen\Desktop\국민대\21(4학년)\빅데이터최신기술\text\tri.txt', 'w')

line = [s.replace(' ', '_') for s in line]

for sentence in line:
    sentence.strip()
    sentence.lower()
    if len(sentence) > 3:
        for i in range(len(sentence)-3):
            tri = ''.join(sentence[i:i+3])
            f_tri.write(tri + ' ')
        f_tri.write('\n')


f_tri.close()

