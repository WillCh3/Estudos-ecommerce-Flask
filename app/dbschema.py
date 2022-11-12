import csv
import sqlite3
import os
import random
import hashlib



def connect(database='site.db'):
    """Retorne uma conexão de banco de dados, por padrão para
    o DATABASE_NAME configurado
    Certifique-se de que a conexão esteja configurada para retornar objetos Row
    em vez de tuplas de consultas"""
    conexao = sqlite3.connect(database)
    conexao.row_factory = sqlite3.Row

    return conexao


def create_tables(db):
    """Cria e inicializa as tabelas do banco de dados"""

    sql = """
    
    DROP TABLE IF EXISTS jewelry;
    CREATE TABLE jewelry (
            id integer unique primary key autoincrement,
            name text,
            description text,
            image_url text,
            category text,
            inventory integer,
            unit_cost number
            );
    """

    db.executescript(sql)
    db.commit()


def sample_data(db):
    """Gere alguns dados de amostra para testar a web
    inscrição. Apaga todos os dados existentes no
    base de dados
    Retorna a lista de usuários e a lista de posições
    que são inseridos no banco de dados"""

    cursor = db.cursor()
    cursor.execute("DELETE FROM jewelry")

    # read sample product data from apparel.csv
    jewelry = {}
    id = 0
    first = True  # flag
    sql = "INSERT INTO jewelry (id, name, description, image_url, category, inventory, unit_cost) VALUES (?, ?, ?, ?, ?, ?, ?)"
    with open(os.path.join(os.path.dirname(__file__), "jewelry.csv")) as fd:
        reader = csv.DictReader(fd)
        for row in reader:
            if row["Title"] is not "":
                if first:
                    inv = 0  # inventory of first item (Ocean Blue Shirt) is zero
                    first = False
                else:
                    inv = int(random.random() * 100)
                cost = int(random.random() * 200) + 0.95
                description = "<p>" + row["Body (HTML)"] + "</p>"
                data = (
                    id,
                    row["Title"],
                    description,
                    row["Image Src"],
                    row["Tags"],
                    inv,
                    cost,
                )
                cursor.execute(sql, data)
                jewelry[row["Title"]] = {
                    "id": id,
                    "name": row["Title"],
                    "description": description,
                    "category": row["Tags"],
                    "inventory": inv,
                    "unit_cost": cost,
                }
                id += 1

    db.commit()

    return jewelry


if __name__ == "__main__":
    db = connect('site.db')
    create_tables(db)
    sample_data(db)
