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


def tri_to_sentence(triSentence):
    tri_list = triSentence.split()
    sentence = tri_list[0]
    for text in tri_list[1:]:
        sentence += text[-1]
    return sentence


def print_max_sim_sentences(lines):
    global cv
    cv = CountVectorizer()
    y = cv.fit_transform(lines)
    for i in range(len(lines) - 1):
        max_sim = 0
        max_idx = [0, 0]
        for j in range(i + 1, len(lines)):
            sim = cosine_similarity(y[i], y[j])
            if sim > max_sim:
                max_sim = sim
                max_idx[0], max_idx[1] = i, j

        sen1 = tri_to_sentence(lines[max_idx[0]])
        sen2 = tri_to_sentence(lines[max_idx[1]])
        print(sen1)
        print(sen2)
        print(f'유사도 : {max_sim}')
        print()


def print_max_sim_sentence(lines):
    global cv
    cv = CountVectorizer()
    y = cv.fit_transform(lines)
    max_sim = 0
    max_idx = [0, 0]
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            sim = cosine_similarity(y[i], y[j])
            if sim > max_sim:
                max_sim = sim
                max_idx[0], max_idx[1] = i, j

    sen1 = tri_to_sentence(lines[max_idx[0]])
    sen2 = tri_to_sentence(lines[max_idx[1]])
    print(sen1)
    print(sen2)
    print(f'유사도 : {max_sim}')

# Vectors
vec_a = [1, 2, 3, 4, 5]
vec_b = [1, 3, 5, 7, 9]

# Dot and norm
dot = sum(a*b for a, b in zip(vec_a, vec_b))
norm_a = sum(a*a for a in vec_a) ** 0.5
norm_b = sum(b*b for b in vec_b) ** 0.5

# Cosine similarity
cos_sim = dot / (norm_a*norm_b)

# Results
print('My version:', cos_sim)
print('Scikit-Learn:', cosine_similarity([vec_a], [vec_b]))

print('1) 두 문장의 유사도 계산')
sentence1 = input('첫 번째 문장을 입력하세요 : ').strip()
sentence2 = input('두 번째 문장을 입력하세요 : ').strip()

tri_sent_1 = mk_trigram(sentence1)
tri_sent_2 = mk_trigram(sentence2)
cv = CountVectorizer()
X = cv.fit_transform([tri_sent_1, tri_sent_2])

print(f'입력한 두 문장의 유사도 : {cosine_similarity(X[0], X[1])}')


f = open('tri.txt', 'r', encoding='949')
line = f.readlines()
f.close()

# X = cv.fit_transform(corpus)
# print(cv.get_feature_names())
# print(X.toarray())



print('2) corpus에서 가장 cos 유사도가 높은 문장들의 쌍 출력')
cline = line[:1500]
# print_max_sim_sentences(cline)
# print('최대 유사한 문장')
print_max_sim_sentence(cline)



