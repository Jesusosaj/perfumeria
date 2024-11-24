from flask import Flask, render_template

app = Flask(__name__)

perfumes = [
    {
        "id": 1,
        "nombre": "Parfum Tonford Ombre",
        "descripcion": "Perfume de la gama Tonford con esencias frutales.",
        "info": "El Parfum Tonford Ombre combina la frescura de frutas exóticas con un toque de dulzura suave. Su aroma delicado evoca un jardín en plena primavera, ideal para quienes buscan una fragancia ligera pero duradera. Perfecto para ocasiones diurnas y climas cálidos.",
        "precio": "150$",
        "imagen": "/static/images/perfumes/tonford1.png"
    },
    {
        "id": 2,
        "nombre": "Parfum Tonford Vienessa",
        "descripcion": "Perfume de la gama Tonford con esencias tropicales.",
        "info": "El Parfum Tonford Vienessa ofrece una experiencia aromática única, llena de energía tropical. Notas de mango maduro y piña se mezclan con toques de vainilla, creando una fragancia vibrante y juvenil que destaca por su carácter alegre y exótico.",
        "precio": "100$",
        "imagen": "/static/images/perfumes/tonford2.png"
    },
    {
        "id": 3,
        "nombre": "Parfum Tonford Wave",
        "descripcion": "Perfume de la gama Tonford con esencias maritimas.",
        "info": "Parfum Tonford Wave es una oda al océano. Su mezcla de notas marinas con matices cítricos y amaderados evoca la brisa fresca del mar. Ideal para los amantes de la naturaleza y el verano, es una fragancia refrescante y elegante para el día a día.",
        "precio": "200$",
        "imagen": "/static/images/perfumes/tonford3.png"
    },
    {
        "id": 4,
        "nombre": "Antonio Banderas Lemoon",
        "descripcion": "Perfume de la gama Antonio Banderas con esencias citricas.",
        "info": "Antonio Banderas Lemoon presenta un vibrante bouquet cítrico con notas predominantes de limón y mandarina, complementadas por toques de menta y almizcle. Es una fragancia fresca y chispeante, perfecta para empezar el día con energía y optimismo.",
        "precio": "230$",
        "imagen": "/static/images/perfumes/banderas1.png"
    },
    {
        "id": 5,
        "nombre": "Antonio Banderas SkyGold",
        "descripcion": "Perfume de la gama Antonio Banderas con esencias frutales.",
        "info": "Antonio Banderas SkyGold es una fragancia sofisticada con un corazón frutal dominado por durazno y manzana, equilibrado con un fondo cálido de ámbar y vainilla. Ideal para ocasiones especiales, combina elegancia y modernidad.",
        "precio": "160$",
        "imagen": "/static/images/perfumes/banderas2.png"
    },
    {
        "id": 6,
        "nombre": "Antonio Banderas Essentials",
        "descripcion": "Perfume de la gama Antonio Banderas con esencias cálidas.",
        "info": "Antonio Banderas Essentials es una fragancia cálida y envolvente, con notas especiadas y un toque de madera de sándalo. Perfecta para las noches frías, transmite confianza y sofisticación con cada aplicación.",
        "precio": "120$",
        "imagen": "/static/images/perfumes/banderas3.png"
    }
]

@app.route("/")
def dashboard():
    return render_template("dashboard.html", perfumes=perfumes)


@app.route("/Login")
def login():
    return render_template("login.html")

@app.route("/Register")
def register():
    return render_template("register.html")

@app.route("/perfume/<int:perfume_id>")
def perfume_detail(perfume_id):
    perfume = next((p for p in perfumes if p["id"] == perfume_id), None)
    if perfume is None:
        return "Perfume no encontrado", 404
    return render_template("detalle.html", perfume=perfume)

if __name__ == "__main__":
    app.run(debug=True)
