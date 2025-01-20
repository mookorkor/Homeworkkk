 m509 = ['julaluck   kongjaroon' ,'Traikoon   Boonnam','Woranasak   Kaitphichetchuen' ,'Nontawat   Khamduang','Panupong   Saison',
    'punnagron   phungsuwan','Wissarut   Klinrueang','Amornthep   Unno','Jakkrich   testong','Jiratha    Noisree','Kornpipat   Leknak',
    'Phattharaphon 	  Chomput','Supachai   Rungsang','Pharat   Dananansuk','Ruangwit   Chokchai',
    'Jirayut   Buranachan ','Natcha   Kumpa','Savitri   Minsaman ','Bannaporn   Siriphan','Yanisa   Phaungpee ',
    'Kityada   Jitwimonrat','Sudarat   Suanyim','Ploypraphat   Pissaruk','Thatchanok   Samai','Pearpilai   Boonkrong ',
    'Kanyaphorn   Sittiwong ','Kankao   Sittho','Kittima   Kreidarporn','Apitsada   Wachirasreesoontra','Sirikarn   Baotun','Kanyawee   Udomsaree',
    'Nattarinee   Chimreaung','Pichporn   Meechoksom','Kannisa   Ratrueangudom','Chuda   Sariphan ','Kanta   Piyapattharakul',
    'Napaspornprom  Tancharakorn','Kingkan   Roumpol',
    'Wachiraya   Wachiranawin']
  for i in m509:
    print(i)
  print('จำนวนรายชื่อนักเรียนชั้น 5/9 : ',len(m509),' คน')
  print('------------------------------------------------------------------------\n')
  print("รับค่าจำนวนเต็ม 1 จำนวน เเล้วเเสดงตารางสูตรคูณของตัวเลขที่รับเข้ามา")
  number = int(input("กรอกตัวเลขจำนวนจริงเพื่อสร้างตารางสูตรคูณ : "))
  for i in range(1,13) :
    print(f'{number} x {i} = {number * i }')
