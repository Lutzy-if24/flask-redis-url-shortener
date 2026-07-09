# Gunakan base image Python resmi yang ringan
FROM python:3.10-slim

# Tentukan folder kerja di dalam container
WORKDIR /app

# Salin file requirements atau langsung install library
RUN pip install flask redis

# Salin seluruh kode proyek kita ke dalam container
COPY app.py /app/app.py

# Buka port 5000 di dalam container
EXPOSE 5000

# Perintah untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]