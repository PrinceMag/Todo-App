from kivy.config import Config
Config.set('graphics','resizable',True)
from app import MainApp
from kivy.garden.iconfonts import register
from os.path import dirname,join

if __name__ == '__main__':
    register('MatIcons',join(dirname(__file__),'app/assets/fonts/Material-Design-Iconic-Font.ttf'),join(dirname(__file__),'app/assets/fonts/zmd.fontd'))
    register('MatIcons',join(dirname(__file__),'app/assets/fonts/fontawesome.ttf'),join(dirname(__file__),'app/assets/fonts/fontawesome.fontd'))
    MainApp().run() 