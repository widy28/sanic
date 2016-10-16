from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


@app.route("/")
async def test(req, res):
    return json({"test": True})


app.run(host="0.0.0.0", port=8000)