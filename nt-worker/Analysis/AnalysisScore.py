import json


class AnalysisScore(object):
    def __init__(self, inputAnalysisTitle, inputAnalysisContent):
        self.at = inputAnalysisTitle
        self.ac = inputAnalysisContent
        self.AnalysisNum = 10

        self.News_Aggs = self.getNewsArrgs()
        self.JournalWeight = self.getJournalWeight()
        self.VanillaWeight = self.getVanillaWeight()

        self.Score = {
            "scoreTotal": 0.0,
            "scoreAverage": 0.0,
            "BylineScore": 0.0,
            "ContentLenScore": 0.0,
            "QuotesNumScore": 0.0,
            "TitleLenScore": 0.0,
            "TitleQuestionMarkExclamationMarkScore": 0.0,
            "ContentNumericalCitationNumScore": 0.0,
            "AverageSentenceLenScore": 0.0,
            "TitleAdverbsCountScore": 0.0,
            "AverageAdverbSentenceNumScore": 0.0,
            "AverageQuotesLenScore": 0.0,
        }

        self.Journal = {
            "scoreTotal": 0.0,
            "readability": 0.0,  # 독이성
            "transparency": 0.0,  # 투명성
            "factuality": 0.0,  # 사실성
            "utility": 0.0,  # 유용성
            "fairness": 0.0,  # 균형성
            "diversity": 0.0,  # 다양성
            "originality": 0.0,  # 독창성
            "importance": 0.0,  # 중요성
            "depth": 0.0,  # 심층성
            "sensationalism": 0.0  # 선정성
        }

        self.Vanilla = {
            "scoreTotal": 0.0,
            "readability": 0.0,  # 독이성
            "transparency": 0.0,  # 투명성
            "factuality": 0.0,  # 사실성
            "utility": 0.0,  # 유용성
            "fairness": 0.0,  # 균형성
            "diversity": 0.0,  # 다양성
            "originality": 0.0,  # 독창성
            "importance": 0.0,  # 중요성
            "depth": 0.0,  # 심층성
            "sensationalism": 0.0  # 선정성
        }

        self.BylineScore = self.getBylineScore()  # 바이라인 스코어
        self.ContentLenScore = self.getContentLenScore()  # 기사길이 스코어
        self.QuotesNumScore = self.getQuotesNumScore()  # 인용문수 스코어
        self.TitleLenScore = self.getTitleLenScore()  # 제목 길이 스코어
        self.TitleQuestionMarkExclamationMarkScore = self.getTitleQuestionMarkExclamationMarkScore()  # 제목에 물음표, 느낌표 스코어
        self.ContentNumericalCitationNumScore = self.getContentNumericalCitationNumScore()  # 수치인용 스코어
        self.AverageSentenceLenScore = self.getAverageSentenceLenScore()  # 평균 문장 길이 스코어
        self.TitleAdverbsCountScore = self.getTitleAdverbsCountScore()  # 제목에 평균 부사수 스코어
        self.AverageAdverbSentenceNumScore = self.getAverageAdverbSentenceNumScore()  # 문장당 평균 부사수 스코어
        self.AverageQuotesLenScore = 0  # 인용문 길이 비율 스코어

        self.setScore()
        self.setJournalScore()
        self.setVanillaScore()

    def getNewsArrgs(self):
        # jsonFilePath = './news_aggr/new_news_aggr.json'
        jsonFilePath = './news_aggr/new_news_aggr.json'
        with open(jsonFilePath, 'r', encoding='utf-8') as json_file:
            news_aggBuffer = json.load(json_file)

        makeNewsAggrBuffer = {}
        for aggr in news_aggBuffer:
            category = aggr['category']
            makeNewsAggrBuffer[category] = aggr
        return makeNewsAggrBuffer

    def getJournalWeight(self):
        jsonFilePath = './news_aggr/journal_weight.json'
        with open(jsonFilePath, 'r', encoding='utf-8') as json_file:
            journalWeightBuffer = json.load(json_file)
        return journalWeightBuffer

    def getVanillaWeight(self):
        jsonFilePath = './news_aggr/vanilla_weight.json'
        with open(jsonFilePath, 'r', encoding='utf-8') as json_file:
            vanillaWeightBuffer = json.load(json_file)
        return vanillaWeightBuffer

    def getBylineScore(self):
        byline = self.ac.Byline
        if len(byline[0]) == 0 and len(byline[1]) == 0:  # 둘다 없음
            return -1
        elif len(byline[0]) != 0 and len(byline[1]) != 0:  # 둘다 있음
            return 1
        elif len(byline[0]) != 0 and len(byline[1]) == 0:  # 이름만 있음
            return 0.8
        else:  # 둘중 하나 있음
            return 0

    def getContentLenScore(self):
        targetNewsAggs = self.News_Aggs[self.ac.Category]['contentLength']
        if self.ac.ContentLen <= (targetNewsAggs['avg']):
            return 0
        if self.ac.ContentLen <= (targetNewsAggs['avg'] + 0.5 * targetNewsAggs['sd']):
            return 0.165
        elif self.ac.ContentLen <= (targetNewsAggs['avg'] + targetNewsAggs['sd']):
            return 0.33
        elif self.ac.ContentLen <= (targetNewsAggs['avg'] + 1.5 * targetNewsAggs['sd']):
            return 0.495
        elif self.ac.ContentLen <= (targetNewsAggs['avg'] + 2.0 * targetNewsAggs['sd']):
            return 0.66
        elif self.ac.ContentLen <= (targetNewsAggs['avg'] + 2.5 * targetNewsAggs['sd']):
            return 0.835
        else:
            return 1

    def getQuotesNumScore(self):
        if self.ac.AverageQuotesNum < 15:
            return self.ac.AverageQuotesNum / 15
        else:
            return 1

    def getTitleLenScore(self):
        if self.at.TitleLen <= 45:
            return 0
        else:
            return -1

    def getTitleQuestionMarkExclamationMarkScore(self):
        totalTagets = self.at.QuestionMarkCount + self.at.ExclamationMarkCount
        if totalTagets == 0:
            return 0
        elif totalTagets == 1:
            return -0.5
        else:
            return -1

    def getContentNumericalCitationNumScore(self):
        targetNewsAggs = self.News_Aggs[self.ac.Category]['numNumber']
        if self.ac.ContentNumericalCitationNum < targetNewsAggs['avg']:
            return 0
        elif self.ac.ContentNumericalCitationNum < (targetNewsAggs['avg'] + 0.5 * targetNewsAggs['sd']):
            return 0.33
        elif self.ac.ContentNumericalCitationNum < (targetNewsAggs['avg'] + targetNewsAggs['sd']):
            return 0.66
        else:
            return 1

    def getAverageSentenceLenScore(self):
        targetNewsAggs = self.News_Aggs[self.ac.Category]['avgSentenceLength']
        if self.ac.AverageSentenceLen >= (targetNewsAggs['avg'] + targetNewsAggs['sd']):
            return -1
        else:
            return 0

    def getTitleAdverbsCountScore(self):
        if self.at.TitleAdverbsCount == 1:
            return -0.5
        elif self.at.TitleAdverbsCount >= 2:
            return -1
        else:
            return 0

    def getAverageAdverbSentenceNumScore(self):
        targetNewsAggs = self.News_Aggs[self.ac.Category]['avgAdverbsPerSentence']
        if self.ac.AverageAdverbSentenceNum >= (targetNewsAggs['avg'] + 2 * targetNewsAggs['sd']):
            return -1
        else:
            return 0

    def getAverageQuotesLenScore(self):
        if self.ac.AverageQuotesLen < 0.5:
            return 0
        elif self.ac.AverageQuotesLen < 0.8:
            return -0.5
        else:
            return -1

    def setScore(self):
        scoreTotal = \
            self.BylineScore + \
            self.ContentLenScore + \
            self.QuotesNumScore + \
            self.TitleLenScore + \
            self.TitleQuestionMarkExclamationMarkScore + \
            self.ContentNumericalCitationNumScore + \
            self.AverageSentenceLenScore + \
            self.TitleAdverbsCountScore + \
            self.AverageAdverbSentenceNumScore + \
            self.AverageQuotesLenScore

        scoreAverage = scoreTotal / self.AnalysisNum
        self.Score['scoreTotal'] = scoreTotal
        self.Score['scoreAverage'] = scoreAverage
        self.Score['BylineScore'] = self.BylineScore
        self.Score['ContentLenScore'] = self.ContentLenScore
        self.Score['QuotesNumScore'] = self.QuotesNumScore
        self.Score['TitleLenScore'] = self.TitleLenScore
        self.Score['TitleQuestionMarkExclamationMarkScore'] = self.TitleQuestionMarkExclamationMarkScore
        self.Score['ContentNumericalCitationNumScore'] = self.ContentNumericalCitationNumScore
        self.Score['AverageSentenceLenScore'] = self.AverageSentenceLenScore
        self.Score['TitleAdverbsCountScore'] = self.TitleAdverbsCountScore
        self.Score['AverageAdverbSentenceNumScore'] = self.AverageAdverbSentenceNumScore
        self.Score['AverageQuotesLenScore'] = self.AverageQuotesLenScore


# Jouranl
    def getJournalRead(self):
        val = self.BylineScore * self.JournalWeight['read']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['read']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['read']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['read']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['read'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['read']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['read']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['read']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['read']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['read']['AverageQuotesLenScore']
        return val

    def getJournalClear(self):
        val = self.BylineScore * self.JournalWeight['clear']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['clear']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['clear']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['clear']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['clear'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['clear']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['clear']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['clear']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['clear']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['clear']['AverageQuotesLenScore']

        return val

    def getJournalTruth(self):
        val = self.BylineScore * self.JournalWeight['truth']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['truth']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['truth']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['truth']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['truth'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['truth']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['truth']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['truth']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['truth']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['truth']['AverageQuotesLenScore']

        return val

    def getJournalUseful(self):
        val = self.BylineScore * self.JournalWeight['useful']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['useful']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['useful']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['useful']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['useful'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['useful']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['useful']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['useful']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['useful']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['useful']['AverageQuotesLenScore']

        return val

    def getJournalBalance(self):
        val = self.BylineScore * self.JournalWeight['balance']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['balance']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['balance']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['balance']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['balance'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['balance'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['balance']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['balance']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['balance']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['balance']['AverageQuotesLenScore']

        return val

    def getJournalVariety(self):
        val = self.BylineScore * self.JournalWeight['variety']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['variety']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['variety']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['variety']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['variety'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['variety'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['variety']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['variety']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['variety']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['variety']['AverageQuotesLenScore']

        return val

    def getJournalOriginal(self):
        val = self.BylineScore * self.JournalWeight['original']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['original']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['original']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['original']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['original'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['original'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['original']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['original']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['original']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['original']['AverageQuotesLenScore']

        return val

    def getJournalImportant(self):
        val = self.BylineScore * self.JournalWeight['important']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['important']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['important']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['important']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['important'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['important'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['important']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['important']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['important']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['important']['AverageQuotesLenScore']

        return val

    def getJournalDeep(self):
        val = self.BylineScore * self.JournalWeight['deep']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['deep']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['deep']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['deep']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['deep'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['deep']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['deep']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['deep']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['deep']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['deep']['AverageQuotesLenScore']

        return val

    def getJournalYellow(self):
        val = self.BylineScore * self.JournalWeight['yellow']['BylineScore'] + \
              self.ContentLenScore * self.JournalWeight['yellow']['ContentLenScore'] + \
              self.QuotesNumScore * self.JournalWeight['yellow']['QuotesNumScore'] + \
              self.TitleLenScore * self.JournalWeight['yellow']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.JournalWeight['yellow'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.JournalWeight['yellow']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.JournalWeight['yellow']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.JournalWeight['yellow']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.JournalWeight['yellow']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.JournalWeight['yellow']['AverageQuotesLenScore']

        return val

    def setJournalScore(self):
        self.Journal['readability'] = self.getJournalRead()
        self.Journal['transparency'] = self.getJournalClear()
        self.Journal['factuality'] = self.getJournalTruth()
        self.Journal['utility'] = self.getJournalUseful()
        self.Journal['fairness'] = self.getJournalBalance()
        self.Journal['diversity'] = self.getJournalVariety()
        self.Journal['originality'] = self.getJournalOriginal()
        self.Journal['importance'] = self.getJournalImportant()
        self.Journal['depth'] = self.getJournalDeep()
        self.Journal['sensationalism'] = self.getJournalYellow()

        self.Journal['scoreTotal'] = self.Journal['readability'] + \
                                     self.Journal['transparency'] + \
                                     self.Journal['factuality'] + \
                                     self.Journal['utility'] + \
                                     self.Journal['fairness'] + \
                                     self.Journal['diversity'] + \
                                     self.Journal['originality'] + \
                                     self.Journal['importance'] + \
                                     self.Journal['depth'] + \
                                     self.Journal['sensationalism']


#Vanilla
    def getVanillaRead(self):
        val = self.BylineScore * self.VanillaWeight['read']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['read']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['read']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['read']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['read'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['read']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['read']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['read']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['read']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['read']['AverageQuotesLenScore']
        return val

    def getVanillaClear(self):
        val = self.BylineScore * self.VanillaWeight['clear']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['clear']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['clear']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['clear']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['clear'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['clear']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['clear']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['clear']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['clear']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['clear']['AverageQuotesLenScore']

        return val

    def getVanillaTruth(self):
        val = self.BylineScore * self.VanillaWeight['truth']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['truth']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['truth']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['truth']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['truth'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['truth']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['truth']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['truth']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['truth']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['truth']['AverageQuotesLenScore']

        return val

    def getVanillaUseful(self):
        val = self.BylineScore * self.VanillaWeight['useful']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['useful']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['useful']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['useful']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['useful'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['useful']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['useful']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['useful']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['useful']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['useful']['AverageQuotesLenScore']

        return val

    def getVanillaBalance(self):
        val = self.BylineScore * self.VanillaWeight['balance']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['balance']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['balance']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['balance']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['balance'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['balance'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['balance']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['balance']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['balance']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['balance']['AverageQuotesLenScore']

        return val

    def getVanillaVariety(self):
        val = self.BylineScore * self.VanillaWeight['variety']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['variety']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['variety']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['variety']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['variety'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['variety'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['variety']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['variety']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['variety']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['variety']['AverageQuotesLenScore']

        return val

    def getVanillaOriginal(self):
        val = self.BylineScore * self.VanillaWeight['original']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['original']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['original']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['original']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['original'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['original'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['original']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['original']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['original']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['original']['AverageQuotesLenScore']

        return val

    def getVanillaImportant(self):
        val = self.BylineScore * self.VanillaWeight['important']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['important']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['important']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['important']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['important'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['important'][
                  'ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['important']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['important']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['important']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['important']['AverageQuotesLenScore']

        return val

    def getVanillaDeep(self):
        val = self.BylineScore * self.VanillaWeight['deep']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['deep']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['deep']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['deep']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['deep'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['deep']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['deep']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['deep']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['deep']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['deep']['AverageQuotesLenScore']

        return val

    def getVanillaYellow(self):
        val = self.BylineScore * self.VanillaWeight['yellow']['BylineScore'] + \
              self.ContentLenScore * self.VanillaWeight['yellow']['ContentLenScore'] + \
              self.QuotesNumScore * self.VanillaWeight['yellow']['QuotesNumScore'] + \
              self.TitleLenScore * self.VanillaWeight['yellow']['TitleLenScore'] + \
              self.TitleQuestionMarkExclamationMarkScore * self.VanillaWeight['yellow'][
                  'TitleQuestionMarkExclamationMarkScore'] + \
              self.ContentNumericalCitationNumScore * self.VanillaWeight['yellow']['ContentNumericalCitationNumScore'] + \
              self.AverageSentenceLenScore * self.VanillaWeight['yellow']['AverageSentenceLenScore'] + \
              self.TitleAdverbsCountScore * self.VanillaWeight['yellow']['TitleAdverbsCountScore'] + \
              self.AverageAdverbSentenceNumScore * self.VanillaWeight['yellow']['AverageAdverbSentenceNumScore'] + \
              self.AverageQuotesLenScore * self.VanillaWeight['yellow']['AverageQuotesLenScore']

        return val

    def setVanillaScore(self):
        self.Vanilla['readability'] = self.getVanillaRead()
        self.Vanilla['transparency'] = self.getVanillaClear()
        self.Vanilla['factuality'] = self.getVanillaTruth()
        self.Vanilla['utility'] = self.getVanillaUseful()
        self.Vanilla['fairness'] = self.getVanillaBalance()
        self.Vanilla['diversity'] = self.getVanillaVariety()
        self.Vanilla['originality'] = self.getVanillaOriginal()
        self.Vanilla['importance'] = self.getVanillaImportant()
        self.Vanilla['depth'] = self.getVanillaDeep()
        self.Vanilla['sensationalism'] = self.getVanillaYellow()

        self.Vanilla['scoreTotal'] = self.Vanilla['readability'] + \
                                     self.Vanilla['transparency'] + \
                                     self.Vanilla['factuality'] + \
                                     self.Vanilla['utility'] + \
                                     self.Vanilla['fairness'] + \
                                     self.Vanilla['diversity'] + \
                                     self.Vanilla['originality'] + \
                                     self.Vanilla['importance'] + \
                                     self.Vanilla['depth'] + \
                                     self.Vanilla['sensationalism']

#Print
    def PrintMyValue(self):
        print('----------print Value----------')
        print('BylineScore : ', self.BylineScore)
        print('ContentLenScore : ', self.ContentLenScore)
        print('QuotesNumScore : ', self.QuotesNumScore)
        print('TitleLenScore : ', self.TitleLenScore)
        print('TitleQuestionMarkExclamationMarkScore : ', self.TitleQuestionMarkExclamationMarkScore)
        print('ContentNumericalCitationNumScore : ', self.ContentNumericalCitationNumScore)
        print('AverageSentenceLenScore : ', self.AverageSentenceLenScore)
        print('TitleAdverbsCountScore : ', self.TitleAdverbsCountScore)
        print('AverageAdverbSentenceNumScore : ', self.AverageAdverbSentenceNumScore)
        print('AverageQuotesLenScore : ', self.AverageQuotesLenScore)
        print('Journal : ', self.Journal)
        print('Vanilla : ', self.Vanilla)
        print('----------End Value----------')
