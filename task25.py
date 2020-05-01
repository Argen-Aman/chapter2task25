text = str(input('Type something (sentence, text):\n'))

def replace_sign (text):
    sign = ['.', ',' ,':' ,';' ,'!', '?', '(', ')', '[', ']', '{', '}', '-', '"', "'"]
    for i in range(len(sign)):
        text = text.replace(sign[i], '')
    print(text)
replace_sign (text)
