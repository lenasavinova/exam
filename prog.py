import re, os
def opening(name):
    f = open (name, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text
def task1(text):
    res = re.findall('[^А-ЯЁ][^.] ([А-ЯЁ]\. [А-ЯЁ][а-яё].*?)[ .,)(\[]', text)
    for el in res:
        print(el)
task1(opening('zamok.txt'))
def task2(text):
    res1 = re.findall('[^А-ЯЁ][^.] ([А-ЯЁ]\. [А-ЯЁ][а-яё].*?)[ .,)(\[]', text)
    res2 = re.findall(' ([А-ЯЁ]\. [А-ЯЁ]\. [А-ЯЁ][а-яё].*?)[ .,()\[]', text)
    res3 = re.findall(' ([А-ЯЁ][а-яё]+? [А-ЯЁ][а-яё].*?)[ .,()\[]', text)
    resfin = res1 + res2 + res3
    for el in resfin:
        print(el)
    return resfin
def task3(text, resfin):
    m = []
    for el in resfin:
        newel = el.split(' ')
        if len(newel[1]) > 2:
            surn = newel[1]
        else:
            surn = newel[2]    
        m.append(surn)
        for el in m:
            try:
                os.makedirs(el)
            except OSError:
                pass
def main():
    f = opening('zamok.txt')
    t1 = task1(f)
    t2 = task2(f)
    t3 = task3(f, t2)
main()
