from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Window(QWidget):
  
    def __init__(self): # Для консольного приложения
        super().__init__()
  
        
        self.setWindowTitle("Python ") # настройка заголовка    
        self.setGeometry(100, 100, 360, 350)    # настройка геометрии    
        self.UiComponents()    # вызов метода     
        self.show() # отображение всех виджетов
  
       
    def UiComponents(self): # метод для виджетов (для кнопок и экрана)
  
        
        self.label = QLabel(self)     # создание метки (экрана)
        self.label.setGeometry(5, 5, 350, 70)    # настройка геометрии для метки
        self.label.setWordWrap(True)    # создание многострочной метки     
        self.label.setStyleSheet("QLabel"    # установка таблицы стилей для метки
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight) # настройка выравнивания по метке
        self.label.setFont(QFont('Arial', 15)) # шрифта

        push1 = QPushButton("1", self) # создание кнопки 1
        push1.setGeometry(5, 150, 80, 40) # геометрия кнопки
     
#дальше абсолютно так же создаюстся кнопки  2 3 4 5 6 7 8 9 0 = + - / *
        push2 = QPushButton("2", self)
        push2.setGeometry(95, 150, 80, 40)
         
        push3 = QPushButton("3", self)
        push3.setGeometry(185, 150, 80, 40)
        
        push4 = QPushButton("4", self)
        push4.setGeometry(5, 200, 80, 40)
         
        push5 = QPushButton("5", self)
        push5.setGeometry(95, 200, 80, 40)
         
        push6 = QPushButton("5", self)
        push6.setGeometry(185, 200, 80, 40)
        
        push7 = QPushButton("7", self)
        push7.setGeometry(5, 250, 80, 40)

        push8 = QPushButton("8", self)
        push8.setGeometry(95, 250, 80, 40)
        
        push9 = QPushButton("9", self)
        push9.setGeometry(185, 250, 80, 40)
  
        push0 = QPushButton("0", self)
        push0.setGeometry(5, 300, 80, 40)
  
        push_equal = QPushButton("=", self) 
        push_equal.setGeometry(275, 300, 80, 40)
  
        c_effect = QGraphicsColorizeEffect() # adding equal кнопка цветовой эффект
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)
  
        push_plus = QPushButton("+", self)
        push_plus.setGeometry(275, 250, 80, 40)

        push_minus = QPushButton("-", self)
        push_minus.setGeometry(275, 200, 80, 40)
  
        push_mul = QPushButton("*", self)
        push_mul.setGeometry(275, 150, 80, 40)

        push_div = QPushButton("/", self)
        push_div.setGeometry(185, 300, 80, 40)
  
        push_point = QPushButton(".", self)
        push_point.setGeometry(95, 300, 80, 40)
  
        push_clear = QPushButton("Clear", self) # создание кнопки Очистить
        push_clear.setGeometry(5, 100, 200, 40)
  
        push_del = QPushButton("Del", self)   