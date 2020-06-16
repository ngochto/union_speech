#hw7.py
#11/26/19
#ClaireTo

#Part1: Word Frequencies
file=open('test.txt','r')
file1=open("state-union-trump.txt",'r', encoding='utf-8', errors='ignore')
file2=open("state-union-clinton.txt",'r', encoding='utf-8', errors='ignore')
file3=open("state-union-gwbush.txt",'r', encoding='utf-8', errors='ignore')
file4=open("state-union-obama.txt",'r', encoding='utf-8', errors='ignore')
#This works as calling the text files.
def toList(filename):
#This function has an argument of a text file, works as spliting the words
#of each line.
    final=[]
    for lines in filename:
        lineLs=lines.split()
        final.extend(lineLs)
    return (final)

def word_freq(filename):
#This function has a filename as its argument and return a tuple containing
#a word count and a word frequency dictionary.
    fileToList = toList(filename)
    count=0
    for el in fileToList:
        count+=1
    temp=(count,)
#Total of words of the entire file.

    wordFreqDictionary={} #an empty dictionary
    freq=0 #base to add for each of the element the function below runs through
    for el in fileToList:
        for i in fileToList:
            if i==el:
                freq+=1
        wordFreqDictionary[el]=freq
        freq=0
    temp+=(wordFreqDictionary,) #add
    return temp

#Part2: Raw Count to Percentage
def freq_to_percentage(filename):
#This function takes a tuple (like that in word_freq) as its argument and
#returns a new dictionary containing all the words/frequency pairs, values associated
#should be percentages instead
    fileToList=toList(filename)
    count=0
    for el in fileToList:
        count+=1
    temp=(count,)
#Count for the number of words. Similar to the part of word_freq
    wordFreqDictionary={}
    freq=0
    for el in fileToList:
        for i in fileToList:
            if i==el:
                freq+=1
        wordFreqDictionary[el]='{:.3%}'.format(freq/count) #Round the percentage to 3
#numbers after the decimal.
        freq=0
    temp+=(wordFreqDictionary,)
    return temp

#Part3: Sorting
def sorting_helper(filename):
#This function takes a file as its argument and return a dictionary
#containing the words and their count in the text.
    fileToList=toList(filename) #split line texts into individual words.
    wordFreqDictionary={} #empty dictionary
    freq=0
    for el in fileToList:
        for i in fileToList:
            if i==el:
                freq+=1
        wordFreqDictionary[el]=freq #count the frequency of each words
        freq=0 #reset freq=0 in order to count for each words, so it does not add up.
    return wordFreqDictionary

def sort_freq(dict):
#This function takes a word frequency dictionary (like that of what sorting_helper
#returns) and returns a list containing all dictionary entries
    ls=list(dict.items()) #convert the dictionary into a list
    temp=[]
    for el in ls:
        temp += [list(el)] #convert each tuple in the list newly created into lists.
#We have lists in a list.

    for el in temp:
        el[0],el[1]=el[1],el[0] #switch position of frequency and the word

    temp=sorted(temp) #sort the frequency (least frequent to most frequent)
    temp=temp[-1::-1] #reverse so that the most frequent words appear first
    temp=temp[0:100] #takes only the most 100 frequent words

    return temp

#Part4: Put it all together
def pretty_print_freqs(ls):
#This function has a list of frequency-word pairs and prints out
#with one paire per line.
    for item in ls:
        print (str(item[0]) + ', ' + "'" + (item[1]) + "'")


def main():
#This function will do the frequency analysis for each of the 4 speech files.
#printing out the sorted list generated as a result of calling functions above.
    print (word_freq(file1))
    print(freq_to_percentage(file1))
    print (pretty_print_freqs(sort_freq(sorting_helper(file1))))
    print (word_freq(file2))
    print(freq_to_percentage(file2))
    print (pretty_print_freqs(sort_freq(sorting_helper(file2))))
    print (word_freq(file3))
    print(freq_to_percentage(file3))
    print (pretty_print_freqs(sort_freq(sorting_helper(file3))))
    print (word_freq(file4))
    print(freq_to_percentage(file4))
    print (pretty_print_freqs(sort_freq(sorting_helper(file4))))

if __name__ == '__main__':
    main()

#Part5: Comparing the 100 most common words.
#What could be learned about each presidents and circumstances of them based on the analysis
#Similarity of the 4: Talks a lot about America, tax, and congress and goverment. This
#shows the general interests of the 4 presidents.

#Differences:
#Trump: says a lot about immigration, signifying that this is one of the problems
#he focuses on most.
#Clinton: says a lot about children and health and security and jobs, signifying that these are
#her interests, different a lot from Trump's interest, even though they are spoken
#in the relatively same time.
#Bush: mostly focuses on security, freedom, terrorism, weapon, iraq, and war. This
#shows us the circumstance that he has to face: the war in Iraq
#Obama: He focuses on education and care, signifying what he does during his presidency: Focus on
#Obamacare
