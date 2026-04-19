# Membuat Database MySQL di AWS EC2

1. Aktifkan Instance / VM di EC2
2. Remote SSH via Terminal
    - Masuk ke Folder penyimpanan Private Key AWS 
    - masukan command (ssh -i namafile.pem ubuntu@[IP_ADDRESS])
    - Tekan Enter
    - Keterangan open ssh hanya support di Windows 11
    - Jika menggunakan Windows 10 kebawah gunakan Putty
3. Lakukan Patching OS
    - sudo apt-get update && sudo apt-get upgrade

4. Kita akan install MariaDb
    - sudo apt-get install mariadb-server / mysql-server
    - sudo systemctl status mariadb
    - coba apakah default setting yg berlaku (sudo mysql -u root -p)
    - Cek apakah masih ada database dummy (show databases;)
![alt text](<WhatsApp Image 2026-04-19 at 19.57.49.jpeg>)
![alt text](<WhatsApp Image 2026-04-19 at 19.50.34.jpeg>)
5. Kita Lakukan Hardening Security
 - Masukan Command (sudo mysql_secure_installation)
 - masukan password kuat untuk user root
 - Remove anonymous users (Y)
 - Disallow root login remotely (Y)
 - Remove test database and access to it (Y)
 - Reload privilege tables now (Y)
![alt text](image.png)

6. Membuat database dan User 
 - Membuat database untuk Web Company Profile (create database dbCompro;)
 - Membuat User untuk Web Company Profile (create user 'userCompro'@'localhost' identified by '********';)
 - Memberikan Hak Akses User untuk Web Company Profile (grant all privileges on dbCompro.* to 'userCompro'@'localhost';)
 - Flush Privilege (flush privileges;)
 - Keluar dari MySQL (exit;)
![alt text](image-1.png)

7. Login sebagai user baru
 - Masukan Command (mysql -u userCompro -p)
 - Masukan Password
 - Cek apakah database dbCompro sudah ada (show databases;)
![alt text](<WhatsApp Image 2026-04-19 at 19.40.46.jpeg>)