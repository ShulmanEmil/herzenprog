from urllib.request import urlopen
from bs4 import BeautifulSoup
from natasha import (Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger,
                     NewsSyntaxParser, NewsNERTagger, PER, NamesExtractor,
                     DatesExtractor, Doc)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# парсинг страницы Новости
doc = urlopen(
    "https://www.herzen.spb.ru/main/facts/nowadays/1558542985/1559574321/")
bs = BeautifulSoup(doc, 'lxml')

urls = []
for child1 in bs.recursiveChildGenerator():
    if child1.name == 'td' and child1.get('class'):
        if child1.get('class') == ['blockwh']:
            for child2 in child1.children:
                if child2.name == 'div':
                    for child3 in child2.children:
                        if child3.name == 'p':
                            for child4 in child3.children:
                                if child4.name == 'a':
                                    urls.append(child4.get('href'))
# парсинг каждой новости по url
news_content = []
for url in urls:
    doc = urlopen(url)
    bs = BeautifulSoup(doc, 'lxml')

content = []
for child1 in bs.recursiveChildGenerator():
    if child1.name == 'td' and child1.get('class'):
        if child1.get('class') == ['blockwh']:
            for child2 in child1.children:
                if child2.name == 'h1':
                    content.append(child2.get_text())
                if child2.name == 'div':
                    for child3 in child2.children:
                        if child3.name == 'p':
                            text = child3.get_text()
                            text = text.replace('\xa0', '')
                            text = text.replace('\r\n', ' ')
                            if text != ' ' and text != '':
                                content.append(text)
news_content.append(' '.join(content))

# обработка текста для имен

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)

for_names_cloud = []

for news in news_content:
    doc = Doc(news)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    for span in doc.spans:
        span.normalize(morph_vocab)
        if span.type == PER:
            span.extract_fact(names_extractor)

    for_cloud = [_ for _ in doc.spans if _.type == PER]
    for i in range(len(for_cloud)):
        name = for_cloud[i]
        if name.fact and name.fact.as_dict and name.fact.as_dict.get('last'):
            for_cloud[i] = name.fact.as_dict['last']
        else:
            for_cloud[i] = name.normal

for_names_cloud.append(' '.join(for_cloud))
wordcloud_with_names = WordCloud().generate(' '.join(for_names_cloud))
plt.imshow(wordcloud_with_names, interpolation='bilinear')
f = plt.axis("off")

# обработка текста на ключевые слова

dates_extractor = DatesExtractor(morph_vocab)

keywords = []

for news in news_content:
    dates = list(dates_extractor(news))
    while dates:
        news = news[:dates[0].start] + news[dates[0].stop + 1:]
        dates = list(dates_extractor(news))

    doc = Doc(news)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    for token in doc.tokens:
        token.lemmatize(morph_vocab)

    tokens = [_.lemma for _ in doc.tokens if _.pos == 'NOUN' or _.pos == 'ADJ']

    words = {}
    for t in tokens:
        if t not in words.keys():
            val = 1
        else:
            val = words[t] + 1
        words.update({t: val})

    for k in sorted(words, key=words.get, reverse=True)[:10]:
        keywords.append(k)
        
wordcloud_with_names = WordCloud().generate(', '.join(keywords))
plt.imshow(wordcloud_with_names, interpolation='bilinear')
f = plt.axis("off")
