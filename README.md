# Cloud-Native URL Shortener Microservice

Layanan REST API pemendek URL berperforma tinggi yang dibangun menggunakan Python, Flask, dan Redis sebagai caching layer berkecepatan tinggi, serta dikontainerisasi sepenuhnya menggunakan Docker.

## 🚀 Fitur Utama
- **REST API Entrypoints**: Endpoint untuk memendekkan URL (`POST /shorten`) dan mengalihkan URL (`GET /<short_code>`).
- **High-Speed Caching**: Integrasi Redis In-Memory Database untuk proses redirect secepat kilat dengan TTL otomatis 24 jam.
- **Dockerized Infrastructure**: Orkestrasi multi-container menggunakan Docker Compose untuk menjamin konsistensi runtime.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Database/Cache**: Redis
- **DevOps/Infrastructure**: Docker, Docker Compose

## 🏃 Menjalankan Aplikasi
Pastikan Docker Desktop sudah aktif, lalu jalankan perintah berikut di terminal:
```bash
docker-compose up --build