import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.input_text = TextInput(multiline=False)
        layout.add_widget(self.input_text)

        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        calculate_button = Button(text="Calculate")
        calculate_button.bind(on_press=self.calculate)
        layout.add_widget(calculate_button)

        return layout

    def process_sequence(self, sequence_text):
        try:
            # Extract numbers, removing spaces and converting to integers
            sequence = [int(x) for x in sequence_text.split() if x.isdigit()]
            return sequence
        except ValueError:
            return None  # Indicate invalid input

    def calculate(self, instance):
        sequence = self.process_sequence(self.input_text.text)
        if sequence is None:
            self.result_label.text = "Invalid input"
            return

        # Now the sequence is guaranteed to be a list of integers
        a1, a2, a3 = sequence[:3]  # Assuming the sequence has at least 3 elements

        # Perform calculations
        x1 = a1 + a3
        x2 = a2 * 2

        # Check and display result
        if x1 == x2:
            d = a2 - a1
            self.result_label.text = f"tn = {a1} + (n-1) * {d}"
        else:
            self.result_label.text = "Your sequence does not count"

if __name__ == '__main__':
    MyKivyApp().run()