# Conlang-word-generator
콘랭(인공어) 단어 생성기 입니다.

# 사용법
자음:28번째 줄에 consonants라는 리스트가 있는데, 거기에서 자음을 추가하시면 됩니다.

모음:29번째 줄에 vowels라는 리스트가 있는데, 거기에서 모음을 추가하시면 됩니다.

음운 구조: 7번째 줄에서 수정하시면 됩니다. 자음은 C이고 모음은 V입니다. 만약 CV(C)형태로 작성하기를 원할경우 음운 구조를 CV, CVC로 나누어

    syllable_structure = [
      ['C', 'V']
      ['C', 'V', 'C']
    ]

형태로 작성하시면 됩니다.

단어 길이:음운 구조가 정용된 단어의 최소 길이는 31번째 줄에 min_length 값을 수정하고 최대 길이는 max_length에서 수정하시면 됩니다.

생성 단어 개수: 33번째 줄에 num_words에서 수정하시면 됩니다.


# 실행
wordgenerator.py를 수정하지 않고 실행할시

    Random Words: ['Ha', 'Mo', 'Tonrolnu', 'Fuzfuc', 'Dobajfan']

형식으로 나오게 됩니다.
