from flask import Flask, request
from drink import Drink
import json

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

drink = Drink()


@app.route('/', methods=["GET"])
def get_drinks():
    category = request.args.get("category")
    if category in drink.category.keys():
        return drink.get_category(category)
    elif category == "what":
        return json.dumps({"category": [key for key in drink.category.keys()]}, ensure_ascii=False)
    else:
        return json.dumps({"nods": 0, "drinks": {}}, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
