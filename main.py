from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ListProperty,NumericProperty
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
import requests
import random
import time
Window.size=(300,500)
url='http://7d75-35-197-54-65.ngrok.io/Heart_disease'
["Age","Sex","MaxHR","ChestPainType","ST_Slope","Cholesterol"]
class circularBAR(MDAnchorLayout):
    bar_color=ListProperty([100/255,0,100/255])
    bar_width=NumericProperty(5)
    bar_value=NumericProperty(10)
    def __init__(self,**kwargs):
        super(circularBAR,self).__init__(**kwargs)
        Clock.schedule_interval(self.checkheart,1)
    def checkheart(self,*args):
        number=random.randint(70,120)
        self.bar_value=number



class MainAPP(MDApp):
    dialog=None
    def build(self):
        self.theme_cls.material_style='M3'
        self.theme_cls.theme_style='Light'
        self.screen=MDScreenManager()
        screen=Screen()
        self.widget=Builder.load_file('main.kv')
        #marker.add_widget(MDIconButton())
        screen.add_widget(self.widget)
        self.screen.add_widget(screen)
        return self.screen
    def send_values(self,age,sex,Cholestrol,slope,Chest_pain,bar_value):
        values=dict()
        values['Age']=int(age)
        values['Sex']=sex
        values['ChestPainType']=Chest_pain
        values["MaxHR"]=bar_value
        values["ST_Slope"]=slope
        values['Cholestrol']=int(Cholestrol)
        payload=requests.post(url,json=values)
        time.sleep(3)
        respond=payload.json()
        text='Healthy:'+str(round(respond['healthy'],2))+" "+"Diseased:"+str(round(respond['Diseased'],2))
        self.widget.ids.pred.text=text
    
MainAPP().run()