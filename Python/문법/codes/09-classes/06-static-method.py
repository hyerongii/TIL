class StringUtils:
    
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)

# 인스턴스가 사용가능함 but 사용하지 말기
# instance1 = StringUtils()
# print(instance1.reverse_string(text))

