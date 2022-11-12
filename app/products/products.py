from flask import Blueprint, render_template, request, abort
from app.models import Fashion, Jewelry, Bicycle, Apparel
import sqlite3

products_bp = Blueprint("products_bp", __name__, template_folder="templates/products")


@products_bp.route("/apparels")
def apparels():
    page = int(request.args.get("page", 1))
    per_page = 10
    apparels = Apparel.query.paginate(page, per_page, error_out=False)
    if apparels is None:
        abort(404)
    else:
        return render_template("list.html", products=apparels, title="apparels")


@products_bp.route("/bicycles")
def bicycle():
    page = int(request.args.get("page", 1))
    per_page = 10
    bicycles = Bicycle.query.paginate(page, per_page, error_out=False)
    if bicycles is None:
        abort(404)
    else:
        return render_template("list.html", products=bicycles, title="bicycles")


@products_bp.route("/jewelry")
def jewelry():
    page = int(request.args.get("page", 1))
    per_page = 10
    jewelries = Jewelry.query.paginate(page, per_page, error_out=False)
    if jewelries is None:
        abort(404)
    else:
        return render_template("list.html", products=jewelries, title="jewelry")


@products_bp.route("/fashion")
def fashion():
    page = int(request.args.get("page", 1))
    per_page = 10
    fashions = Fashion.query.paginate(page, per_page, error_out=False)
    if fashions is None:
        abort(404)
    else:
        return render_template("list.html", products=fashions, title="fashion")


@products_bp.route("/<product>/<product_id>")
def view_product(product, product_id):
    # product = Jewelry(product)
    # product_items = product.return_items()
    # product_items = [dict(prod) for prod in product.return_items()]
    # product_name = [
    #     prod for prod in product_items if prod["name"].lower() == product_id
    # ]

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
            "view.html",
            results= envio,
            title=envio[1],
        )


@products_bp.route("/view")
def view():
    id = int(request.args.get("id"))
    product = Jewelry()
    product_items = product.show_all_items()
    product_items = [dict(prod) for prod in product_items if prod["id"] == id]
    print(product_items)
    return render_template(
        "view.html", results={"item": product_items}, title="Product View"
    )
