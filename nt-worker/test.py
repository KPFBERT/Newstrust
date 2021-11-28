import json
from Analysis.AnalysisContents import AnalysisContent
from Analysis.AnalysisTitle import AnalysisTitle
from Analysis.AnalysisScore import AnalysisScore
newsBuffer = []
jsonFilePath = 'test_3_news.json'
with open(jsonFilePath, 'r', encoding='utf-8') as json_file:
    newsBuffer = json.load(json_file)

for targetIndex in range(len(newsBuffer)):
    at = AnalysisTitle(newsBuffer[targetIndex]['title'])
    at.PrintMyValue()
    ac = AnalysisContent(newsBuffer[targetIndex]['content_content'], newsBuffer[0]['provider'], newsBuffer[0]['fix_category'])
    ac.PrintMyValue()
    myAs = AnalysisScore(at, ac)
    myAs.PrintMyValue()