from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Konfigurasi koneksi ke YugabyteDB
def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='yugabyte',
        user='yugabyte',
        password='',
        port='5433'
    )
    return conn

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Selamat datang di API YugabyteDB. Akses /buku atau /penulis"})

@app.route('/buku', methods=['GET'])
def get_buku():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM buku;')
    buku = cur.fetchall()
    cur.close()
    conn.close()
    
    # Format hasil ke JSON
    hasil = [{"id_buku": b[0], "judul": b[1], "id_penulis": b[2], "tahun_terbit": b[3]} for b in buku]
    return jsonify(hasil)

@app.route('/penulis', methods=['GET'])
def get_penulis():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM penulis;')
    penulis = cur.fetchall()
    cur.close()
    conn.close()
    
    # Format hasil ke JSON
    hasil = [{"id_penulis": p[0], "nama": p[1], "negara": p[2]} for p in penulis]
    return jsonify(hasil)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)