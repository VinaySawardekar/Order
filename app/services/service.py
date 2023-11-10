from ..db import db 

cur = db.conn.cursor()

def get_all_order():
    cur.execute('SELECT * FROM orders')
    orders = cur.fetchall()
    if orders is None:
        return []
    return orders

def get_order(id):
    if id :
        cur.execute('SELECT * FROM orders WHERE id = %s', (id,))
        order = cur.fetchone()

        if order is None:
            return {}
        return order
    else:
        return {}
    

def create_order(order):
    cur.execute('INSERT INTO orders (user_id, product_price, quantity, total_price) VALUES (%s, %s, %s, %s)', (order['user_id'], order['product_price'], order['quantity'], order['total_price']))
    db.conn.commit()
    new_order_id = cur.lastrowid
    return get_order(new_order_id)


def update_order(id, order):
    print(order)
    cur.execute('UPDATE orders SET user_id = %s, product_price = %s,quantity = %s, total_price = %s WHERE id = %s', (order['user_id'], order['product_price'],order['quantity'], order['total_price'], id))
    db.conn.commit()
    return get_order(id)

def delete_order(id):
    cur.execute('DELETE FROM orders WHERE id = %s', (id,))
    db.conn.commit()
    deleted_id = cur.lastrowid
    return deleted_id