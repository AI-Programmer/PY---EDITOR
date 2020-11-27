#---------------------------------------------------#
#-------------------- PY - EDITOR ------------------#
#---------------------(R.LOKESH)--------------------#
#---------------------------------------------------#

import kivy
from kivy.uix.codeinput import CodeInput
from pygments.lexers import CythonLexer
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.modules import keybinding
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from tkinter import Tk
from tkinter import filedialog
import subprocess
import os
import sys


global f
f = None
kv = '''
ScreenManager:
    Screen1:

<Screen1>:
    name : 'main'
    code : code
    BoxLayout:
        orientation : 'vertical'
        ActionBar:
            pos_hint: {'top':1}
            ActionView:
                use_separator: True
                ActionPrevious:
                    title: 'PY - EDITOR'
                    with_previous: False
                ActionGroup:
                    text: 'File' 
                    mode: 'spinner'
                    ActionButton:
                        text: 'Save'
                        on_press:
                            root.save()
                    ActionButton:
                        text: 'Save As'
                        on_press:
                            root.saveas()
                
                ActionButton:
                    text: 'Open'
                    on_press:
                        root.open()
                ActionButton:
                    text: 'Close'
                    on_press:
                        root.close()
                       
        CodeInput:
            id : code


'''


class Screen1(Screen):
    code = ObjectProperty(None)

    def close(self):
        sys.exit()

    def open(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename()
        with open(filename, "r") as input_file:
            text = input_file.read()
            self.code.text = str(text)

    def save(self):
        file_save = f
        code_save_write = self.code.text
        try:
            with open(file_save, 'w') as write_file:
                text = write_file.write(code_save_write)
                print(text)
        except Exception:
            pass

    def saveas(self):
        global f
        code_save = self.code.text
        Tk().withdraw()
        f = filedialog.asksaveasfilename(filetypes=(('Python File', '*.py'),))
        python_file = open(f, 'w')
        python_file.write(code_save)
        python_file.close()


s = ScreenManager()
s.add_widget(Screen1(name='main'))


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    MyApp().run()
