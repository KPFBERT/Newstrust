from .byLineClass import MainBylineParser


# init
def getByLineParser(target: str):
    target = target.lower()
    # def __init__(self,boardPattenAdd:list,selfPatten:list,includeText:list):
    boardPattern = []
    selfPattern = []
    includeText = []

    if "kbs" in target:
        selfPattern = ["KBS\\s?뉴스\\s?([가-힣]{2,4})\\s?입니다?",
                       "뉴스[,\\s]*([가-힣]{2,4})입니다",
                       "([가-힣]{2,4}) 기잡니다.",
                       "제작:([가-힣]{2,4})",
                       "업그레이드[,\\s]*([가-힣]{2,4})입니다.",
                       "톡톡 ([가-힣]{2,4})입니다."]
        includeText = ["SBS 뉴미디어부"]
        return MainBylineParser(boardPattern, selfPattern, includeText)
    elif "ytn" in target:
        selfPattern = ["([가-힣]{2,4})\\s?\\[email",
                       "YTN ([가-힣]{2,4})입니다.",
                       "([가-힣]{2,4})\\s?PD\\s?\\[email",
                       "([가-힣]{2,4})\\s?기자\\s?\\[email",
                       "뉴스가 있는 저녁 ([가-힣]{2,4})입니다.",
                       "영상 편집 : ([가-힣]{2,4})",
                       "YTN Star ([가-힣]{2,4}) 기자",
                       "구성 ([가-힣]{2,4})",
                       "취재기자: ([가-힣]{2,4})",
                       "YTN PLUS ([가-힣]{2,4}) 기자",
                       "([가-힣]{2,4})\\s?\\(email",
                       "([가-힣]{2,4})\\s?PD\\s?\\(email",
                       "([가-힣]{2,4})\\s?기자\\s?\\(email",
                       "낚시채널 FTV\\s?\\(([가-힣]{2,4})\\)",
                       "VJ ([가-힣]{2,4})"
                       "vj ([가-힣]{2,4})"
                       ]
        boardPattern = ["의 앵커", "앵커", "-VJ", "-구성"]
        includeText = ["에이앤뉴스"]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "mbc" in target:
        selfPattern = ["뉴스\\s?([가-힣]{2,4})\\s?입니다.",
                       ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "obs" in target:
        selfPattern = [
            "([가-힣]{2,4})\\s?\\(email",
            # 김정수(webmaster@obs.co.kr)
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "sbs" in target:
        boardPattern = ["국방전문기자"]
        includeText = ["SBS 뉴미디어부"]
        selfPattern = ["KBC\\s?([가-힣]{2,4})\\s?기자",
                       "([가-힣]{2,4}) SBS 기자"
                       ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "헤럴드경제" in target:
        includeText = ["아트데이"]
        boardPattern = ["건설부동산부"]
        selfPattern = [
            "헤럴드경제\\s?([가-힣]{2,4})\\s?기자",
            "([가-힣]{2,4})\\s?기자"
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "한라일보" in target:
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "한국일보" in target:
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "한국경제" in target:
        includeText = []
        selfPattern = [
            "([가-힣]{2,4})\\s?한경닷컴\\s?기자",
            "([가-힣]{2,4})\\s?한경닷컴\\s?객원",
            "([가-힣]{2,4})\\s?한경닷컴\\s?연예",
            "한경닷컴\\s?([가-힣]{2,4})\\s?기자",
            "([가-힣]{2,4})\\s?기자\\s?email",
            "([가-힣]{2,4}) 뉴스룸 email"
        ]
        boardPattern = ["한국경제신문", "논설위원", "웰스에듀", "여행레저전문기자"]

        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "한겨레" in target:
        boardPattern = ["한국경제신문", "논설위원", "ㅣ논설위원", "객원기자", "선임기자"
            , "책지성팀장", "ㅣ젠더데스크 ", " ㅣ 디지털콘텐츠부", "ㅣ베이징 특파원", "사람과디지털연구소장"
            , "ㅣ에디터부문장", "｜국제부", "ㅣ 저널리즘책무실장"
                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?종교전문기자\\s?email",
            "([가-힣]{2,4})\\s?선임기자\\s?email",
            "([가-힣]{2,4})\\s?기자\\s?email",
            "([가-힣]{2,4})\\s?\\(email",
        ]
        # 김미나 기자 mina@hani.co.kr
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True)
    elif "파이낸셜뉴스" in target:
        boardPattern = ["논설실장", "골프전문기자", "생활경제부장", "정치부장", "정책사회부장",
                        "정보미디어부", "블록체인팀", "부국장", "논설위원", "국제부장"
                        ]
        selfPattern = [
            "email\\s?([가-힣]{2,4})\\s?기자",
        ]
        # 김미나 기자 mina@hani.co.kr
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "충청투데이" in target:
        # boardPattern  = ["논설실장","골프전문기자","생활경제부장","정치부장","정책사회부장",
        # "정보미디어부", "블록체인팀", "부국장","논설위원","국제부장"
        # ]
        # =조재광 기자 cjk9230@cctoday.co.kr
        selfPattern = [
            "\\[충청투데이\\s?([가-힣]{2,4})\\s?기자",
            "\\[충청투데이\\s?([가-힣]{2,4})",
            "([가-힣]{2,4})\\s?기자\\s?email",
            "=([가-힣]{2,4})\\s?기자",

        ]
        # 김미나 기자 mina@hani.co.kr
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "충청일보" in target:
        # boardPattern  = ["논설실장","골프전문기자","생활경제부장","정치부장","정책사회부장",
        # "정보미디어부", "블록체인팀", "부국장","논설위원","국제부장"
        # ]
        # =조재광 기자 cjk9230@cctoday.co.kr
        selfPattern = [
            "\\[충청투데이\\s?([가-힣]{2,4})\\s?기자",
            "\\[충청투데이\\s?([가-힣]{2,4})",
            "([가-힣]{2,4})\\s?기자\\s?email",
            "=([가-힣]{2,4})\\s?기자",

        ]
        # 김미나 기자 mina@hani.co.kr
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    # 충청일보
    elif "충북일보" in target:
        selfPattern = [
            "\\/\\s?([가-힣]{2,4})\\s?기자",
            "사진=([가-힣]{2,4})",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "중앙일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            "제작=([가-힣]{2,4})",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "중부일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    # 중앙일보
    elif "중부매일" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "중도일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부"

                        ]
        selfPattern = [
            "=([가-힣]{2,4})\\s?기자",

        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "조선일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부"
                        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "제민일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부"
                        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "전자신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
                        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)
    elif "전북일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
                        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)
    elif "전북도민일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자"]
        selfPattern = [
            "=([가-힣]{2,4})\\s?기자",

        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)
    elif "전남일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자"]
        selfPattern = [
            "=([가-힣]{2,4})\\s?기자",

        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)
    elif "울산매일" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자"]
        selfPattern = [
            "=([가-힣]{2,4})\\s?기자",

        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)

    elif "영남일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자"]
        selfPattern = [
            "=([가-힣]{2,4})기자",

        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)
    elif "아주경제" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "팀장", "편집국장"]
        selfPattern = [
            "=([가-힣]{2,4})기자",

        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True,
                                            backFirst=True)
    elif "아시아경제" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "팀장", "편집국장"]
        selfPattern = [
            "=([가-힣]{2,4})\\s기자",
            "([가-힣]{2,4})\\s?기자\\s?email"
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "세계일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자"]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            # "([가-힣]{2,4})\\s?email",
            "=([가-힣]{2,4})\\s기자",

            # 현화영 기자 hhy@segye.com
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "서울신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소"]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            # "([가-힣]{2,4})\\s?email",
            "=([가-힣]{2,4})\\s기자",

            # 현화영 기자 hhy@segye.com
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "서울경제" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소"]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            "\\/\\s?([가-힣]{2,4})\\s?email",
            "=([가-힣]{2,4})\\s기자",

            # 현화영 기자 hhy@segye.com
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "부산일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소"]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            "\\/\\s?([가-힣]{2,4})\\s?email",
            "=([가-힣]{2,4})\\s기자",

            # 현화영 기자 hhy@segye.com
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "문화일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소"]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            "\\/\\s?([가-힣]{2,4})\\s?email",
            "=([가-힣]{2,4})\\s기자",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "무등일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            "\\/\\s?([가-힣]{2,4})\\s?email",
            "=([가-힣]{2,4})\\s기자",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "머니투데이" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?email",
            "\\[머니투데이\\s?([가-힣]{2,4})\\s?기자",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "매일신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    # 수정 필요 매일경제!!!!
    elif "매일경제" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "감정평가사"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?email",
            "\\[스타투데이\\s?([가-힣]{2,4})\\s?기자",
            "\\[([가-힣]{2,4})\\s?매일경제",

            # 이종혁 매일경제
            # 스타투데이 양소영 기자
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "디지털타임스" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "동아일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?동아닷컴\\s?기자\\s?email",
            "동아닷컴\\s?([가-힣]{2,4})\\s?\\s?기자\\s?email",
            "동아닷컴\\s?([가-힣]{2,4})\\s?\\s?기자\\s?email",
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "대전일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "대구일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "내일신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "국제신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "국민일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "광주일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "광주매일신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "경향신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "경인일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)
    elif "경상일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "경남신문" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "경남도민일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "경기일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            "=([가-힣]{2,4})\\s?기자",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "강원일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"

                        ]
        selfPattern = [
            # "([가-힣]{2,4})\\s?\\s?기자\\s?email",
            "=([가-힣]{2,4})\\s?기자",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, backContent=True)

    elif "강원도민일보" in target:
        boardPattern = ["정치팀장", "사회2팀장", "고용노동전문기자 email", "종교전문기자", "문화선임기자", "야구팀장", "논설실장"
            , "골프전문기자", "사진전문기자", "문화선임기자", "산업1팀장", "논설위원", "인턴기자", "사회에디터", "고용노동전문기자", "프리랜서"
            , "경제산업부디렉터", "중앙컬처", "경제부장", "시인", "소설가", "경기도박물관장", "경제사회교육부", "정치행정부", "전자신문인터넷"
            , "도민기자", "중부지역본부장", "수습기자", "국제경제팀", "편집국장", "온라인 뉴스", "선임 기자", "평화연구소", "문화부 차장"
            , "취재2부", "취재1부장", "신문제작국", "스포츠부 차장", "편집부국장", "문화전문기자", "교육전문기자", "사회부장", "궁리출판", "논설위원"
            , "강릉본부장"

                        ]
        forceList = [
            "([가-힣]{2,4})",
            "([가-힣]{2,4})\\s?email",
        ]
        LastExcept = [
            "명단", "kado", "첨부파일", "net", "프로필", "관련기사", "▶", "◇"
        ]
        selfPattern = [
            "=\\s?([가-힣]{2,4})\\s?기자$",
            "([가-힣]{2,4})\\s?email$",
            "정리/([가-힣]{2,4})",
            "정리:\\s?([가-힣]{2,4})",
            # "\\/\\s?([가-힣]{2,4})\\s?기자\\s?email",
        ]
        return MainBylineParser(boardPattern, selfPattern, includeText, emailStr=True, FindForceLast=True,
                                            backContent=False,
                                            ForceList=forceList, LastExcept=LastExcept)

# 중앙일보
# 중앙일보

# 아시아경제

# 중앙일보
# 중앙일보


# 전북도민일보
# 중앙일보
# 영남일보