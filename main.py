class Sick():
    def __init__(self,fullname,identiy):
        self.fullname = fullname
        self.__identiy = identiy
    def diagnosis(self,diagnosis):
        self.diagnosis = diagnosis
    def data(self):
        content = f"Hasta adi / soyadi : {self.fullname}\nHasta kimlik numarasi : {self.__identiy}\nHasta tanisi : {self.diagnosis}\n\n"
        return content

while True: 
    fullname = input("Hasta adini giriniz : ")
    identy = int(input("Hastanin kimlik numarasını giriniz : "))
    diagnosis = input("Hasta tanısını giriniz : ")

    sick = Sick(fullname, identy)
    sick.diagnosis(diagnosis)
    result = sick.data()

    with open("C:\\Users\\icerm\\Software\\Project\\PythonProject\\HospitalApp\\database.txt","a") as fileWrite:
        fileWrite.write(result)
    
    quit = int(input("İşlemi sonlandırmak için 0'a, devam etmek için 1'e basınız : "))
    if quit == 0:
        break
    elif quit == 1:
        continue