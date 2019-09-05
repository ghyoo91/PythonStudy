import random
import time

class Sticker_quiz:
    level = 0
    dont_know = ""
    def __init__(self):
        with open("py_input.txt", "r") as fp:
            self.dont_know = fp.readline()
        print("--------------------------------------------------------------")
        print(" Welcome : This is the simple test for Sticker's category")
        print("         Notice : All answers are case sensitive")
        print("If you don't know what's the correct answer, plz type "+self.dont_know)
        print("-------------------------Start Now~!--------------------------")
        print("--------------------------------------------------------------")
        print("          Select your appropriate level for the test          ")
        print("  Easy level : Please input 0 // Hard level : Please input 1  ")
        print("--------------------------------------------------------------")
        self.level = input()
        print("--------------------------------------------------------------")

    def quiz(self, field):
        wrong = 0
        while True:
            #wrong == 0 -> Create a New question
            if wrong == 0:
                i = random.randrange(0, len(field))
                if self.level == 0:
                    j = 0
                else:
                    j = random.randrange(0, 2)
            #wrong == 1 -> Show the previous wrong problem
            else:
                pass

            if j == 0:
                print("What is the value of the " + field[i][j] + "?")
            else:
                print("What is the abbr. of the " + field[i][j] + "?")
            temp = input()

            if temp == field[i][1-j]:
                wrong = 0
                print("OOOOOOOOOOOOOOOOO   Correct!! U r genius!!   OOOOOOOOOOOOOOOOO")
            elif temp == '-1':
                break
            elif temp == self.dont_know:
                print("Answer is : " + field[i][1-j])
                time.sleep(3)
                print("\n"*100)
            else:
                wrong = 1
                print("XXXXXX   Your answer isn't correct. Plz try it again.   XXXXXX")
            print("--------------------------------------------------------------")
#classend

a = [['B', '배경'], ['F', '얼굴인식'], ['D', '왜곡'], ['M', '음악'], ['W', '얼굴바꾸기'], ['K', '얼굴스킨'], ['L', '스티커전용필터'], ['E', '카메라이펙트'], ['P', '프레임'], ['R', '화상축소'], ['O', '3D스티커']]

b = [['JSON', 'JavaScript Object Notation'], ['HAR', 'HTTP Archive'], ['AJAX', 'Asynchronous Javascript and XML']]

wego = Sticker_quiz()
wego.quiz(a)
wego.quiz(b)
