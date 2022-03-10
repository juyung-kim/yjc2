length = bream_length + smelt_length
weight = bream_weight + smelt_weight
# 도미, 빙어 전체 길이, 무게 데이터
fish_data = [[l, w] for l, w in zip(length, weight)]
# 도미, 빙어 정답 데이터 (도미: 1, 빙어: 0)
fish_target = [1]*35 + [0]*14
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
# 모델 훈련
kn.fit(fish_data, fish_target)
# 모델 정확도
kn.score(fish_data, fish_target)
# 새로운 데이터 예측
print(kn.predict([[30, 600]]))
