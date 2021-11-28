import copy

from konlpy.tag import Mecab
from newGetByline.byLineParserSelector import getByLineParser
from hanspell import spell_checker

class AnalysisContent(object):

    def __init__(self, inputContent, inputProvider=None, inputCategory=None):

        self.Content = self.preProcessContent(inputContent)  # 본문 내용
        self.Provider = inputProvider  # 언론사
        self.Category = inputCategory  # 카테고리
        self.SentenceBuffer = self.getSentenceBuffer()
        self.MecabTags = self.getMecabTag()  # 본문 형태소분석
        self.ContentLen = self.getContentLen()  # 본문 길이
        self.ContentNumericalCitationNum = self.getContentNumericalCitationNum()  # 본문 수치인용 갯수

        self.AverageSentenceLen = self.getAverageSentenceLen()  # 평균 문장 길이
        self.AverageAdverbSentenceNum = self.getAverageAdverbSentenceNum()  # 문장당 평균 부사수
        self.AverageQuotesNum = self.getAverageQuotesNum()  # 인용문수 평균
        self.AverageQuotesLen, self.QuotesBuffer = self.getAverageQuotesLen()  # 인용문수 길이 비율


        self.PeopleNum, self.PeopleBuffer = self.getPeople() # 인명 정보
        self.SpellError = self.getSpellCheck() #스펠 체크
        self.Subjectlesspredicate = self.getSubjectlesspredicate() #무주체 술어 개수


        if inputProvider != None:
            self.Byline = self.getByline()  # 바이라인
        else:
            self.Byline = None

    def getMecabTag(self):
        mecab = Mecab()
        mecabTagBuffer = []
        for val in self.SentenceBuffer:
            mecabTag = mecab.pos(val)
            mecabTagBuffer.append(mecabTag)
        return mecabTagBuffer

    def preProcessContent(self, content):
        value = content.replace("\n\n", "\n", -1)
        value = value.replace('‘', '\'', -1)
        value = value.replace('’', '\'', -1)
        value = value.replace('“', '\"', -1)
        value = value.replace('”', '\"', -1)
        # print(value)
        return value

    def getSentenceBuffer(self):
        buffer = self.Content.replace('\n', '', -1)
        buffer = buffer.split('.')
        print(len(buffer))
        newBuffer = []
        if buffer[-1]  == 'com':
            buffer[len(buffer)-2] = buffer[len(buffer)-2] +'.'+ buffer[len(buffer)-1]
            for index in range(len(buffer)-1):
                print(buffer[index])
                newBuffer.append(buffer[index])
        elif buffer[-1]  == 'kr':
            buffer[-3] = buffer[-3] +'.'+ buffer[-2] +'.'+ buffer[-1]
            for index in range(len(buffer) - 2):
                newBuffer.append(buffer[index])
        elif buffer[-1]  == 'net':
            buffer[-2] = buffer[-2] +'.'+ buffer[-1]
            for index in range(len(buffer) - 1):
                newBuffer.append(buffer[index])
        else:
            newBuffer = buffer

        print(len(newBuffer))
        for index in range(len(newBuffer)):
            if len(newBuffer[index]) == 0:
                continue
            newBuffer[index] = newBuffer[index] + '.'
        return newBuffer

    def getContentLen(self):
        result = len(self.Content)
        return result

    def getContentNumericalCitationNum(self):
        count = 0
        if len(self.MecabTags) == 0:
            return 0
        for val in self.MecabTags:
            for tag in val:
                if tag[1] == 'SN':
                    count += 1
        return count

    def getAverageSentenceLen(self):
        countBuffer = []
        for val in self.SentenceBuffer:
            countBuffer.append(len(val))
        return sum(countBuffer, 0.0) / len(countBuffer)

    def getAverageAdverbSentenceNum(self):
        countBuffer = []
        if len(self.MecabTags) == 0:
            return 0
        for val in self.MecabTags:
            count = 0
            for tag in val:
                if 'MAG' in tag[1] or 'MAJ' in tag[1]:
                    count += 1
            countBuffer.append(count)
        return sum(countBuffer, 0.0) / len(countBuffer)

    def getAverageQuotesNum(self):
        qStack = []
        popCounter = 0
        if len(self.MecabTags) == 0:
            return 0
        for val in self.MecabTags:
            for tag in val:
                if 'SY' in tag[1] or 'SSO' in tag[1]:
                    if '\'' in tag[0] or '\"' in tag[0]:
                        if len(qStack) == 0:
                            qStack.append(tag[0])
                        elif qStack[-1] == tag[0]:
                            qStack.pop()
                            popCounter += 1
        return popCounter

    def getAverageQuotesLen(self):
        # print("getAverageQuotesLen")
        QuotesBuffer = []
        QuotesLenBuffer = []
        qStack = []
        count = 0
        quotes = ''
        for char in self.Content:

            if char == '\'' or char == '\"':
                if len(qStack) == 0:
                    qStack.append(char)
                    quotes += char
                    # print("stack push : ", char)
                    continue
                else:
                    if qStack[-1] == char:
                        qStack.pop()
                        quotes += char
                        # print("stack pop : ", char)
                        if len(qStack) == 0:
                            # print("Len : ", count)
                            QuotesLenBuffer.append(count)
                            count = 0
                            QuotesBuffer.append(quotes)
                            quotes = ''
                    else:
                        qStack.append(char)
                        quotes += char
            if len(qStack) != 0:
                count += 1
                quotes += char
            else:
                continue
        if len(QuotesLenBuffer) == 0:
            return 0,[]

        # print(sum(QuotesLenBuffer, 0.0), self.ContentLen)
        result = sum(QuotesLenBuffer, 0.0) / self.ContentLen
        return result, QuotesBuffer

    def getByline(self):
        bylineParser = getByLineParser(target=self.Provider)
        # print(bylineParser)
        # print(self.Content)
        nameArray, emailArray = bylineParser.findByLineBase(content=self.Content)
        return nameArray, emailArray

    def getPeople(self):
        m = Mecab()
        tagger = m.tagger.parse(self.Content)
        buff = tagger.split('\n')
        peopleBuffer = []
        peopleNum = 0
        for val in buff:
            if '인명' in val:
                temp = val.split('\t')
                peopleBuffer.append(temp[0])
                peopleNum += 1
        return peopleBuffer, peopleNum

    def getSpellCheck(self):
        content = self.Content[:480]
        try:
            result = spell_checker.check(content)
        except:
            print('Error')
            return 0
        return result.as_dict()['errors']

    def getSubjectlesspredicate(self):
        count = 0
        flag = 0
        if len(self.MecabTags) == 0:
            return 0
        for val in self.MecabTags:
            count = 0
            for tag in val:
                if 'NNB' in tag[1] and '때문' in tag[0]:
                    flag = 1
                if flag == 1:
                    if 'JKB' in tag[1] and '에' in tag[0]:
                        flag = 0
                        count += 1
                    else:
                        flag = 0
        return count


    def PrintMyValue(self):
        print('----------print Analysis Content----------')
        print('Provider : ', self.Provider)
        print('Category : ', self.Category)
        print('ContentLen : ', self.ContentLen)
        print('ContentNumericalCitationNum : ', self.ContentNumericalCitationNum)
        print('AverageSentenceLen : ', self.AverageSentenceLen)
        print('AverageAdverbSentenceNum : ', self.AverageAdverbSentenceNum)
        print('AverageQuotesNum : ', self.AverageQuotesNum)
        print('AverageQuotesLen : ', self.AverageQuotesLen)
        for quo in self.QuotesBuffer:
            print('QuotesBuffer : ', quo)
        print('----------End Analysis Content----------')