from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField

class TodoCard(FakeRectangularElevationBehavior,MDFloatLayout):
    title = StringProperty()
    description = StringProperty()

class Add_TodoCard(FakeRectangularElevationBehavior,MDFloatLayout):
    pass


class Content(BoxLayout):
    pass


class MainWindow(MDBoxLayout):
    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release= self.closeDialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.grabText
                    ),
                ],
            )
        self.dialog.open()
        
    def grabText(self, inst):
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)
        self.dialog.dismiss()

    def closeDialog(self, inst):
        self.dialog.dismiss()