from hanspell import spell_checker

def SpellCheck(content):
    # print(content)
    # print(len(content))
    content = content[:480]
    try:
        result = spell_checker.check(content)
        # print(result.as_dict())
    except:
        print('Error')
        return 0
    return result.as_dict()['errors']

# SpellCheck("안녕하세요.")