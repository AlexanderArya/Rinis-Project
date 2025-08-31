from flask_mysqldb import MySQL  
from config import Config  
class DatabaseCreate:
    def __init__(self, app):
        self.app = app
        self.mysql = MySQL(self.app)
        self.secret_key = app.config['SECRET_KEY']

    # Membuat User
    def create_user(self, id_user, name, email, no_telp, alamat, role):
        cur = self.mysql.connection.cursor()
        query = """
            INSERT INTO users (id_user, name, email, no_telp, alamat, role) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_user, name, email, no_telp, alamat, role))
        self.mysql.connection.commit()
        cur.close()

    def create_property(self, id_properties, nama_properti, tipe_properti, harga, alamat_properti, besar_properti, lebar_properti, deskripsi_properti, id_penjual, image_path=None):
        cur = self.mysql.connection.cursor()

        # Membaca gambar jika ada
        image_data = None
        if image_path:
            with open(image_path, 'rb') as file:
                image_data = file.read()

        query = """
            INSERT INTO properties (id_properties, nama_properti, tipe_properti, harga, alamat_properti, besar_properti, lebar_properti, deskripsi_properti, id_penjual, image_data) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_properties, nama_properti, tipe_properti, harga, alamat_properti, besar_properti, lebar_properti, deskripsi_properti, id_penjual, image_data))
        self.mysql.connection.commit()
        cur.close()

        
    # Membuat Pembayaran
    def create_payment(self, id_payments, id_transaksi, payment_amount, payment_date, payment_methods, payment_status):
        cur = self.mysql.connection.cursor()
        query = """
            INSERT INTO payments (id_payments, id_transaksi, payment_amount, payment_date, payment_methods, payment_status) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_payments, id_transaksi, payment_amount, payment_date, payment_methods, payment_status))
        self.mysql.connection.commit()
        cur.close()
        
    # Membuat assingment
    def create_agent_property_assignment(self, id_assgn, id_agent, properties_id, id_prt, assgn_date, assgn_status):
        cur = self.mysql.connection.cursor()
        query = """
            INSERT INTO agent_property_assignment (id_assgn, id_agent, properties_id, id_prt, assgn_date, assgn_status) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_assgn, id_agent, properties_id, id_prt, assgn_date, assgn_status))
        self.mysql.connection.commit()
        cur.close()
        
    # Membuat Transaksi
    def create_transaksi(self, id_transaksi, jadwal_transaksi, total_harga, status_transaksi, id_user, properties_id):
        cur = self.mysql.connection.cursor()
        query = """
            INSERT INTO transaksi (id_transaksi, jadwal_transaksi, total_harga, status_transaksi, id_user, properties_id) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_transaksi, jadwal_transaksi, total_harga, status_transaksi, id_user, properties_id))
        self.mysql.connection.commit()
        cur.close()

    # Membuat Agent
    def create_agent(self, id_agent, id_user, nama, email, no_telp, alamat):
        cur = self.mysql.connection.cursor()
        query = """
            INSERT INTO agents (id_agent, id_user, nama, email, no_telp, alamat) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_agent, id_user, nama, email, no_telp, alamat))
        self.mysql.connection.commit()
        cur.close()

    # Membuat review
    def create_review(self, id_review, id_user, rating, comment, review_date, properties_id):
        cur = self.mysql.connection.cursor()
        query = """
            INSERT INTO reviews (id_review, id_user, rating, comment, review_date, properties_id) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_review, id_user, rating, comment, review_date, properties_id))
        self.mysql.connection.commit()
        cur.close()


