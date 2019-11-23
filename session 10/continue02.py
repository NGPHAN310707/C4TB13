Dictionary = {
    "homework" : "bài tập vè nhà",
    "goodbye" : "tạm biệt",
    "red" : "màu đỏ",
    'champion' : 'nhà vô địch'
}
while True:
    s = input('what are you up to?    ')
    if s  in Dictionary:
        print(s,'meaning',Dictionary[s])
    else:
        print(s ,'cannot found')
