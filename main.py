import openai
import base64
import tkinter as tk
from PIL import Image, ImageTk

openai.api_key = "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"

window = tk.Tk()
window.geometry("700x350")
global imagePrint


class Lotfi(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit() or not self.get():
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)


def onClick(numAdults, numKids, budget):
    gpt_prompt = "Suggest a dish for thanksgiving meal along with ingredients which serves the amount of people given " \
                 "in the budget.\n\nInput: Serves: 8-10, Budget: $60\nDish with Ingredients: Turkey: 12-14 pound fresh " \
                 "whole turkey, ½ cup unsalted butter, 1 shallot, 2 tablespoons chopped fresh sage leaves, " \
                 "2 tablespoons fresh thyme leaves, 3 celery ribs, 2 cloves garlic, 3 carrots, 1 sweet onion, " \
                 "½ cup dry white wine\nInput: Adults: " + str(numAdults) + ", Kids: " \
                 + str(numKids) + ", Budget: " + "$" + str(budget) + "\nDish with Ingredients: ";

    entry.set("")
    entry2.set("")
    entry3.set("")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.3,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    line = ""
    for line in response['choices'][0]['text'].split('\n'):
        print(line)
        if line:
            output.config(text=line)
            output.pack()
            break
    dalle_prompt = "image of " + line
    img = openai.Image.create(
        prompt=dalle_prompt,
        n=1,
        size="1024x1024",
        response_format="b64_json"
    )
    image = open("image.png", "wb")
    image.write(base64.b64decode(img['data'][0]['b64_json']))
    image.close()
    imagePrint = ImageTk.PhotoImage(Image.open("image.png").resize((300, 300)))
    canvas.create_image(0, 0, image=imagePrint, anchor="nw")
    canvas.image = imagePrint


configWidget = tk.Frame(window)
configWidget.pack(side="bottom")

entryWidget = tk.Frame(configWidget)
entryWidget.pack(side="left")

adults = tk.Label(entryWidget, text="# of adults")
adults.pack(side="top")

entry = Lotfi(entryWidget, width=30)
entry.pack(side="top")

kids = tk.Label(entryWidget, text="# of kids")
kids.pack(side="top")

entry2 = Lotfi(entryWidget, width=30)
entry2.pack(side="top")

budget = tk.Label(entryWidget, text="budget")
budget.pack(side="top")

entry3 = Lotfi(entryWidget, width=30)
entry3.pack(side="top")

b1 = tk.Button(configWidget, width=90, text="Generate Dish", command=lambda: onClick(entry.get(), entry2.get(), entry3.get()))
b1.pack(side="right")

output = tk.Label(window, width=30, wraplength=150, justify="left")
output.pack(side="left")

canvas = tk.Canvas(window)
canvas.pack(side="right")

window.mainloop()
