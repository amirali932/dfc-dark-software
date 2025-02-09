from kivy.app import App
from kivy.uix.actionbar import window_icon
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
import webbrowser

Window.icon = "dfc.png"
class DarkSoftwareApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title Label
        title = Label(text='Welcome to Dark Software', font_size='24sp', color=(1, 0, 0, 1), bold=True)
        layout.add_widget(title)

        # Description Label
        desc = Label(text='Your ultimate tool for system management. Download the latest version below:',
                     font_size='16sp', color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(desc)

        # Download Button
        download_button = Button(text='Download Dark Software', background_color=(1, 0, 0, 1), size_hint=(None, None),
                                 size=(250, 50))
        download_button.bind(on_press=lambda x: webbrowser.open(
            'https://drive.google.com/file/d/1qvk6a1DJhryevDD3dw2wGO5cXWdtpNJf/view?usp=drive_link'))
        layout.add_widget(download_button)

        # About Section
        about_title = Label(text='About Dark Software', font_size='20sp', color=(1, 0, 0, 1), bold=True)
        layout.add_widget(about_title)

        about_text = Label(
            text='Dark Software is an advanced tool designed to make system management easy and efficient.',
            font_size='16sp', color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(about_text)

        # Features
        features_title = Label(text='Features:', font_size='18sp', color=(1, 0, 0, 1), bold=True)
        layout.add_widget(features_title)

        features_list = Label(
            text='- Powerful system optimization tools\n- Easy-to-use interface\n- Customizable settings\n- Regular updates',
            font_size='16sp', color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(features_list)

        # Contact Section
        contact_title = Label(text='Contact Us', font_size='18sp', color=(1, 0, 0, 1), bold=True)
        layout.add_widget(contact_title)

        contact_info = Label(text='Email: dujin7@gmail.com\nWhatsApp: +93791838411\nCompany: Dark Force',
                             font_size='16sp', color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(contact_info)

        return layout


if __name__ == '__main__':
    DarkSoftwareApp().run()
