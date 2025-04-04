# Discord Görev Takip Botu 

Discord üzerinden çalışan basit görev takip botu.

## Kurulum

1. Python 3.9x yükleyin.
2. Requirements.txt dosyasını kullanarak gerekli paketleri yükleyin. (pip install -r requirements.txt)
3. db.py dosyasını çalıştırarak database oluşturun.
4. Main dosyasının en altına inip token kısmını doldurun. (main.py dosyası 109. Satır)
5. Botu çalıştırmak için main.py dosyasını çalıştırın.

## Komutlar

- !add_task <görev_adı> : Görev ekleme komutu.
- !show_tasks : Görevleri görüntüleme komutu.
- !delete_task <görev_id> : Görev silme komutu.

## Testler

- test_add.py : Görev ekleme testi. ( Test Görevi ekler )
- test_show.py : Görevleri görüntüleme testi. (Database içindeki tüm görevleri gösterir)
- test_del.py : Görev silme testi. (Database içindeki bir görevi siler)
- test_complete.py : Görev tamamlama testi. (Database içindeki bir görevi tamamlandı olarak işaretler)







