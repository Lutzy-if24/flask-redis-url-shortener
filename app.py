from flask import Flask, jsonify, request, redirect
import redis  # 1. Tambahkan import redis di paling atas

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    return jsonify({"message": "Layanan URL Shortener Microservice Aktif!"})

# 1. Endpoint untuk memendekkan URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('url')
    
    if not long_url:
        return jsonify({"error": "Silakan masukkan URL panjang!"}), 400
        
    short_code = str(abs(hash(long_url)))[:6]
    
    # 3. PERUBAHAN DI SINI:
    # Ganti url_db[short_code] = long_url menjadi penyimpanan ke Redis
    # Kita set waktu kedaluwarsa otomatis (TTL) selama 24 jam (86400 detik)
    redis_client.setex(short_code, 86400, long_url)
    
    short_url = f"http://localhost:5000/{short_code}"
    
    return jsonify({
        "original_url": long_url,
        "short_url": short_url
    }), 201

# 2. Endpoint untuk redirect dari URL pendek ke URL asli
@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    # 4. PERUBAHAN DI SINI:
    # Ganti long_url = url_db.get(short_code) menjadi mengambil data dari Redis
    long_url = redis_client.get(short_code)
    
    if long_url:
        return redirect(long_url)
    else:
        return jsonify({"error": "URL tidak ditemukan atau sudah kedaluwarsa!"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)