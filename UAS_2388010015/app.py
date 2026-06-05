from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>UAS Administrasi Server Berhasil!</h1><p>Nama: Mohamad Kadik</p><p>NIM: 2388010015</p><p>Aplikasi Python Dinamis berjalan di Docker.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
