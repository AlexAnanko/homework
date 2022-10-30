import psycopg2

try:

    connection = psycopg2.connect(user = "postgres",
                                  password = "",
                                  host = "localhost",
                                  port = "5432",
                                  database = "")

    cursor = connection.cursor()

    create_table_category = '''CREATE TABLE category
                                (id INT PRIMARY KEY NOT NULL,
                                name TEXT NOT NULL,
                                description TEXT NOT NULL);
                                '''
    cursor.execute(create_table_category)
    connection.commit()

    create_table_discounts = '''CREATE TABLE discounts
                                (id INT PRIMARY KEY NOT NULL,
                                name TEXT NOT NULL,
                                percent INT NOT NULL);
                                '''

    cursor.execute(create_table_discounts)
    connection.commit()

    create_table_products = '''CREATE TABLE products(
                                id INT PRIMARY KEY NOT NULL,
                                name VARCHAR(50) NOT NULL,
                                price INT NOT NULL,
                                category_id INT,
                                discounts_id INT,

                                CONSTRAINT FK_Products_Category FOREIGN KEY (category_id)
                                REFERENCES category (id)
                                ON DELETE CASCADE,

                                CONSTRAINT FK_Products_Discounts FOREIGN KEY (discounts_id)
                                REFERENCES discounts (id)
                                ON DELETE CASCADE
                                );
                                '''
    cursor.execute(create_table_products)
    connection.commit()

    with connection.cursor() as cursor:
        insert_category = '''INSERT INTO category (id, name, description) VALUES(1, 'Food',
        'Consumer goods for food use')'''
        cursor.execute(insert_category)
        connection.commit()
        insert_category = '''INSERT INTO category (id, name, description) VALUES(2, 'Drink',
        'Consumer products in liquid form for use in food')'''
        cursor.execute(insert_category)
        connection.commit()
        insert_category = '''INSERT INTO category (id, name, description) VALUES(3, 'Technologies',
        'Consumer technology products microelectronics and information technology')'''
        cursor.execute(insert_category)
        connection.commit()
        insert_category = '''INSERT INTO category (id, name, description) VALUES(4, 'Personal hygiene products',
        'Consumer Products for Personal Care Use')'''
        cursor.execute(insert_category)
        connection.commit()

    with connection.cursor() as cursor:
        insert_discounts = '''INSERT INTO discounts(id, name, percent) VALUES(1,'5%', 5)'''
        cursor.execute(insert_discounts)
        connection.commit()
        insert_discounts = '''INSERT INTO discounts(id, name, percent) VALUES(2,'10%', 10)'''
        cursor.execute(insert_discounts)
        connection.commit()
        insert_discounts = '''INSERT INTO discounts(id, name, percent) VALUES(3,'15%', 15)'''
        cursor.execute(insert_discounts)
        connection.commit()
        insert_discounts = '''INSERT INTO discounts(id, name, percent) VALUES(4,'30%', 30)'''
        cursor.execute(insert_discounts)
        connection.commit()
        insert_discounts = '''INSERT INTO discounts(id, name, percent) VALUES(5,'45%', 45)'''
        cursor.execute(insert_discounts)
        connection.commit()

    with connection.cursor() as cursor:
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(1, 'Bottle of water', 100, 2, 3)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(2, 'Bread', 75, 1, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(3, 'Milk', 85, 1, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(4, 'Butter', 90, 1, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(5, 'Cheese', 150, 1, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(6, 'NoteBook', 1500, 3, 3)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(7, 'TV', 990, 3, 4)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(8, 'Soap', 190, 4, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(9, 'iPhone', 1250, 3, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(10, 'Perfume', 560, 4, 5)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(11, 'Pasta', 125, 1, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(12, 'SD Card', 710, 3, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(13, 'Headphones', 350, 3, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(14, 'Deodorant', 160, 4, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(15, 'Soda', 85, 2, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(16, 'Beer', 115, 2, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(17, 'Toothbrush', 98, 4, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(18, 'PS4', 1440, 3, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(19, 'Potato', 15, 1, 3)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(20, 'Toothpaste', 70, 4, 3)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(21, 'Eggs', 45, 1, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(22, 'Detergent', 145, 4, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(23, 'SSD', 450, 3, 1)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(24, 'Keyboard', 210, 3, 2)'''
        cursor.execute(insert_products)
        connection.commit()
        insert_products = '''INSERT INTO products (id, name, price, category_id, discounts_id) VALUES(25, 'Shampoo', 180, 4, 4)'''
        cursor.execute(insert_products)
        connection.commit()


    price_from = int(input("Set price from: "))
    price_before = int(input("Set price before: "))

    with connection.cursor() as cursor:
        cursor.execute(
            f'''SELECT * FROM products 
            RIGHT JOIN category ON products.category_id=category.id
            RIGHT JOIN discounts ON products.discounts_id=discounts.id
            WHERE {price_from} <= products.price AND products.price <= {price_before}''')

        records = cursor.fetchall()
        head = ["ID","Name","Price","Category","Description","Discount"]
        print("\n————————————————————————————————————————————————————————————————————————————————————————", end="")
        print("————————————————————————————————————————————————————————")
        print(f"{head[0]:<3}|{head[1].center(17)}|{head[2].center(9)}|{head[3].center(27)}|", end="")
        print(f"{head[4].center(72)}|{head[5].center(10)}|")
        print("———|—————————————————|—————————|———————————————————————————|——————————————————————", end="")
        print("——————————————————————————————————————————————————|——————————|")
        for record in records:
                print(f"{record[0]:<2} | {record[1].center(15)} |{record[2]:^9}|{record[6].center(27)}|", end="")
                print(f"{record[7].center(72)}|{record[9].center(10)}|")
                print("———|—————————————————|—————————|———————————————————————————|————————————————————", end="")
                print("————————————————————————————————————————————————————|——————————|")
except (Exception, psycopg2.Error) as e:
    print(f"Error in process working with database: {e}")

finally:
    if connection:
        connection.close()
        cursor.close()
        print("Connection to database closed")