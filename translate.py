import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from ttkthemes import ThemedStyle
# python math
# Dictionary mapping language codes to full names
language_names = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "zh": "Chinese",
    "ja": "Japanese",
    "hi": "Hindi",
    "bn": "Bengali",
}
# Creation code
def translate_text():
    text = input_text.get("1.0", "end-1c")
    source_lang = source_language.get()
    target_lang = target_language.get()
    
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    
    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated.text)

app = tk.Tk()
app.title("Language Translator")

# Apply a theme to the application
style = ThemedStyle(app)
style.set_theme("radiance")
# python math
# Input Text
input_label = ttk.Label(app, text="@python.math")
input_label.pack()
input_text = tk.Text(app, height=5, width=40)
input_text.pack()

# Source Language
source_label = ttk.Label(app, text="Source Language:")
source_label.pack()
source_language = ttk.Combobox(app, values=list(language_names.values()))
source_language.set("English")  # Default to English
source_language.pack()

# Target Language
target_label = ttk.Label(app, text="Target Language:")
target_label.pack()
target_language = ttk.Combobox(app, values=list(language_names.values()))
target_language.set("Hindi")  # Default to French
target_language.pack()

# Translate Button
translate_button = ttk.Button(app, text="Translate", command=translate_text)
translate_button.pack()
# Creation code
# Output Text
output_label = ttk.Label(app, text="Translation:")
output_label.pack()
output_text = tk.Text(app, height=5, width=40)
output_text.pack()

app.mainloop()
