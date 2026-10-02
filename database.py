import sqlite3


DB_NAME = "orders.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            carrier TEXT,
            tracking_number TEXT,
            estimated_delivery TEXT
        )
    """)

    conn.commit()
    conn.close()


def seed_orders():
    conn = get_connection()

    cursor = conn.cursor()

    orders = [
        (
            "1001",
            "shipped",
            "DHL",
            "DHL123456",
            "2026-08-16"
        ),
        (
            "1002",
            "processing",
            None,
            None,
            "2026-08-19"
        ),
        (
            "1003",
            "delivered",
            "FedEx",
            "FDX789012",
            "2026-08-10"
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO orders
        VALUES (?, ?, ?, ?, ?)
    """, orders)

    conn.commit()
    conn.close()


def get_order(order_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            order_id,
            status,
            carrier,
            tracking_number,
            estimated_delivery
        FROM orders
        WHERE order_id = ?
    """, (order_id,))

    order = cursor.fetchone()

    conn.close()

    return order
