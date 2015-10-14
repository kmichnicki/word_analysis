##In command line type
##
##for windows:
##type alice.txt | python most_common_words.py number_of_words
import sys
from collections import Counter
from matplotlib import pyplot as plt

num_words=10
all_words=[]
for line in sys.stdin:
    for word in line.strip().split():
        if word:
            all_words.append(word)

counter = Counter(all_words)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")

words=[word for word, count in counter.most_common(num_words)]
xs=[i+0.1 for i,_ in enumerate(words)]
num_times = [counter[i] for i in words]
plt.bar(xs,num_times)


plt.ylabel("# of times the word shows up")
plt.title("Most common words in Alice in Wonderland")



plt.xticks([i+0.5 for i, _ in enumerate(words)],words)
plt.show()

####Find the mean, median and mode
word_lengths=[]
for word in all_words:
    word_lengths.append(len(word))

##find mean word length
num_words=len(word_lengths)
mean =1.0*sum(word_lengths)/num_words
print "The mean length of a word in Alice in Wonderland is: ", mean

##find median
sorted_words=sorted(word_lengths)
if num_words % 2:
    median=1.0*sorted_words[(num_words-1)/2]
else:
    median=0.5*(sorted_words[num_words/2]+counter2.most_common()[num_words/2-1])

print "The median word length of words in Alice in Wonderland is: ", median
    
##find the mode
counter2 = Counter(word_lengths)
x=[length for length, count in counter2.most_common(1)]
mode=x[0]

print "The mode, the most common word, in Alice in Wonderland is: ", mode

xs=[length for length, count in counter2.most_common()]
ys=[count for length, count in counter2.most_common()]

plt.scatter(xs,ys)
plt.title("Frequency of words of a particular length in Alice in Wonderland")
plt.ylabel("Number of words")
plt.xlabel("Length of word")

plt.show()
