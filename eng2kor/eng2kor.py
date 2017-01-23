BASE_CODE, CHO_CODE, JUNG_CODE = 44032, 588, 28
CHO_LIST = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
JUNG_LIST = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
JONG_LIST = list(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')


class EngHanConverter:
    @staticmethod
    def eng2kor(text):
        pass

    @staticmethod
    def kor2eng(text):
        pass

    @staticmethod
    def combine(cho, jung, jong):
        res = BASE_CODE
        res += 0 if cho == ' ' else CHO_LIST.index(cho) * CHO_CODE
        res += 0 if jung == ' ' else JUNG_LIST.index(jung) * JUNG_CODE
        res += JONG_LIST.index(jong)
        return chr(res)

    @staticmethod
    def split(kor):
        code = ord(kor) - BASE_CODE
        return CHO_LIST[code // CHO_CODE], JUNG_LIST[(code % CHO_CODE) // JUNG_CODE], JONG_LIST[(code % CHO_CODE) % JUNG_CODE]


if __name__ == '__main__':
    print(EngHanConverter.split('뷁'))
    print(EngHanConverter.combine(*EngHanConverter.split('뷁')))