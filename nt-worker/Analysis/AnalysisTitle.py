# from eunjeon import Mecab
from konlpy.tag import Mecab
class AnalysisTitle(object):

    def __init__(self, inputTitle):
        self.TitleText = self.preProcessTitle(inputTitle) #제목 내용
        self.TitleMecabTag = self.getMecabTag() #제목 mecab tag
        self.TitleLen = self.getTitleLen() #제목 길이
        self.QuestionMarkCount = self.getQuestionMarkCount() #제목에 물음표 갯수
        self.ExclamationMarkCount = self.getExclamationMarkCount() #제목에 느낌표 갯수
        self.TitleAdverbsCount = self.getTitleAdverbsNum() #제목에 평균 부사수
        self.TitleDoubleQuotationsMarksNum = self.getTitleDoubleQuotationsMarksNum() #제목에 쌍따옴표 갯수

    def preProcessTitle(self, title):
        value = title.replace("\n\n", "\n")
        value = value.replace('‘', '\'', -1)
        value = value.replace('’', '\'', -1)
        value = value.replace('“', '\"', -1)
        value = value.replace('”', '\"', -1)
        return value

    def getMecabTag(self):
        mecab = Mecab()
        # mecab = MeCab.Tagger()
        mecabTag = mecab.pos(self.TitleText)
        # mecabTag = mecab.parse(self.TitleText)
        return mecabTag

    def getTitleLen(self):
        TitleLen = len(self.TitleText)
        return TitleLen

    def getQuestionMarkCount(self):
        count = 0
        for val in self.TitleMecabTag:
            if 'SF' in val[1]:
                if '?' == val[0]:
                    count += 1
        return count

    def getExclamationMarkCount(self):
        count = 0
        for val in self.TitleMecabTag:
            if 'SF' in val[1]:
                if '!' == val[0]:
                    count += 1
        return count

    def getTitleAdverbsNum(self):
        count = 0
        for val in self.TitleMecabTag:
            if 'MAG' in val[1] or 'MAJ' in val[1]:
                count += 1
        return count

    def getTitleDoubleQuotationsMarksNum(self):
        count = 0
        for val in self.TitleMecabTag:
            if 'SY' in val[1]:
                if '"' in val[0]:
                    count += 1
        return count

    def PrintMyValue(self):
        print('----------print Analysis Title----------')
        print('TitleText : ', self.TitleText)
        print('TitleMecabTag : ', self.TitleMecabTag)
        print('TitleLen : ', self.TitleLen)
        print('QuestionMarkCount : ', self.QuestionMarkCount)
        print('ExclamationMarkCount : ', self.ExclamationMarkCount)
        print('TitleAdverbsCount : ', self.TitleAdverbsCount)
        print('TitleDoubleQuotationsMarksNum : ', self.TitleDoubleQuotationsMarksNum)
        print('----------End Analysis Title----------')