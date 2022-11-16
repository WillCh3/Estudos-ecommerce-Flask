
import sqlite3
from loja import app
from flask import render_template, abort



@app.route('/')
def home():
    return render_template("/index/index.html", title="Home")

@app.route('/login/')
def login():
    return render_template("/login/login.html", title="Login")

@app.route('/register/')
def register():
    return render_template("/login/signup.html", title="register")

@app.route('/recuperar_senha/')
def recuperar_senha():
    return render_template("/login/forgot_password.html", title="recuperar senha")

@app.route('/produtos/po/')
def produtos_po():
    db = sqlite3.connect('site.db')
    cursor = db.cursor()
    itens = cursor.execute( "SELECT * FROM po")
    products = itens.fetchall()
    print(products)

    return render_template("/produtos/list.html", products = products, title="po")

@app.route('/produtos/graos/')
def produtos_graos():
    db = sqlite3.connect('site.db')
    cursor = db.cursor()
    itens = cursor.execute( "SELECT * FROM graos")
    products = itens.fetchall()
    print(products)

    return render_template("/produtos/list.html", products = products, title="graos")


@app.route('/produtos/capsula/')
def produtos_capsula():
    db = sqlite3.connect('site.db')
    cursor = db.cursor()
    itens = cursor.execute( "SELECT * FROM capsulas")
    products = itens.fetchall()
    print(products)

    return render_template("/produtos/list.html", products = products, title="capsula")

@app.route('/produtos/soluvel/')
def produtos_soluvel():
    db = sqlite3.connect('site.db')
    cursor = db.cursor()
    itens = cursor.execute( "SELECT * FROM soluvel")
    products = itens.fetchall()
    print(products)

    return render_template("/produtos/list.html", products = products, title="soluvel")


@app.route("/produtos/<product>/<product_id>")
def view_product(product, product_id):

    conexao = sqlite3.connect('site.db')
    cursor = conexao.cursor()
    res = cursor.execute(f"""
                            SELECT * FROM {product.lower()}
                            WHERE id = {product_id}
                        """)
    envio = res.fetchone()
    print(f'\n\n\n{envio[1]}\n\n\n')

    if envio == False:
        abort(404)
    else:
        return render_template(
            "/produtos/view.html",
            results= envio,
            title=envio[1],
        )

# @app.route("/carrinho/<product>/<product_id>")
# def view_product(product, product_id):

#     conexao = sqlite3.connect('site.db')
#     cursor = conexao.cursor()
#     res = cursor.execute(f"""
#                             SELECT * FROM {product.lower()}
#                             WHERE id = {product_id}
#                         """)
#     envio = res.fetchone()
#     print(f'\n\n\n{envio[1]}\n\n\n')

#     if envio == False:
#         abort(404)
#     else:
#         return render_template(
#             "/produtos/view.html",
#             results= envio,
#             title=envio[1],
#         )

@app.route('/carrinho/')
def carrinho():
    return render_template("/carrinho/carrinho.html", title="Carrinho")


#------------------------------------User ------------------------------------------------------------#
