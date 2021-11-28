import re
import json
import regex


class MainBylineParser():
    boardParsingList = ["기상캐스터", "해설위원", "특파원", "기상 캐스터", "앵커리포트", "PLUS", "선임기자",
                        "한경닷컴", "군사전문기자", "의학전문기자", "기상 캐스터", "촬영기자", "사건팀장", "기상전문기자", "국방전문기자",
                        "의학기자", "의학 기자", "국방 전문"]
    bylinePattennamePatten = re.compile('([가-힣]{2,4})\\s기자')
    email = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+')
    selfPattern = []
    emailInfo = []
    bylineInfo = []
    checkNoNameValue = {"기자": 0, "뉴스": 0, "온라인": 0, "사진": 0, "": 0, "선임": 0, "특파원": 0,
                        "세계일보": 0, "자료사진": 0, "인턴": 0, "게티이미지": 0, "뱅크": 0, "제공": 0, "연합뉴스": 0, "공동취재단": 0
        , "전국종합": 0, "산업부": 0, "사무국장": 0, "부산닷컴": 0, "인턴": 0
        , "취재": 0, "촬영": 0, "는": 0, "기자회견": 0, "연결합니": 0, "연결": 0, "연결해": 0, "코너": 0, "해설": 0,
                        "방송": 0, "의학전문": 0, "조선일보": 0, "설비": 0, "이날": 0}
    checkErrorValue = ["연결", "코너", "풀어", "질문", "입니", "불러", "국회", "회견", "확인", "설비", "를"]
    boardBackCompile = {}
    boardFrontCompile = {}
    includeText = []
    contents = []
    backPatten = True
    emailStr = False
    bylineBaseBack = re.compile('([가-힣]{2,4})\\s?기자')
    bylineBaseFront = re.compile('기자\\s?([가-힣]{2,4})')
    peopleName = re.compile('([가-힣]{2,4})')
    bylinePreFix = re.compile('([가-힣]{2,6})기자')
    backContent = False
    backFirst = False
    LastForcePattern = []

    def __init__(self, boardPattenAdd: list, selfPatten: list, includeText: list, backPatten=True, emailStr=False,
                 backContent=False, backFirst=False, FindForceLast=False, ForceList=[], LastExcept=[]
                 ):
        self.boardParsingList.extend(boardPattenAdd)
        self.includeText = includeText
        self.backPatten = backPatten
        self.emailStr = emailStr
        self.backContent = backContent
        self.backFirst = backFirst
        self.FindForceLast = FindForceLast
        self.ForceList = ForceList
        self.LastExcept = LastExcept
        for reP in selfPatten:
            self.selfPattern.append(re.compile(reP))
        for reP in ForceList:
            self.LastForcePattern.append(re.compile(reP))
        for board in self.boardParsingList:
            self.boardBackCompile[board] = re.compile('([가-힣]{2,4})\\s?' + board)
            self.boardFrontCompile[board] = re.compile(board + '\\s?([가-힣]{2,4})')

    def __checkEmail(self, content):
        res = self.email.findall(content)
        emailArray = []
        if len(res) != 0:
            emailArray = res
            for email in res:
                if self.emailStr:
                    content = content.replace(email, "email")
                else:
                    content = content.replace(email, "")

            emailArray = res
        return content, emailArray

    def __splitSentence(self, content: str):
        contents = []
        for con in regex.split("[\n]", content):
            con = con.strip()
            if len(con) == 0:
                continue
            if "." in con and "@" not in con:
                innerCon = con.split(".")
                contents.extend([line.strip() for line in innerCon if len(line.strip()) != 0])
            else:
                contents.append(con)
        return contents

    def __getBylineUsingPattern(self, content: str, pattern):
        nameArray = pattern.findall(content)
        resArray = []
        if len(nameArray) != 0:
            for name in nameArray:
                if name not in self.checkNoNameValue:
                    errorFlag = False
                    for error in self.checkErrorValue:
                        if error in name:
                            errorFlag = True
                            break
                    if errorFlag == False:
                        resArray.append(name)
        if resArray:
            return resArray, True
        return resArray, False

    def findByLineBase(self, content: str):
        # email Remove
        # print('findByLineBase !! : ', content)
        content, emailArray = self.__checkEmail(content)
        nameArray = []
        # # #

        # if " 중점을 뒀다”고 했다" in content:
            # print()

        # 실행 순서 바꿈
        if self.backFirst != True:
            for selfP in self.selfPattern:
                nameArray, result = self.__getBylineUsingPattern(content, selfP)
                if result:
                    return nameArray, emailArray

        contents = self.__splitSentence(content)
        self.contents = contents

        if self.FindForceLast == True:

            revese = list(contents)
            revese.reverse()
            for cont in revese:
                if cont == "":
                    continue
                conti = False
                for last in self.LastExcept:
                    if last in cont:
                        conti = True
                        break
                if conti:
                    continue
                for selfP in self.LastForcePattern:
                    nameArray, result = self.__getBylineUsingPattern(cont, selfP)
                    if result:
                        return nameArray, emailArray

        if self.backContent == True:
            contentsLast = contents[-1].replace("email", "")
            checkLogic = False

            if "기자" in contents[-1]:
                # res = self.bylinePreFix.findall(contents[-1])
                # if res:
                #     for data in res:
                #         contentsLast = contentsLast.replace(data,"")
                # else:
                contentsLast = contentsLast.replace("기자", "")
                checkLogic = True

            if checkLogic != True:
                for board in self.boardParsingList:
                    if board in contentsLast:
                        contentsLast = contentsLast.replace(board, "")
                        checkLogic = True
            if checkLogic:
                nameArray, result = self.__getBylineUsingPattern(contentsLast, self.peopleName)
                if result:
                    return nameArray, emailArray

        #       실행 순서 바꿈
        if self.backFirst == True:
            for selfP in self.selfPattern:
                nameArray, result = self.__getBylineUsingPattern(content, selfP)
                if result:
                    return nameArray, emailArray

        if not nameArray:
            for include in self.includeText:
                if include in content:
                    nameArray.append(include)
                    return nameArray, emailArray

        for con in contents:
            for board in self.boardParsingList:
                if board in con:
                    nameArray, result = self.__getBylineUsingPattern(con, self.boardBackCompile[board])
                    if result:
                        return nameArray, emailArray
                    if self.backPatten:
                        nameArray, result = self.__getBylineUsingPattern(con, self.boardFrontCompile[board])
                        if result:
                            return nameArray, emailArray
            if "기자" in con:
                nameArray, result = self.__getBylineUsingPattern(con, self.bylineBaseBack)
                if result:
                    return nameArray, emailArray
                nameArray, result = self.__getBylineUsingPattern(con, self.bylineBaseFront)
                if result:
                    return nameArray, emailArray

        return nameArray, emailArray