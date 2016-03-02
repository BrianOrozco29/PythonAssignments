import string
def equalLetters(inFile):
    inF=open(inFile,'r')
    d={}
    letters=string.printable

    content=inF.readlines()
    for letter in letters:
        reqCount=content[0].count(letter)
        
        if reqCount==0:
              continue
        count=0
        
        for x in range(len(content)-1):  
            
            nextCount=content[x+1].count(letter) 
            if reqCount==nextCount:
                count+=1   
            if count==len(content)-1:
                d[letter]=reqCount
    return d
    inF.close()
print(equalLetters('trouble.txt'))



