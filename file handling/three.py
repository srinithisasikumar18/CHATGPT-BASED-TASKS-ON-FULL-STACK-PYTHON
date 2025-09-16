fp=open('notes.txt','w')
text=('''To generate dummy text (Lorem Ipsum) in VS Code, you can use Emmet abbreviations, which are built-in: Basic Lorem Ipsum.
Type lorem and press Tab. This will generate a standard paragraph of Lorem Ipsum text. Specific Number of Words.
Type lorem followed by the desired number of words, then press Tab. For example, lorem20 will generate 20 words of Lorem Ipsum. Generating Multiple Paragraphs.
You can combine lorem with other Emmet abbreviations. For instance, to generate three paragraphs, each containing five words, type p*3>lorem5 and press Tab. This will create three <p> elements, each filled with five Lorem Ipsum words.
These methods are efficient for quickly inserting placeholder text during development.''')
words=fp.write(text)
fp.close()
print(words)