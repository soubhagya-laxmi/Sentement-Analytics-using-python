import sentiment_mod as s
from nltk.tokenize import sent_tokenize
from nltk.corpus import state_union



sample_text = state_union.raw("E:/Python/NLP/Movie review/sample_data.txt")
new_sample = sent_tokenize(sample_text)

result = []

for i in new_sample[:50]:
    result.append(s.sentiment(i))
    
with open("Output.txt", "w") as text_file:
    text_file.write("Result: {0}".format(result))