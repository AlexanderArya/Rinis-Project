from flask_mysqldb import MySQL  
from config import Config  
class LandingPageModel:
    def __init__(self, app):
        self.app = app
        self.mysql = MySQL(self.app)
        self.secret_key = app.config['SECRET_KEY']

    def get_property_with_image(self):
        cur = self.mysql.connection.cursor()
        query = "SELECT id_properties, nama_properti, tipe_properti, harga, alamat_properti, besar_properti, lebar_properti, deskripsi_properti, id_penjual, image_data FROM properties"

        cur.execute(query)
        property_data = cur.fetchall()

        cur.close()
        print(property_data)
        return ""
        if property_data:
            # Ambil data gambar (image_data) jika ada
            image_data = property_data['image_data']

            # Jika image_data ada, kamu bisa menyimpan file gambar ke sistem file
            if image_data:
                with open(f"property_image_{id_properties}.jpg", 'wb') as img_file:
                    img_file.write(image_data)

            return property_data
        else:
            return None
