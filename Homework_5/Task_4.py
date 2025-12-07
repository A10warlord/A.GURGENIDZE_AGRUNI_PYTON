
sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."
for c in ',.;:-?!()\'"':
    sentence=sentence.replace(c,'')
sentence=sentence.split() #გადაიქცევა სიად
list(map(lambda x:x.lower(),sentence)) #დაიწერება პატარ ასოებით
max(sentence, key=lambda x:sentence.count(x)) #ყველაზე მეტად გამეორებადი სიტყვა
list(filter(lambda x: len(x) > 3, sentence)) #სიტყვები რომლებიც შეიცავს 3-ზე მეტ ასოს
