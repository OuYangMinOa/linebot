import pyqrcode,png
def make_Qrcode(msg):
    print(msg)
    url = pyqrcode.create(msg.strip(),error = 'L')
    url.png('code.png', scale=8)
if __name__ == "__main__":
    make_Qrcode("https://www.youtube.com/watch?v=auTe1lvqDkM")
    
