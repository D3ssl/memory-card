from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QPushButton, QGroupBox
from random import shuffle
from random import randint
# создать класс Question
class Question():
    def __init__(self, quest,a_r,w1,w2,w3):
        self.quest = quest
        self.a_r = a_r
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3


#создай приложение для запоминания информации
app = QApplication([])
main_win = QWidget()

# создать виджеты
main_win.resize(400,200)
main_win.setWindowTitle('Memory Card')
answer = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')
main_win.cur_quest = -1
#создать группу и лэйауты


RBG = QGroupBox('Варианты ответов')
rbt_1 = QRadioButton('Энцы')
rbt_2 = QRadioButton('Смурфы')
rbt_3 = QRadioButton('Чулымцы')
rbt_4 = QRadioButton('Алеуты')

layout_quest = QVBoxLayout()
layout_quest2 = QVBoxLayout()
layout_quest.addWidget(rbt_1)
layout_quest.addWidget(rbt_2)
layout_quest2.addWidget(rbt_3)
layout_quest2.addWidget(rbt_4)
layout_quest3 = QHBoxLayout()
layout_quest3.addLayout(layout_quest)
layout_quest3.addLayout(layout_quest2)

RBG.setLayout(layout_quest3)


l1 = QHBoxLayout()
l1.addWidget(question, alignment = Qt.AlignCenter)
l2 = QHBoxLayout()
l2.addWidget(RBG, alignment = Qt.AlignCenter)
l3 = QHBoxLayout()
l3.addWidget(answer, alignment = Qt.AlignCenter)
v_main = QVBoxLayout()
v_main.addLayout(l1)
v_main.addLayout(l2)
v_main.addLayout(l3)
#скрыть варианты ответов

#создать виджет-результат
ansRBG = QGroupBox('Результат теста')
a = QLabel('Правильно/Неправильно')
a1 = QLabel(' ')

v1 = QVBoxLayout()
v1.addWidget(a, alignment = Qt.AlignLeft)
v1.addWidget(a1, alignment = Qt.AlignCenter)
ansRBG.setLayout(v1)


l2.addWidget(ansRBG)
ansRBG.hide()

#Написать функции
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbt_1)
RadioGroup.addButton(rbt_2)
RadioGroup.addButton(rbt_3)
RadioGroup.addButton(rbt_4)

def show_result():
    RBG.hide()
    ansRBG.show()
    answer.setText('Следующий вопрос')

    

def show_question():
    ansRBG.hide()
    RBG.show()
    answer.setText('Ответить')
    
    RadioGroup.setExclusive(False)
    rbt_1.setChecked(False)
    rbt_2.setChecked(False)
    rbt_3.setChecked(False)
    rbt_4.setChecked(False)
    RadioGroup.setExclusive(True)
'''def start_test():
    if answer.text() == 'Ответить':
        show_result()
    else:
        show_question()'''
    
answers = [rbt_1, rbt_2, rbt_3, rbt_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.a_r)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    question.setText(q.quest)
    a1.setText(q.a_r)
    show_question()

def show_correct(res):
    a.setText(res)
    show_result()

main_win.total = 0
main_win.score = 0


def check_answer():  
      
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')
    result = main_win.score/main_win.total * 100
    print('Рейтинг:',int(result), '%')
    print('Статистика\n-Всего вопросов:', main_win.total,'\n-Правильных ответов:', main_win.score)
questions_list = list()

q1 = Question('Выбери перевод слова "переменная"','variable', 'changeable', 'fickle', 'volatile')
q2 = Question('Формула площади параллелограмма', 's = a*h', 's = a*h/2', 's = a+h/2', 's = a*h*2')
q3 = Question('Как зовут создателя Теслы', 'Мартин Эберхард', 'Илон Маск', 'Чарльз Терон', 'Марк Тарпенинг')
q4 = Question('Какова градусная мера окружности', '360', '120', '720','180')
q5 = Question('Что такое "H2O"','Вода', 'Бромоводород', 'Азот','Золото')
q6 = Question('Государственный язык в Бразилии', 'Португальский', 'Английский', 'Бразильский', 'Итальянский')
q7 = Question('Годы правления Александра I','1801-1825','1830-1865','1780-1830','1800-1810')
q8 = Question('Выбери перевод слова "superstition"','Предрассудок','Супер сила','Мощь','захватывающий')
q9 = Question('Что делают в точке пересечения диагонали в параллелограмме','Делятся','Ничего','Создают угол в 60','Не делятся')
q10 = Question('Закон всемирного тяготения','F = Gm1m2/r^2','F = m1m2/2','F = Gm2m1/r','F = Gr^2/m1m2')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)



def next_question():
    main_win.total += 1

    cur_question = randint(0, len(questions_list) - 1)
    # main_win.cur_quest += 1
    # if main_win.cur_quest >= len(questions_list):
    #     main_win.cur_quest = 0
    q = questions_list[cur_question]
    ask(q)
  
next_question()
def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()




answer.clicked.connect(click_ok)






#отображение окна приложения 
main_win.setLayout(v_main)
main_win.show()
app.exec_()


