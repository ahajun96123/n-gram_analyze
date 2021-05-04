from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def mk_trigram(text):
    text = text.lower()
    text = text.strip()
    text = text.replace(' ', '_')

    triSentence = ''
    for i in range(len(text) - 2):
        tri = ''.join(text[i:i + 3])
        triSentence += tri + ' '

    return triSentence


print('1) 두 문장의 유사도 계산')
sentence1 = input('첫 번째 문장을 입력하세요 : ').strip()
sentence2 = input('두 번째 문장을 입력하세요 : ').strip()

tri_sent_1 = mk_trigram(sentence1)
tri_sent_2 = mk_trigram(sentence2)
cv = CountVectorizer()
X = cv.fit_transform([tri_sent_1, tri_sent_2])

print(f'입력한 두 문장의 유사도 : {cosine_similarity(X[0], X[1])}')

# X = cv.fit_transform(corpus)
# print(cv.get_feature_names())
# print(X.toarray())


