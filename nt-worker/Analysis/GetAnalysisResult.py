from Analysis.AnalysisTitle import AnalysisTitle
from Analysis.AnalysisContents import AnalysisContent
from Analysis.AnalysisScore import AnalysisScore
import datetime

def makeDateLine(dateLine):
    temp = str(dateLine).split('.')
    myDateLine = datetime.datetime.strptime(temp[0], '%Y-%m-%dT%H:%M:%S')
    myDateLine = myDateLine.isoformat()
    strTemp = str(dateLine).split('T')
    # print(strTemp)
    myStrDateLine = strTemp[0].replace('-', '', 100)
    # print(myStrDateLine)
    return myDateLine, myStrDateLine

def getAnalysisResultToDocument(doc):
    at = AnalysisTitle(inputTitle=doc['title'])
    ac = AnalysisContent(inputContent=doc['content'], inputProvider=doc['provider'], inputCategory=doc['fix_category'])
    myAs = AnalysisScore(inputAnalysisTitle=at, inputAnalysisContent=ac)

    myDoc = {}
    myDoc['news_id'] = doc['news_id']
    myDoc['provider'] = doc['provider']
    myDoc['bigkinds_category'] = doc['category']
    myDoc['bigkinds_byline'] = doc['byline']

    # myDoc['fix_category'] = doc['fix_category']
    myDoc['fix_category'] = ''
    myDoc['fix_byline'] = ac.Byline
    apiTime, strTime = makeDateLine(doc['dateline'])
    myDoc['fix_dateline'] = apiTime
    myDoc['fix_str_dateline'] = strTime

    myDoc['title'] = at.TitleText
    myDoc['title_len'] = at.TitleLen
    myDoc['title_question_mark_count'] = at.QuestionMarkCount
    myDoc['title_exclamation_mark_count'] = at.ExclamationMarkCount
    myDoc['title_adverbs_count'] = at.TitleAdverbsCount
    myDoc['title_doublequotations_marks_num'] = at.TitleDoubleQuotationsMarksNum

    myDoc['content_content'] = ac.Content
    myDoc['remove_content_junk'] = ac.SentenceBuffer
    myDoc['content_mecab_tag'] = ac.MecabTags
    myDoc['content_len'] = ac.ContentLen
    myDoc['content_numerical_citation_num'] = ac.ContentNumericalCitationNum
    myDoc['content_average_sentence_len'] = ac.AverageSentenceLen
    myDoc['content_average_adverb_sentence_num'] = ac.AverageAdverbSentenceNum
    myDoc['content_average_quotes_num'] = ac.AverageQuotesNum
    myDoc['content_average_quotes_len'] = ac.AverageQuotesLen
    myDoc['content_quotes'] = ac.QuotesBuffer
    myDoc['content_people_num'] = ac.PeopleNum
    myDoc['content_people_buffer'] = ac.PeopleBuffer
    myDoc['content_spell_error_num'] = ac.SpellError
    myDoc['content_subjectless_predicate_num'] = ac.Subjectlesspredicate

    myDoc['ntScore'] = myAs.Score
    myDoc['ntJournalScore'] = myAs.Journal
    myDoc['ntVanillaSocre'] = myAs.Vanilla

    return myDoc

