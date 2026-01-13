data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
"""
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
"""
data = 'menggunakan singel quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at?'")

#2. menggunakan tanda \ (backslash)

#membuat tanda ' menjadi string
print('mari shalat jum\'at ')
print("g\day,isn\'t it")

#backslash
print("C:\\user\\ucup")

#tab
print("ucup\t\t\totong,semakin jauhan")

#backspace
print("ucup\botong,jadi dekatan")

#newline
print("baris pertama\nbaris kedua") #LF -> line feed -> UNIX, Linux, MacOS
print("baris pertama\rbaris kedua") #CR -> carriage return -> COMMODORE,accorn,lisp
print("baris pertama\baris kedua") #CRLF -> carriage return line feed -> WINDOWS

# 3,string lieteral (raw string)

print('c:\new folder') # akan salah path nya

#menggunakan raw string
print(r'c:\new folder')

#multiline literal string
print(""")
nama = ucup
kelas = 3 sd
""")

#multiline literal string dan raw
print(r"""
      nama : ucup
      kelas : 3 SD\new normal
      website : www.ucup.com\newid
      """)

