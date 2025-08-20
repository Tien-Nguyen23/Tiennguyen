#1. Write a Python program to calculate the length of a string.
x='hello'
length=len(x)
print("độ dài chuỗi:",length)

#2. Write a Python program to count the number of characters (character frequency) in a string.
y='google.com'
def dem_tung_ky_tu(chuoi_can_nhap):
    ket_qua ={}
    for ky_tu in chuoi_can_nhap:
        if ky_tu in ket_qua:
         ket_qua[ky_tu] = ket_qua[ky_tu] +1
        else:
         ket_qua[ky_tu] = 1
    return ket_qua
print(f"Expected Result:{dem_tung_ky_tu(y)}")

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
z='w3resource'
if len(z)>=2:
    Result =z[:2] + z[-2:]
else :
    Result =""
print(f"Ket qua: {Result}")

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
t= 'restart'
def change_string(s):
     return s[0] + s[1:].replace(s[0], "$")
t=change_string(t)
print("Result:", t)
#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1, str2='abc', 'xyz'
def mix_up(a, b):
    new_a= b[:2]+a[2:]
    new_b= a[:2]+b[2:]
    return new_a +' '+new_b
print(mix_up(str1,str2))
#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
word='abc'
def add(s):
    if len(s)>=3 and word.endswith("ing"):
        return s+'ly'
    elif len(s)>=3:
        return s+'ing'
    else:
        return s
print("Expected Result:", add(word))
#7. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
word_list ='Exercises','apple','banana'
def longest(words):
    longest_word = max (words, key=len)
    return longest_word, len(longest_word)
word,length =longest(word_list)
print("Longest word:", word)
print("Length of the longest word:", length)
#8 Write a Python program to remove the nth index character from a nonempty string.
word='laptrinh'
def remove(a,index):
    return a[:index]+ a[index+1:]
n=2
result= remove(word,n)
print("Original string:", word)
print("After removing character at index", n, ":", result)
#9. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
string='Camtien'
def change(voc):
    return voc[-1:]+voc[1:-1]+voc[:1]
print(change(string))
#10 Write a Python program to remove characters that have odd index values in a given string.
c='xinchao'
def remove_odd(f):
    return f[::2]
print(f"chuỗi ban đầu: {c}")
print(f"chuỗi sau khi bỏ ký tự lẻ: {remove_odd(c)}")
#11  Write a Python program to count the occurrences of each word in a given sentence.
w = 'xin chao ban'
def count_words (g):
    counts = dict()
    voc1 = g.split()
    for k in voc1 :
        if k in counts:
            counts[k]=counts[k]+1
        else:
            counts[k]=1
    return counts
result = count_words(w)
print("Số lần xuất hiện của từng từ:",result )
for word, count in result.items():
    print(word, ":", count)
#12 Write a Python script that takes input from the user and displays that input back in upper and lower cases.
chuoi='camon'
print("Chữ in hoa:",chuoi.upper())
print("Chữ in thường:",chuoi.lower())
#13 Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
r='red, white, black, red, green, black'
p=[word for word in r.split(",")]
print(",".join(sorted(list(set(p)))))
#14 Write a Python function to create an HTML string with tags around the word(s).
ham='Python Tutorial'
def html(tag,text):
    return f"<{tag}>{text}</{tag}>"
print(html("b",ham))
print (html("i", ham))
#15 Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
bien='Python'
def insert(tu_cuoi):
   gia_tri_moi=tu_cuoi[-2:]
   return gia_tri_moi *4
print("ket qua lap lai cua 2 tu cuoi:",insert(bien))
#16 Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
gia_tri=' python'
def keep(k):
    k=k.strip( )
    if len(k)>=3:
        return k[:3]
    else:
        return k
print(keep(gia_tri))
#17 Write a Python function to reverse a string if its length is a multiple of 4.
h='laptrinh'
if len(h)%4==0:
    print( h[::-1])
else:
    print(h)
#18 # Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
l= 'XinChao'
def upper(s):
    num_upper=0
    for letter in s[:4]:
        if letter.upper()== letter :
            num_upper=num_upper+1
    if num_upper>=2:
        return s.upper()
    else:
        return s
print(upper(l))
#19 Write a Python program to sort a string lexicographically.
d='python'
def sort(s):
    return sorted(sorted(s), key=str.upper)
print(sort(d))
#20 Write a Python program to remove a newline in Python.
v='python Exercises\n'
print(v)
print(v.rstrip())
#21 Write a Python program to check whether a string starts with specified characters.
q='python'
print(q.startswith('py'))
#22 Write a Python program to display formatted text (width=50) as output.
import textwrap
sample_text='Python is a powerful programming language that is easy to learn and widely used. Its design philosophy emphasizes code readability'
print(textwrap.fill(sample_text, width=50))
#23 Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap
r = """
        Python is a widely used programming language.
        It is easy to learn and powerful.
        Many developers enjoy using Python for projects.
        """
clean_text = textwrap.dedent(r)
print("Original text:", r)
print("After removing indentation:", clean_text)
#24 Write a Python program to add prefix text to all of the lines in a string.
import textwrap
m=""" Python easy to learn.
 Hello python.
 Thankyou."""
text_without= textwrap.dedent(m)
print("Original text:")
print(m)
print("Text after removing indentation:")
print(text_without)
#25Write a Python program to set the indentation of the first line.
m=""" Python easy to learn.
Hello python.
Thankyou."""
indent=" "
lines = m.splitlines() #tách
lines[0]= "\n"+indent+ lines[0] #thụt lề dòng đầu
new="\n".join(lines) #nối lại thành
print("ket qua nhan duoc:",new)
#26 Write a Python program to print the following numbers up to 2 decimal places.
number=2.8230601
print("ket qua: {:.2f}".format(number))
#27 Write a Python program to print the following numbers up to 2 decimal places with a sign.
num_1=2.32801
num_2=-1.3455
print("ket qua nhan duoc: {:+.2f}".format(num_1))
print("ket qua nhan duoc: {:+.2f}".format(num_2))
#28 Write a Python program to print the following positive and negative numbers with no decimal places.
num_1=2.32801
num_2=-1.3455
print("ket qua: {:+.0f}".format(num_1))
print("ket qua: {:+.0f}".format(num_2))
#29 Write a Python program to print the following integers with zeros to the left of the specified width.
num1=2
num2=3
print("gia tri sau thay doi: {:0>2d}".format(num1))
print("gia tri sau thay doi: {:0>3d}".format(num2))
#30 Write a Python program to print the following integers with '*' to the right of the specified width.
num1=2
num2=3
print("gia tri nhan duoc: {:*<3d}".format(num1))
print("gia tri nhan duoc: {:*<4d}".format(num2))
#31Write a Python program to display a number with a comma separator.
number1=651633929
number2=67653547.23
print("ta duoc: {:,}".format(number1))
print("ta duoc: {:,}".format(number2))
#32 Write a Python program to format a number with a percentage.
num1=0.065
num2=0.34
print("nhan duoc: {:.2%}".format(num1))
print("nhan duoc: {:.1%}".format(num2))
#33 Write a Python program to display a number in left, right, and center aligned with a width of 10.
so=283
print("can trai: {:<10d}".format(so))
print("can giua: {:^10d}".format(so))
print("can phai: {:>10d}".format(so))
#34 Write a Python program to count occurrences of a substring in a string.
du_lieu='Hello python. python is easy to learn'
print("so lan python xuất hiện là:",du_lieu.count("python"))
#35 Write a Python program to reverse a string.
chuoi= 'hello python'
print("chuoi sau khi dao nguoc:", chuoi[::-1])
#36 Write a Python program to reverse words in a string.
nhap_chuoi= 'hello python'
print(" chuoi sau thay doi:", " ".join(nhap_chuoi.split()[::-1]))
#37 Write a Python program to count repeated characters in a string.
from collections import Counter
v='thequickbrownfoxjumpsoverthelazydog'
print("ket qua lap lai tung ki tu:")
dem=Counter(v)
for char,count in dem.items():
    if count>1:
      print(f"{char}:{count}")
#38 Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
import math
c_dai = 4
c_rong = 3
r = 2
c_cao = 5
print(f"dien tich HCN= {c_dai*c_rong} cm^2")
print(f"the tich hinh tru= {math.pi*(r*r)*c_cao} cm^3")
#39 Write a Python program to print the index of a character in a string.
w= 'w3resource'
for index, char in enumerate(w):
    print(f" Current character {char} position at {index}")
#40 Write a Python program to convert a given string into a list of words.
u='The quick brown fox jumps over the lazy dog.'
print(u.split(' '))
#41 Write a Python program to lowercase the first n characters in a string.
e='pythonhomework'
print(e[:6].upper()+e[6:])
#42 Write a Python program to swap commas and dots in a string.
so= '234,555.56'
t=so.maketrans
print(so.translate(t(',.','.,')))
#43 Write a Python program to split a string on the last occurrence of the delimiter.
y= 'p,y,t,h,o,n'
print(y.rsplit(',',2))
#44 Write a Python program to find the first non-repeating character in a given string.
text='hellopytho'
def first(s):
    char_order = []  # danh sách lưu thứ tự ký tự gặp lần đầu
    ctr = {}  # từ điển đếm số lần xuất hiện của từng ký tự
    for c in s :
        if c in ctr :
            ctr[c]=ctr[c]+1
        else:
            ctr[c]=1
            char_order.append(c)  # đồng thời lưu vào danh sách thứ tự
    for c in char_order: # tìm kí tự không lập
        if ctr[c] == 1:
            return c
    return none
print("kí tự không lập  đầu tiên:",first(text))
#45 Write a Python program to find the first repeated character in a given string.
text='hellopytho'
def first(s):
    char_order = []  # danh sách lưu thứ tự ký tự gặp lần đầu
    ctr = {}  # từ điển đếm số lần xuất hiện của từng ký tự
    for c in s :
        if c in ctr :
            ctr[c]=ctr[c]+1
        else:
            ctr[c]=1
            char_order.append(c)  # đồng thời lưu vào danh sách thứ tự
    for c in char_order: # tìm kí tự không lập
        if ctr[c] > 1:
            return c
    return
print("kí tự lập  đầu tiên:",first(text))
#46 Write a Python program to remove spaces from a given string.
text= 'hello python'
no_space= text.replace(' ','')
print(no_space)
#47 Write a Python program to capitalize the first and last letters of each word in a given string.
text='hello python'
def first_last(str1):
    str1= str1.title()
    result=""
    for word in str1.split():
         result += word[:-1] + word[-1].upper() + " "
    return result[:-1]
print(first_last(text))
#48 Write a Python program to compute the sum of the digits in a given string.
text='12python675'
def sum(s):
    total=0
    for c in s :
        if c.isdigit():  # kiểm tra nếu c là chữ số
            total=total+int(c) # cộng vào tổng
    return total
print("tổng của các số =",sum(text))
#49 Write a Python program to remove leading zeros from an IP address.
so='123.010.012'
def remove(ip):
    parts =ip.split('.')  # tách IP thành các phần theo dấu chấm
    new_parts=[] # Loại bỏ số 0 đầu và chuyển về chuỗi
    for part in parts:
        number = int(part)  # chuyển sang số, tự động loại bỏ số 0 đầu
        new_parts.append(str(number))  # chuyển lại thành chuỗi và thêm vào list mới
    return ".".join(new_parts)
print("kết quả sau khi loại bỏ:",remove(so))
#50 Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".
str1='hello'
str2='pythone'
def common_ter(str1,str2):
    common = set(str1) & set(str2) # Chuyển cả hai chuỗi thành set để loại bỏ trùng lặp và tìm giao của 2 set
    if common:
        result = ''.join(sorted(common))      # Sắp xếp theo thứ tự chữ cái
        return result
    else:
        return "No common characters"
print("giá trị chung và sau khi sắp xếp là:" ,common_ter(str1,str2))