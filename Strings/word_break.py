# Segment a long string into a set of valid words using a dictionary
seen = {}
def segment(text,words):
    if text in words:
        return text
    if text in seen:
        return seen[text]
    for i in range(1,len(text)+1):
        prefix = text[:i]
        if prefix in words:
            remaining = segment(text[i:],words)
            if remaining is not None:
                return prefix+' '+remaining
    seen[text] = True
        
    

if __name__ == '__main__':
    words = ['temraz','name','is','data','scientist','i','My','machine','learning','algorithms','research',\
             'interests','language','processing','like','developing']
    print segment('Mynameistemraz',words)
    print segment('machinelearningalgorithms',words)
    print segment('hellomachine',words)
    print segment('temraz',words)
