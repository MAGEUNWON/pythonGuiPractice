from tkinter import *
basic_data_dict = {
  "title_name" : "HTML maker",
  "window_width" : 300,
  "window_height" : 300,
  "resizable_x" : True,
  "resizable_y" : True,
}

class Resizable:
    def __init__(self, width, height):
        self.width = width,
        self.height = height,
    @property
    def size(self):
        set_tuple = self.width + self.height
        return set_tuple

# ?Resizable class 만들어보기 
# *사이즈는 어디에나 사용할 수 있을 것 같아 클래스로 만듬
# *getter의 형태가 자바스크립트 클래스와 다름
# **@데코레이터(c++) 라는 문법으로 getter를 사용할 수 있는 것이 특징
# **get 키워드를 사용한ㄴ 자바스크립트 getter

test = Resizable(100, 200)
print(test.size)
print(type(test.size[0]))
print(type(str(test.size[1])))

window = Tk()

window.title(basic_data_dict["title_name"])

# geometry_value = str(basic_data_dict["window_width"]) + "x" +str(basic_data_dict["window_height"])

geometry_value = Resizable(basic_data_dict["window_width"], basic_data_dict["window_height"]).size
# ?geometry_value변수: 위에서 선언한 클래스를 할당하면서 필요한 값을 가져오기 위해 getter인 size를 불러옴
# *값을 불러오다보니 자바스크립트는 타입을 지정할 수 있었는데 파이썬에서는 무조건 튜플로 처리되는 것을 확인
# *코드양으로 보았을 땐 더 길어졌지만, 사이즈를 사용하는 일이 많아지면 편해질 듯



# window.title("HTML maker")

window.geometry(str(geometry_value[0]) + "x" + str(geometry_value[1]))
window.resizable(basic_data_dict["resizable_x"], basic_data_dict["resizable_y"])

def html_maker():
    temp_string = '''
    <html>
      <head></head>
      <body></body>
    </html>
    '''
    button["text"] = temp_string
# *title, geometry, resizable 이 세가지는 항상 써야함
# 함수로 처리하면 편함

button = Button(window, text = "HTML 찍어내기!", width=20, height=5, command=html_maker)
# ?Button() 첫글자가 대문자인 것으로 보아 class문법으로 제작된 것을 유추할 수 있음.
# *의도 : 버튼을 누르면 원하는 문자열이 나타날 것
# pseudo : 최종적으로 html 파일이 생성되서 지정될 것

# label = Label(window, text="이게 뭐지?")

# label.pack(side="bottom")

# pack(side="bottom")하면 글씨가 아래로 위치

# pack() 은 <HTML>의 display:block 비슷한 역할을 하는 속성

# print(window)
# # *불러온 라이브러리에 무슨 함수와 값들이 있는지 확인 하려고 디버거를 사용함. 
# # *무엇인지 한눈에 안보이는 것 90프로
# # *class variables 항목을 조회해보니 얼추 기능을 유추할 수 있는 것들을 확인 할 수 있음

# # *HTML처럼 기본 형태는 무엇인지 검색함

button.pack()

window.mainloop()

