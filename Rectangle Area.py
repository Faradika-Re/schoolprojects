# Make de function of rectangle area calc
def rectangle():
    length = input("Enter the length of the rectangle : ")
    width = input("Enter the width of the rectangle : ")
    area = float(length) * float(width);
    # Perlu diberi int type dalam menginisialisasi var length ataupun width
    # ke dalam var area. Hal ini dimaksudkan agar value dari kedua var yang dimasukkan 
    # ke dalam operation of rectangle area bakal sesuai dengan apa yang kita mau
    # kalo mau float tinggal diganti float
    # kalo mau int tinggal diganti
    print(f"The area of the rectangle is : {area} cm\u00B2");
    # \u**** ialah superscript
    # superscript memungkinkan kita untuk memasukkan simbol ke dalam string yang kita inginkan
    # output dari superscript ini disebut unicode atau teks khusus
rectangle()