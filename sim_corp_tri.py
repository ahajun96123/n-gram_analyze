from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def tri_to_sentence(triSentence):
    tri_list = triSentence.split()
    sentence = tri_list[0]
    for text in tri_list[1:]:
        sentence += text[-1]
    return sentence


def print_max_sim_sentences(lines):
    cv = CountVectorizer()
    y = cv.fit_transform(lines)

    # again = True
    # while again:
    #     max_sim = 0
    #     max_idx = [0, 0]
    #     for sen in lines:
    #         sim = cosine_similarity(y[i], y[j])
    #         if sim > max_sim:
    #             max_sim = sim
    #             max_idx[0], max_idx[1] = i, j
    #         sen1 = tri_to_sentence(lines[max_idx[0]])
    #         sen2 = tri_to_sentence(lines[max_idx[1]])
    #
    #         max_idx[0]
    #
    #         print(sen1)
    #         print(sen2)
    #         print(f'유사도 : {max_sim}\n')
    #     lines.__delitem__(0)

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
        print(f'유사도 : {max_sim}\n')


def print_max_sim_sentence(lines):
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


# asdf = [1, 2, 6, 7, 8, 9, 3, 3, 5]
#
#
# again = True
# while again:
#     print(asdf)
#     for i in asdf:
#         if asdf[0] > i:
#             print(asdf[0], i)
#             asdf.remove(i)
#             break
#     asdf.__delitem__(0)
#     if len(asdf) < 2:
#         again = False
# print(asdf)

f = open(r'C:\Users\lichen\Desktop\국민대\21(4학년)\빅데이터최신기술\text\tri.txt', 'r', encoding='949')
line = f.readlines()
f.close()

print('2) corpus에서 가장 cos 유사도가 높은 문장들의 쌍 출력')
cline = line[:700]
print('유사한 문장들의 쌍 출력')
print_max_sim_sentences(cline)
# print('최대 유사한 문장')
# print_max_sim_sentence(cline)



