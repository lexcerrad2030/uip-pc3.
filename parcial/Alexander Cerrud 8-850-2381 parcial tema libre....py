from kivi.app  import App

from kivy.uix.scatter import scatter
from kivy.uix.label import label
from kivy.uix.floatlayout import FloatLayout
class primerApp(App):
        def build(self):
                f = FloatLayout()
                s =  scatter()
                l = label(text="mi primer intento!",
                          font_size=150)

                f.add_widget(s)
                s.add_widget(l)
                return f

if __name__=="__main__"
primerApp().run()