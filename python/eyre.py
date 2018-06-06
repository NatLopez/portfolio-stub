#loads package called nltk
import nltk

def open_file_and_get_text(filename):
#given a file name, open it.

    with open (filename, 'r') as our_file:
    #takes the file and reads the text and stores it.
        text = our_file.read()
    return text


def clean_tokens(tokens):
#given tockens, lowercase them

    #create an empty list
    clean_words=[]

    #for each word in list words, loops over and lowercases them
    for word in tokens:
        clean_words.append(word.lower())
    return clean_words

#naming file
our_file = "eyre.txt"

text = open_file_and_get_text(our_file)

words = nltk.word_tokenize(text)
clean_words=clean_tokens(words)

word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts['jane'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])

#print first 99 characters of text
# print(text[0:100])
#
#
# if "The" != "the":
#     print ("Does case matter?")
