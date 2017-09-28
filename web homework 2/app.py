from flask import Flask, render_templat
import mlab.py
from mongoengine import Document, Stringfield
mlab.connect()
class GirlType(Documment):
    name = Stringfield
    image = Stringfield
    description = Stringfield
    girl_type = GirlType(name="Gái tiểu thư"
                         , image="https://via.placeholder.com/400x200",
                         description="Tính gọn gàng sạch sẽ, thường giỏi nghệ thuật, thích đến nơi sang trọng")
    girl_type.save()
#1.Connect to mlab
#2.Add some data

app = Flask(__name__)
app.config("Debug") = True

gt = [
{
"name": "Gái tiểu thư",
"image": "https://via.placeholder.com/400x200",
"description": "Tính gọn gàng sạch sẽ, thường giỏi nghệ thuật, thích đến nơi sang trọng"
},
{"name": "Gái tiểu thư",
"image": "https://via.placeholder.com/400x200",
"description": "Tính bình dân, trẻ như học sinh, già như công sở, hay xuất hiện ở L'éspace, viện Goethe"
},
{"name": "Gái hư",
"image": "https://via.placeholder.com/400x200",
"description": "Chỉ cần nhìn là biết"
},

]


@app.route('/')
def index():
    return render_template("index html", girl_types=gt)


@app.route("/about")
def about():
    return render_template('about.html')
    app.run()
