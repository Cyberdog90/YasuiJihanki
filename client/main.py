import PySimpleGUI as gui
import json
import requests


def main():
    gui.theme("Python")
    window = gui.Window(title="最安値", layout=layout(), size=(800, 600), element_justification="C")
    while True:
        event, value = window.read()
        if event == "searchButton":
            window["table"].update(values=get_category(value["category"]))
            window["resultText"].update(visible=True)
            window["table"].update(visible=True)
        if event is None:
            break
    window.close()


def get_category(category):
    dic = json.loads(requests.get(f"http://192.168.98.240:8888/?category={category}").text)
    items = []
    for key, values in dic["drinks"].items():
        for place, price in values.items():
            items.append([key, place, f"{price}円"])
    return items


def layout():
    category = json.loads(requests.get("http://192.168.98.240:8888/?category=what").text)
    return [
        [gui.Combo(category["category"], default_value=category["category"][0], size=(20, 1), key="category")],
        [gui.Button(button_text="検索", key="searchButton")],
        [gui.Text(text="検索結果", key="resultText", visible=False)],
        [gui.Table(values=[], headings=["商品名", "場所", "値段"], col_widths=[20, 20, 10], auto_size_columns=False,
                   size=(1, 30), key="table", visible=False)]
    ]


if __name__ == '__main__':
    main()
