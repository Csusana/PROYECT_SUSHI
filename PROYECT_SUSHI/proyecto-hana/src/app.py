# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect, flash
import os

from flask_mail import Mail, Message


app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "../static"),
)


def cocina_lista():
    return {
        1: {
            "nombre": "Wok Pasta Thai Langostinos.",
            "precio": 26660,
            "descripcion": "Con vegetales, hongos y spaghettis, con salsa thai a base de maní, con langostinos.",
            "foto": url_for("static", filename="/images/wok-pasta-langostinos.jpg"),
            "numero": 1,
        },
        2: {
            "nombre": "Wok Pasta Thai Pollo.",
            "precio": 17220,
            "descripcion": "Con vegetales, hongos y spaghetis, con salsa thai a base de maní, con pollo.",
            "foto": url_for("static", filename="/images/wok-pasta-pollo.jpg"),
            "numero": 2,
        },
        3: {
            "nombre": "Wok de Mero y Camarones.",
            "precio": 26220,
            "descripcion": "Con vegetales, salsa de ostras, leche y crema, acompañado de arroz blanco.",
            "foto": url_for("static", filename="/images/wok-mero-camarones.jpg"),
            "numero": 3,
        },
        4: {
            "nombre": "Wok de Vegetales y Arroz Mixto.",
            "precio": 18600,
            "descripcion": "Con salsa de ostras y soja, con lomo y pollo.",
            "foto": url_for("static", filename="/images/wok-vegetales-arroz.jpg"),
            "numero": 4,
        },
    }


def lanzamientos_lista():
    return {
        1: {
            "nombre": "Combinado Niguiri Fusion 6p",
            "precio": 11970,
            "descripcion": "(6 piezas) Crispy White Niguiri, Niguiri de Salmón, Niguiri Anticuchero, Fuego Thai, Niguiri Palta Thai, Niguiri de Langostino Fuego Thai",
            "foto": url_for("static", filename="/images/niguiri-6.jpg"),
            "numero": 5,
        },
        2: {
            "nombre": "Combinado Niguiri Selecto 8p",
            "precio": 55200,
            "descripcion": "(8 piezas): Crispy White Niguiri, Niguiri de Salmón, Niguiri Anticuchero, Fuego Thai, Niguiri Palta Thai, Niguiri de Langostino Fuego Thai, Niguiri de Pulpo, Niguiri de Salmón Ahumado",
            "foto": url_for("static", filename="/images/niguiri-8.jpg"),
            "numero": 6,
        },
        3: {
            "nombre": "Temaki de Langostino",
            "precio": 8680,
            "descripcion": "Langostinos en tempura, palta y queso crema con salsa de maracuyá.",
            "foto": url_for("static", filename="/images/temaki-langostino.jpg"),
            "numero": 7,
        },
        4: {
            "nombre": "Temaki de Salmon",
            "precio": 8680,
            "descripcion": "Salmón, palta y queso crema.",
            "foto": url_for("static", filename="/images/temaki-salmon.jpg"),
            "numero": 8,
        },
    }


def combinados_lista():
    return {
        1: {
            "nombre": "Combinado BIO-Veggie 15 piezas",
            "precio": 21280,
            "descripcion": "crispy green, fresh fusion, camembert, niguiri palta thai, sweet treee. Ingredientes: tomates secos en conserva, espinaca, panko, queso camembert, guacamole, zanahoria, criolla de rocoto, palta, crocante de batata, verdeo, palta, queso crema, maíz cancha frito. salsas agripicante, apio, mango, tailandesa a base de pasta de maní y mango.",
            "foto": url_for("static", filename="/images/combinado-veggie-15.png"),
            "numero": 9,
        },
        2: {
            "nombre": "Combinado Blue Sea 15 piezas",
            "precio": 31640,
            "descripcion": "buenos aires, celerity, feel, soul, niguiri fuego thai. incluye salsa buenos aires (creación sushiclub). Ingredientes: salmón, langostinos, palta, queso crema, guacamole, criolla de rocoto, mayonesa de apio, verdeo, tamago, palmito, almendras caramelizadas y sal marina. salsas de sésamo, tailandesa a base de pasta de maní y agripicante. ",
            "foto": url_for("static", filename="/images/combinado-blue-sea-15.jpg"),
            "numero": 10,
        },
        3: {
            "nombre": "Combinado Roll&Roll 15 piezas",
            "precio": 31640,
            "descripcion": "placer real, soul, feel, geishas de salmón, futurama, sweet, spf. Ingredientes: palta, palmito, queso crema, tamago, salmón, salsa de maracuyá, crocante de batata, almendras caramelizadas, verdeo, sésamo, langostinos rebozados, panko, langostino tempura. salsas de mango y miel & mostaza.",
            "foto": url_for("static", filename="/images/combinado-rollroll-15.jpg"),
            "numero": 11,
        },
        4: {
            "nombre": "Combinado Superstar 15 piezas",
            "precio": 28700,
            "descripcion": "spf, placer real, buenos aires, niguiri palta thai, fresh fusion. Ingredientes: salmón, palta, sésamo, palmito, queso crema, tamago, crocantes de batata, langostinos, verdeo, sal marina, queso camembert, guacamole, zanahoria, criolla de rocoto. salsas de sésamo, maracuyá, tailandesa a base de pasta de maní, agripicante, apio",
            "foto": url_for("static", filename="/images/combinado-superstar-15.jpg"),
            "numero": 12,
        },
        5: {
            "nombre": "Combinado SushiClub 15 piezas",
            "precio": 31640,
            "descripcion": "buenos aires, placer real, feel, honey, philadelphia, sashimi de salmón y niguiri de salmón.  incluye salsa buenos aires (creación sushiclub). Ingredientes: salmón, langostinos, palta, queso crema, palmito, tamago, crocante de batata, verdeo, salmón cocido saborizado con reducción de miel & jengibre y sésamo. salsas de sésamo y maracuyá.",
            "foto": url_for("static", filename="/images/combinado-sushiclub-15.png"),
            "numero": 13,
        },
        6: {
            "nombre": "Combinado BIO-Veggie 30 piezas",
            "precio": 41720,
            "descripcion": "crispy green, fresh fusion, camembert, niguiri palta thai, sweet treee. Ingredientes: tomates secos en conserva, espinaca, panko, queso camembert, guacamole, zanahoria, criolla de rocoto, palta, crocante de batata, verdeo, palta, queso crema, maíz cancha frito. salsas agripicante, apio, mango, tailandesa a base de pasta de maní y mango.",
            "foto": url_for("static", filename="/images/combinado-veggie-30.png"),
            "numero": 14,
        },
        7: {
            "nombre": "Combinado Blue Sea 30 piezas",
            "precio": 61740,
            "descripcion": "buenos aires, celerity, feel, soul, niguiri fuego thai. incluye salsa buenos aires (creación sushiclub). Ingredientes: salmón, langostinos, palta, queso crema, guacamole, criolla de rocoto, mayonesa de apio, verdeo, tamago, palmito, almendras caramelizadas y sal marina. salsas de sésamo, tailandesa a base de pasta de maní y agripicante. ",
            "foto": url_for("static", filename="/images/combinado-bluesea-30.jpg"),
            "numero": 15,
        },
        8: {
            "nombre": "Combinado Roll&Roll 30 piezas",
            "precio": 61740,
            "descripcion": "placer real, soul, feel, geishas de salmón, futurama, sweet, spf. Ingredientes: palta, palmito, queso crema, tamago, salmón, salsa de maracuyá, crocante de batata, almendras caramelizadas, verdeo, sésamo, langostinos rebozados, panko, langostino tempura. salsas de mango y miel & mostaza.",
            "foto": url_for("static", filename="/images/combinado-rollroll-30.jpg"),
            "numero": 16,
        },
        9: {
            "nombre": "Combinado Superstar 30 piezas",
            "precio": 56280,
            "descripcion": "spf, placer real, buenos aires, niguiri palta thai, fresh fusion. Ingredientes: salmón, palta, sésamo, palmito, queso crema, tamago, crocantes de batata, langostinos, verdeo, sal marina, queso camembert, guacamole, zanahoria, criolla de rocoto. salsas de sésamo, maracuyá, tailandesa a base de pasta de maní, agripicante, apio",
            "foto": url_for("static", filename="/images/combinado-superstar-30.jpg"),
            "numero": 17,
        },
        10: {
            "nombre": "Combinado SushiClub 30 piezas",
            "precio": 61740,
            "descripcion": "buenos aires, placer real, feel, honey, philadelphia, sashimi de salmón y niguiri de salmón.  incluye salsa buenos aires (creación sushiclub). Ingredientes: salmón, langostinos, palta, queso crema, palmito, tamago, crocante de batata, verdeo, salmón cocido saborizado con reducción de miel & jengibre y sésamo. salsas de sésamo y maracuyá.",
            "foto": url_for("static", filename="/images/combinado-sushiclub-30.jpg"),
            "numero": 18,
        },
    }


def menu_infantil_lista():
    return {
        1: {
            "nombre": "Arrollados Primavera J&M.",
            "precio": 11270,
            "descripcion": "Jamón y muzarella envuelto masa crocante, acompañado de salsa agridulce.",
            "foto": url_for("static", filename="/images/arrollado-primavera.jpg"),
            "numero": 19,
        },
        2: {
            "nombre": "Chick & Chips.",
            "precio": 11270,
            "descripcion": "Croquetas de pollo y queso cheddar, acompañado de papas smile.",
            "foto": url_for("static", filename="/images/chick-chips.jpg"),
            "numero": 20,
        },
        3: {
            "nombre": "Peke de Lomo.",
            "precio": 11270,
            "descripcion": "A base de lomo y arroz.",
            "foto": url_for("static", filename="/images/peke-lomo.jpg"),
            "numero": 21,
        },
        4: {
            "nombre": "Peke de Pollo.",
            "precio": 11270,
            "descripcion": "A base de pollo y arroz.",
            "foto": url_for("static", filename="/images/peke-pollo.jpg"),
            "numero": 22,
        },
    }


def bebidas_lista():
    return {
        1: {
            "nombre": "Agua Smartwater",
            "precio": 3360,
            "descripcion": "Con o sin gas",
            "foto": url_for("static", filename="/images/agua.jpg"),
            "numero": 23,
        },
        2: {
            "nombre": "Aquarius Manzana",
            "precio": 3780,
            "descripcion": "-",
            "foto": url_for("static", filename="/images/manzana.jpg"),
            "numero": 24,
        },
        3: {
            "nombre": "Aquarius Naranja",
            "precio": 3780,
            "descripcion": "-",
            "foto": url_for("static", filename="/images/naranja.jpg"),
            "numero": 25,
        },
        4: {
            "nombre": "Aquarius Pera",
            "precio": 3780,
            "descripcion": "-",
            "foto": url_for("static", filename="/images/pera.jpg"),
            "numero": 26,
        },
        5: {
            "nombre": "Aquarius Pomelo",
            "precio": 3780,
            "descripcion": "-",
            "foto": url_for("static", filename="/images/pomelo.jpg"),
            "numero": 27,
        },
        6: {
            "nombre": "Coca-Cola 500 ml.",
            "precio": 3780,
            "descripcion": "-",
            "foto": url_for("static", filename="/images/coca.jpg"),
            "numero": 28,
        },
        7: {
            "nombre": "Cerveza Corona",
            "precio": 6720,
            "descripcion": "Por falta de stock de porrón podrías recibir una lata del mismo producto.",
            "foto": url_for("static", filename="/images/corona.jpg"),
            "numero": 29,
        },
        8: {
            "nombre": "Patagonia 24.7 IPA Lata 410cc",
            "precio": 5970,
            "descripcion": "-",
            "foto": url_for("static", filename="/images/patagonia.jpg"),
            "numero": 30,
        },
        9: {
            "nombre": "Stella Artois",
            "precio": 4760,
            "descripcion": "Por falta de stock de porrón podrías recibir una lata del mismo producto.",
            "foto": url_for("static", filename="/images/stella.jpg"),
            "numero": 31,
        },
        10: {
            "nombre": "Stella Artois sin alcohol",
            "precio": 3500,
            "descripcion": "Por falta de stock de porrón podrías recibir una lata del mismo producto.",
            "foto": url_for("static", filename="/images/stella-no-alcohol.jpg"),
            "numero": 32,
        },
    }


def postres_lista():
    return {
        1: {
            "nombre": "Cheesecake.",
            "precio": 10080,
            "descripcion": "Sobre masa crocante con confitura de frutos rojos",
            "foto": url_for("static", filename="/images/cheescake.jpg"),
            "numero": 33,
        },
        2: {
            "nombre": "Lujuria de Chocolate.",
            "precio": 10710,
            "descripcion": "Mousse de chocolate, crema chantilly, laminas de frutilla, en salón con tuil de almendras.",
            "foto": url_for("static", filename="/images/lujuria-chocolate.jpg"),
            "numero": 34,
        },
        3: {
            "nombre": "Pasión de Chocolate.",
            "precio": 14000,
            "descripcion": "Volcán de chocolate con corazón de maracuyá, en salón con helado de mascarpone y frutos rojos.",
            "foto": url_for("static", filename="/images/volcan.jpg"),
            "numero": 35,
        },
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        menu1=lanzamientos_lista()[2],
        menu2=cocina_lista()[1],
        menu3=combinados_lista()[3],
        menu4=combinados_lista()[4],
        menu5=menu_infantil_lista()[2],
        menu6=postres_lista()[3],
    )


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/shop")
def shop():
    return render_template(
        "shop.html",
        lanzamientos=lanzamientos_lista(),
        combinados=combinados_lista(),
        menu_infantil=menu_infantil_lista(),
        bebidas=bebidas_lista(),
        postres=postres_lista(),
        cocina=cocina_lista(),
    )


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    # esto solo funca usando python3 app.py
    app.run("0.0.0.0", port=8081, debug=True)
