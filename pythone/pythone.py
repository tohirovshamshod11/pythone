# # a=1
# # b=2
# # c=a+b
# # print(c)
# # for i in range(1,51):
# #     if i % 5 == 0 and i % 3 == 0:
# #         print(i,'FizzBuzz')
# #     elif i % 5 == 0:
# #         print(i,'Buzz')
# #     elif i % 3 == 0:
# #         print(i,'Fizz')
# #DICTINARY
# # bobom = {'ism':'Baltayev Tohir','yosh':63,'t_yil':'1962','t_joy':'Xorazm viloyati'}
# # print(bobom)
# # buvim
# # otam = {'ism':'Elmurod Baltayev','yosh':38,'t_yil':1968,'t_joy':'Xorazm viloyati'}
# # print(otam)
# # onam = {'ism':'Shahodat Karimova','yosh':38,'t_yil':1968,'t_joy':'Xorazm viloyati'}
# # print(onam)
# # talaba_0 = {
# #     'ism':'alijon',
# #     'familiya':'shamshiyev',
# #     'yosh':22,
# #     'fakultet':'matematika',
# #     'kurs':4
# #     }

# # print(talaba_0.items())

# #Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin
# # 443
# # print(talaba_1.items())

# #Bu metodni to'g'ridan-to'g'ri emas, for tsikli yordamida chaqirish orqali lug'atdagi barcha elementlarni tushunarliroq shaklda ko'rishimiz mumkin.

# # for kalit, qiymat in talaba_1.items():
# #     print(f"Kalit: {kalit}")
# #     print(f"Qiymat: {qiymat} \n")

# #Qisqartma shakli
# # telefonlar = {
# #     'Ustoz':'iphone 15 pro',
# #     'Shamshod':'galaxy a34 5G',
# #     'Shahzod':'Redmi iphonedan ko\'piya',
# #     'Xusan':'A32',
# #     'Xasan':'A10'   
#     # }
# # for k,q in telefonlar.items():
# #     print(f"{k.title()} ning telefoni {q}")
# # print(telefonlar.values())

# #Amaliyot
# #1
# # izohli_lugat={
# #     "Boolen":"Boolen - Mantiqiy qiymat",
# #     "Float":"Float - Onlik son",
# #     "For":"For - Biror amalni qayta-qayta bajarish",
# #     "If":"If - Shartlarni tekshirish aperatori",
# #     "Integer":"Integer - Butun son"
# # }
# # print(izohli_lugat["Boolen"])
# # print(izohli_lugat["Float"])
# # print(izohli_lugat["For"])
# # print(izohli_lugat["If"])
# # print(izohli_lugat["Integer"])

# #Nesting

# # car0 = {
# #         'model':'lacetti',
# #         'rang':'oq',
# #         'yil':2018,
# #         'narh':13000,
# #         'km':50000,
# #         'korobka':'avtomat'
# #         }

# # car1 = {
# #         'model':'nexia 3',
# #         'rang':'qora',
# #         'yil':2015,
# #         'narh':9000,
# #         'km':89000,
# #         'korobka':'mexanika'
# #         }

# # car2 = {
# #         'model':'gentra',
# #         'rang':'qizil',
# #         'yil':2019,
# #         'narh':15000,
# #         'km':20000,
# #         'korobka':'mexanika'
# #         }
# # cars=(car0,car1,car2)
# # for car in cars:
# #     print(f"{car['model'].title()}, "
# #           f"{car['rang']}rang, "
# #           f"{car['yil']}-yil, {car['narh']}$" )4

# # buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
# #            'tyil':810,
# #            'vyil':870,
# #            'tjoy':'Buxoro',
# #            'yzasar':' „Al-jomeʼ as-sahih“, „Al-adab al-mufrad“, „At-tarix al-kabir“, „At-tarix as-sagʻir“, „At-tarix al-avsat“, „At-tafsir al-kabir“ „Birrul volidayn“, „Asmo as-sahoba“, „Kunyalar“ va boshqalar.'
# #            }

# # qodiriy = {'ism':'Abdulla Qodiriy',
# #            'tyil':1894,
# #            'vyil':1938,
# #            'tjoy':'Toshkent'
# #            }

# # vohidov = {'ism':'Erkin Vohidov',
# #            'tyil':1936,
# #            'vyil':2016,
# #            'tjoy':"Farg'ona"
# #            }

# # navoiy = {'ism':'Alisher Navoiy',
# #            'tyil':1441,
# #            'vyil':1501,
# #            'tjoy':"Xirot"
# #            }
# # shaxslar=[buxoriy,qodiriy,vohidov,navoiy]

# # for shaxs in shaxslar:
# #     ism = ['ism']
# #     tyil = ['tyil']
# #     vyil = ['vyil']
# #     tjoy = ['tjoy']
# #     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
# #           f"{vyil-tyil} yil umr ko'rgan.")
# # print('Buxoriyning mashxur asarlari:')
# # print(buxoriy['yzasar'])
# #O'TILGANLAR BILAN ISHLASH
# #1
# # car_1 = {
# #     'Model':'Cobalt',
# #     'rangi':'Oq',
# #     'carobka':'Mexanik'
# #          }
# # print(car_1)
# #2
# # fish={}
# # fish = {
# #     'ism':'shamshod',
# #     'fam':'Tohirov',
# #     't_yil':'2010',
# #     't_kun':'5-iyul',
# # }
# # print(f"{fish['fam'].title()}, {fish['ism'].title()},{fish['t_yil']}-yil,{fish['t_kun']}da tug'ilgan")
# #3
# # fish1 = {
# #     'ism':'shamshod tohirov',
# #     'mk':'11',
# #     'yosh':'14'
# # }
# # print(f"Ismi:{fish1['ism'].title()},{fish1['mk']}-maktabda taxsil oladi,{fish1['yosh']}-yoshda.")
# #4
# # phone = fish1.get('Shamshod','Shamshod bunday ism yoq kuuu')
# # print(phone)
# #5
# # bobom = {'ism':'Baltayev Tohir','yosh':63,'t_yil':1962,'t_joy':'Xorazm viloyati'}
# # buvim={'ism':'Rozmetova Nazira','yosh':63,'t_yil':1962,'t_joy':'Xorazm viloyati'}
# # otam = {'ism':'Elmurod Baltayev','yosh':38,'t_yil':1968,'t_joy':'Xorazm viloyati'}
# # onam = {'ism':'Shahodat Karimova','yosh':38,'t_yil':1968,'t_joy':'Xorazm viloyati'}
# # print(f"{bobom['ism']},{bobom['t_yil']}-yilda,{bobom['t_joy']}-da tugilgan,{bobom['yosh']}-yoshda")
# # print(f"{buvim['ism']},{buvim['t_yil']}-yilda,{buvim['t_joy']}-da tugilgan,{buvim['yosh']}-yoshda")
# # print(f"{otam['ism']},{otam['t_yil']}-yilda,{otam['t_joy']}-da tugilgan,{otam['yosh']}-yoshda")
# # print(f"{onam['ism']},{onam['t_yil']}-yilda,{onam['t_joy']}-da tugilgan,{onam['yosh']}-yoshda")

# # LUG'AT ELEMENTLARI BILAN ISHLASH

# #1 items() Metodi
# # oquvchi ={
# #     'ism':'shamshodbek tohirov',
# #     'yosh':'14',
# #     'tugilgan yil':'2010',
# #     'tuguilgan joy':'xorazm viloyati'
# # }
# # print(oquvchi['ism'].title())

# #2 items()ni for bilan iwlatw
# # for kalit,qiymat in oquvchi.items():
# #     print(f"kalit: {kalit}")
# #     print(f"qiymat: {qiymat} \n")

# #3 Chiroyli ko'rinishda iwlaw
# telefonlar = {
#     'Shamshod':'A34',
#     'Behruz':'A 01',
#     'Shahzod':'Redmi',
#     'Shelli':'A10'
# }
# # for k, q in telefonlar.items():
# #     print(f"{k.title()}ning telefoni:{q}")

# #4
# narsalar  = {
#     'olma':'1200',
#     'nok':'1300',
#     'bexi':'2000',
#     'olxori':'1500'
# }
# # print('Do\'kondagi maxsulotlar')
# # for narsa in narsalar

# #5 Tepadagi codni yaxshiroq qilib chiqaramiz

# bozorlik = ['olma','nok','bexi','banan']
# # for narsa in narsalar:
# #     if narsa in bozorlik:
# #         print(f"{narsa.title()}:{narsalar[narsa]}")

# #6 Tepadagi codda yoq narsani qanday chiqarishni o'rganamiz
# # for buyum in bozorlik:
# #     if buyum  not in narsalar:
# #         print(f"Iltimos do'koningizga {buyum.title()} ham olib kelib qo'ying")

# #7 .values() METODI

# # print(telefonlar.values())

# #8 values() dan foydalanib ajoyib narsa yaratamiz 

# # print('Do\'stlarimiz foydalaniladigan telefonlar:')
# # for tel in telefonlar.values():
# #     print(tel)

# #9 AMALIYOT
# #1
# # bir = {
# #     'Boolen':'Mantiqiy qiymat',
# #     'Float':'O\'nlik son',
# #     'For':'Biror amalni qayta-qayta bajarish',
# #     'If':'Shartlarni tekshirish',
# #     'Integer':'Butun son'
# # }
# # print(sorted(bir))

# #2
# dav = {
#     'Aqsh':'Washington',
#     'italiya':'Rim',
#     'Malayzya':'Kuala_Lampur',
#     'O\'zbdekiston':'Toshkent',
#     'Qirg\'iziston':'Nursulton',
#     'Qozog\'iston':'Dushanbe',
#     'Rossiya':'Moskwa',
#     'Singapur':'Singapur',
#     'Tojikiston':'Bishkek'
# }
# # print('Dunyo davlatlari:   Davlatlarning poytaxtlari:')
# # for k,q in dav.items():
# #     print(k, "   ", q)

# #3 
# # davvlat=input('Hohlagan davlatingizni kiriting>>>>>>')
# # if davvlat in dav:
# #     print(f"{davvlat}ning poytaxti.{dav}[dav]")
# # else:
# #     if davvlat not in dav:
# #         print("Bizda bunday poytaxt yo'q")

# #4
# # ovqatlar = {
# #     'Osh':'50000',
# #     'Manti':'40000',
# #     'Suzma':'20000',
# #     'Shaovla':'2000',
# #     'Baliq':'60000',
# #     'Qovurilgan baliq':'65000',
# #     'Dimlangan baliq':'120000',
# #     'Tovuq oyoqlari':'30000',
# #     'Steyk':'70000',
# #     'Omlet':'15000'
# # }
# # print('Bizning restoranimizda barcha ovqatlar hozirgi vaqatda skidkada.')
# # taom = input('3 ta ovqat buyurtma qilishingiz mumkin>>>>>')
# # buyurtmalar = []
# # for ovqat in ovqatlar:

# #NESTING

# #1
# car_1 = {
#     'model':'Cobalt',
#     'rang':'Oq',
#     'yil':'2022',
#     'karobka':'Mexanik'
# }
# car_2 = {
#     'model':'Nexia 1',
#     'rang':'Sariq',
#     'yil':'1999',
#     'karobka':'Mexanik'
# }
# # cars = [car_1, car_2]
# # for car in cars:
# #     print(f"{car['model']}, "
# #           f"{car['rang']} rang",
# #           f"{car['yil']}-yil",
# #           f"{car['karobka']}"
# #     )

# #2
# # print(cars[1])

# #3
# # malibu = []
# # for n in range(10):
# #     malibus = {
# #         'rusumi':'Malibu',
# #         'rangi':'None',
# #         'yil':'2023',
# #         'narxi':'None',
# #         'karobka':'Avtomat'
# #     }
# #     for malibu in malibus[:5]:
# #         malibu['rang']='qora'
# #         for malibu in malibus[6:8]:
# #             malibu['rang']='ko\'k'
# #             for malibu in malibus[9:10]:
# #                 malibu['rang']='oq'
# #     print(malibus)

# #4
# # dasturchilar = {
# #     'Shamshod':['Html','Css','Phyton'],
# #     'Shahzod':['Html','Java'],
# #     'Behruz':['C++','Java Scrip'],
# #     'Sherzod':['Phyton','Php']
# # }
# # for k,q in dasturchilar.items():
# #     print(f"\n{k} quyidagi dasturlash tillarni biladi:")
# #     for til in q:
# #         print(til.upper())

# #5
# #Amaliy 1 da

# # #AMALIYOT
# buyuklar = {
# 'qodiriy' = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            },

# 'vohidov' = {
#                 'ism':'Erkin Vohidov',
#                 'tyil':1936,
#                 'vyil':2016,
#                 'tjoy':"Farg'ona",
#                 'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            },

# 'navoiy' = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
# }
# # print('Buyuk allomalar')
# # print(f"{qodiriy['ism']} {qodiriy['tyil']}-yilda {qodiriy['tjoy']} shahrida tug'ilgan. {qodiriy['vyil']}-yilda vafot etgan.\n")
# # print(f"{vohidov['ism']} {vohidov['tyil']}-yilda{vohidov['tjoy']} viloyatida tug'ilgan. {vohidov['vyil']}-yilda vafot etgan.\n")
# # print(f"{navoiy['ism']} {navoiy['tyil']}-yilda {navoiy['tjoy']} shahrida tug'ilgan. {navoiy['vyil']}-yilda vafot etgan.")

# #2
# shaxslar_a = [vohidov,qodiriy,navoiy]
# for shaxs in shaxslar_a:
#     ism = shaxs['ism']
#     ism  = shaxs['asarlar']
#     print(f"\n{ism}-ning asarlari:")
#     for asar in  asarlar:
#         print(asar)

# #3
# # birinchi = input('\'Ozingizning yoqtirgan 3 ta filmingizni yozing>>>>')
# # kinolar = {
# #     'ali':['Terminator','Rambo','Titanic'],
# #     'vali':['Tenet','Inception','Interstellar'],
# #     'hasan':['Abdullajon','Bomba','Shaytanat'],
# #     'husan':['Mahallada duv-duv gap','John Wick']
# #     }
# # if k,kinolar in kinolar:
# #     print(f"\n{ism[kinolar]}")

# #TEstlar

# #1
# my_list = []

# my_list.append(3)
# my_list.append(5)
# my_list.append(2)
# my_list.append(6)
# my_list.append(8)
# my_list.append(23)

#3
# print(sum(my_list))

#4
# yangi_r = []
# r = [2,5,7,9,10,12]

# for yangi in r:
#     if yangi % 2== 0:
#         print('Bu toq son')
#     elif  yangi % 2 == 1:
#         print('Bu toq emas')

#5
# print(max(r))

#6
# for yangi in r:
#     yangi_r.append(yangi * 2)
# print(yangi_r)

#7 Element o'chirish
# del(r[2])
# print(r)

#8 NAbarot yozish
# r.reverse()
# print(r)

#9
# dic = {
#     'name':'Ali',
#     'city':'Toshkent',
#     'age':25
# }

#10
# if 'age' in dic:
#     print(dic['age'])
#     print('Bunday kalit so\'z bor')
# else:
#     print(('Kalit so\'z yoq'))

#11
# son = []
# summa = 0
# for raqamlar in r:
#     if raqamlar % 2 == 0:
#         son.append(raqamlar)
#         summa= + 1
# print(len(son))
# print(summa)

#12
# my_list = [5,10,15,20,25,30,35,40]
# for son in my_list:
#     if son % 3==0  and son %5 ==0:
#         print("Bu son 3 ga va 5 ga bo'linadi.")
#     elif son % 2==0:
#         print('Son 2 ga bo\'linadi')
#     elif son % 3==0:
#         print('BU son 3 ga bo\'linadi')
#     elif son % 5==0:
#         print('Bu son 5 ga bo\'linadi.')
#13
# print(sorted(my_list))

#14
# ism = input('Ismingizni yozing>>> ')
# yosh = int(input('Yoshingiz nechida>>> '))
# shar = input('Siz qayerda yashaysiz>>> ')
# dicc = {'ism': ism, 'yosh': yosh, 'shar': shar}
# print(dicc['yosh'] + 1)

#15
# words = ['Apple','Banana','Cherry','Date']
# e_u_soz = max(words,key=len)
# print('Eng uzun so\'z:',e_u_soz)

#16
# myy_list = [1,2,3,4]
# dictt = [myy_list]
# print(myy_list * 2)

#17
# togrisi = {
#     'a':'1',
#     'b':'2',
#     'c':'3'
# }
# yolgpni = swapped_dict = {value: key for key, value in togrisi.items()}
# # print(yolgpni)
# #18
# numbers = [1, 2, 2, 3, 1, 4, 1, 3, 2]

# #19
# list1 = [1,2,3]
# list2 = [4,5,6]

#Testlar

#2
# ism = input("Ismingizni yozing? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
#Testlar    

#1
# mevalar =['Olma','banan','gilos']
# print(mevalar)

#2
# mashinalar = ["BMW", "Toyota", "Honda"]
# mashinalar.append("Mers")
# mashinalar.remove("Honda")
# print(mashinalar)

#3
# shaharlar = ["Samarqand","Buxora"]
# shaharlar

#4
# sonlar = [1, 2, 3, 4, 5, 6]
# for son in sonlar:
#     if son %2==0:
#         print("Bu sonlar juft sonlardir:",son)

#5
# oquvchilar = ["Ali", "Vali", "Sanjar"]
# print(len(oquvchilar))

#6
# sonlar = [2, 3, 4]
# for son in sonlar: 
#     print(son **2)

#7 Internetni iwlagani
# son = [5]
# for sonlar in son:
#     if sonlar %2 ==0:
#         print("Bu son juft ekan.")
# # else: sonlar %2 != 0
# print("Bu son toq ekan.")

#Meni iwlaganim
# son = [5]
# for sonlar in son:
#     if sonlar %2 ==0:
#         print("Bu son juft ekan.")
# # else: sonlar %2 != 0 
# print("Bu son toq ekan.")

#8
# talaba = {"ism": "Ali", "yoshi": 16}
# for sinf in talaba:
#     print('Mana')
# else:
#     print("Uzr yoq ekan",sinf)

#9
# alo = int(input("Bugun siz qanday baxo oldingiz."))
# baxolar = [5,4,3,2,1]
# # for baxo in baxolar:
# if alo <=5:
#     print(alo,"Siz bugun alo baxo olibsiz.")
# elif alo <=4:
#     print(alo,"Siz bugun yaxshi baxo olibsiz.")
# else:
#     print(alo,"Siz bugun yaxshi baxo ololmabsiz,umid qilamanki ertaga yaxwi baxo olasiz.")

#10
# talaba = {"ism": "Ali", "yosh": 16, "sinfi": 8}
# # print(talaba.values())
# # print(talaba.keys())
# print(talaba)

#11 Domillodan so'ra

#12
# raqamlar = [1, 2, 3, 4, 5]
# raqamlar.reverse()
# print(raqamlar)

#13
# sonlar = [3, 7, 1, 9, 2]
# print(max(sonlar),min(sonlar))

#14
# ballar = [3, 4, 5, 6, 7]
# print(sum(ballar) /2)

#15Domillodan sora

#16 80% iwlandi oryonini domilodan sora
# raqamlar = [1, 2, 3, 4, 5, 6]
# for raqam in raqamlar:
#     if raqam %2==0:
#         print(raqam)

#17 Domillodan sora
# sozlar = ["kitob", "qalam", "stol"]
# rezultat = get_first_letters(sozlar)
# print(rezultat)

#18
# baholar = [85, 90, 78, 92]
# print(max(baholar))

#19
# oquvchilar =[
#     {"ism": "Vali", "sinfi": 7},
# ]
# for i in oquvchilar:
#     print(i['ism'])
#     print(i['sinfi'])

#20 Tuwinmading jilli domillodan so'risan mnam indi tupoy
# talabalar = [
#     {"ism": "Ali", "sinfi": 8, "fanlar": ["matematika", "fizika"]},
#     {"ism": "Vali", "sinfi": 7, "fanlar": ["biologiya", "kimyo"]},
# ]
# print(talabalar)

#WHILE
#1
# ism = input("Ismingiz nima>>>")
# print(f'Salom  {ism.title()}')

#2

# ism = input("Ismingiz nima>>>")
# savol = (f'Salom  {ism.title()}.Yoshingiz nechida.')
# print(savol)

#3 Malumotlar
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input('Bo\'yingiz necha santimetr:')
# height = int(height)
# hammasi = (f"Siz haqingizda malumot:Ismingiz {ism} yoshingiz {yosh} bo'yingiz {height}cm")
# print(hammasi)

#4
# son = 1
# while son <=5:
#     print(son , end=' ')
#     son = son +1

#5
# print("Istalgan sonni kvadratini topuvchi dastur")
# savol=  ("Istalgan sonni kiriting,")
# savol += ("To'xtatish uchun 'exit'deb yozing>>>")
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat!= 'exit':
#         print(float(qiymat)**2)

#6
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)


#7
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son}-ning kvadrati {son **2} ga teng")

#8
# sonlar = range(1,16)
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son}-nig kvadrati{son **2}ga teng")

#9

#While Amaliyoti
#1
# sorash = input("Yaxshi ko'rgan kitobingizni kiriting.")
# sorash +=("To'xtatish uchun 'stop' deb yozing")
# q = ''
# while q != 'stop':
#     q = input(sorash)
#     if q!= 'exit':
#         print(q)

#2

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

#3
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

#WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

#1
# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

#2
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho

#FUNKSIYA

#1
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
# salom_ber()

#2
# def salom_ber(ism):
#     """Fodyalanuvchi ismini 
#     qabul qilib, 
#         unga salom beruvchi 
#         funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('Bekzod')

#3
# print(salom_ber.__doc__)

#4
# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchining ismi:{ism.title()}\n"
#           f"Foydalanuvchining familiyasi:{familiya.title()}")
# toliq_ism('shamshodbek','tohirov')


#5
# def yoshni_hisobla(ism,tg_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024 - tg_yil} yoshda.")
# yoshni_hisobla('Shamshod',2010)

#6
# yoshni_hisobla(tg_yil=2010, ism='shamshod')

#7
# def yosh_hisob(tg_yil,jory_yl=2024):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Sizn {jory_yl - tg_yil} yoshdasiz")
# yosh_hisob(2010,2024)

#8
# def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)

#Amaliyot
#1
# def hisobla(tugilgan_yil, joriy_yil=2024):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""

#     print(f"Siz { int(yosh)-joriy_yil}-yilda tug'ilgansiz.")
    

# ism = input("Ismingizni yozing:")
# yosh = input("Yoshingizni yozing:")
# hisobla(2010)

#2
# print("Hohlagan soningizni Kubini va Kvadratini chiqaruvchi funksiya")
# son =float(input("Hohlagan soningizni kiriting:"))
# print(f"Mana marhamat:{son**2}")
# print(f"Mana marhamat:{son **3}")

#QIYMAT QAYTARUVCHI FUNKSIYA
#1
# def ism_yasa(ism,familiya):
#      """Toliq isma qaytaruvchi funksiya"""
#      ism_yasa = f"{ism.title()} {familiya.title()}"
#      return ism_yasa
# oquvchi1 = ism_yasa('shamshod','tohirov')
# oquvchi2 = ism_yasa('saidov','behruz')
# print(f"Darsga kelmagan o'quvchilar {oquvchi1} va {oquvchi2}")
#2
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ismi qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism. title()

# talaba1 = toliq_ism_yasa('Shamshod', 'Tohirov')
# talaba2 = toliq_ism_yasa('Behruz', 'Saidov', 'Mansurovich')
# print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}.")


#3

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=''):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rangi':rangi,
#             'karobka':korobka,
#             'yili':yili,
#             'narhi':narhi
#             }
#     return avto
# avto1 = avto_info('GM','Cobalt','Oq','Mexanik',2022,150000)
# avto2 = avto_info('GM','Nexia 1','Sariq','Mexanik',1999)
# avtolar = [avto1,avto2]
# print("Bozorda mavjud mashinalar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = "Nomalum"
#         print(  f"{avto['rangi']},{avto['model']},{avto['narhi']}")
# 4
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#5
#     print("Sizning avtomabilingizni ro'yhatini yaratamiz.")
# avtolar = []
# while True:
#     print("Quyidagi malumotlarni kiriting.")
#     kompany = input("Ishlab chiqaruvchi:")    
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
#     avtolar.append(avto_info(kompany, model, rangi, korobka, yili, narhi))
#     javob = input("Yangi avtomabil qo'shasizmi'ha/yoq'")
#     if javob=='yoq':
#         break
# print(f"Sizning avtomabilingiz {kompany} kompaniyasida ishlab chiqarilgan bo'lib,Modeli {model},Rangi {rangi},Karobkasi {korobka},Ishlab chiqarilgan yili esa {yili}-yil,Narhi esa {narhi} so'm ekan.Sizda juda ajoyib mashina bor ekan.")    

#Amaliyot

#1
# def malumotlar(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email_manzili ='',telefon =''):
#     malumot ={
#         'ismi' :ismi,
#         'familiya':familiyasi,
#         'tg_yil':tugilgan_yili,
#         'tg_joy':tugilgan_joyi,
#         'email':email_manzili,
#         'tel':telefon
# }
#     return malumot
# ism = input("Ismingizni kiriting:".title())
# fam = input("Familiyangizni kiriting:".title())
# tg_yili = input("tug'ilgan yilingizni kiriting:")
# tg_joy = input("Tug'ilgan  joyingizni kiriting:")
# gmail = input("Emailingizni kiriting(Hohlasangiz):")
# tel_n = input("Telefon nomeringizni kiriting(Hohlasangiz):")
# data = malumotlar(ism,fam,tg_yili,tg_joy,gmail,tel_n)
# print(data)

# MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)

#1
# def summa(*sonlar):
#         """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#         yigindi = 0
#         for son in sonlar:
#                 yigindi += son 
#         return yigindi
# print(summa(1,2,3,4,5,6,7,8,9))

#2
# def summa(*sonlar):
#     """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# print(summa(1,2,3,4,5,6))

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(1,2,3,87,9))

# def avto_info(kompoaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompoaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
# print(avto1,avto2)

# def son(*son_bering):
    # son=(1,2,3,4,5)
    # print(son(1,2,3)*2)

#Takrorlash
#1
# ism = "Shamshodbek"
# print(f"Mening ismim + {ism}")

#2
ism = "Shamshodbek"
familiya = "Tohirov"
ism_fam = f"{familiya} {ism}"
# print(ism_fam)

#3
# print(f"Salom mening ismim {ism}.{ism} {familiya}")

#4
# print("Hello world")
# print("Hello \tWorld")
# print("Hello \nWorld")
#5

# print(ism_fam.upper())
#6
