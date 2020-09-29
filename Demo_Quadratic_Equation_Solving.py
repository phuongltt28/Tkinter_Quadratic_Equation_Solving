# Lê Thị Trúc Phương - 43.01.104.137
# Chương trình giải phương trình bậc 2

#import thư viện Tkinter
from tkinter import *
import tkinter.font as font

# import thư viện Math
from math import sqrt

# Function giải pt bậc 2
def quadratic_equation(A, B, C):
	# Xóa dữ liệu cũ
	resField.delete(0, END)

	# Thêm dữ liệu vào listbox vào vị trí cuối của listbox
	resField.insert(END, "Equation: " + A + "x^2 + " + B + "x + " + C + " = 0")
	resField.insert(END, "Result: ")
	
	try:

		# Cast kiểu dữ liệu về kiểu số nguyên
		A = int(A)
		B = int(B)
		C = int(C)

		# Nếu số A = 0 => Pt: Bx + C = 0
		if (A == 0):
			if (B == 0):
				if (C == 0): 
					resField.insert(END, "This equation has no real solution")
					
				else:
					resField.insert(END, "No solution")
			else:
				res = eval("-C/B")
				resField.insert(END, "This equation has one solution: x = " + str(res))
		else:
			delta= B ** 2 - (4 * A * C)
			resField.insert(END, "Delta = " + str(delta))

			x1 = (- B + sqrt(delta)) / (2 * A)
			x2 = (- B - sqrt(delta)) / (2 * A)

			if (delta < 0):
				resField.insert(END, "No solution")
			elif delta == 0:
				res = eval("-B/2*A")
				resField.insert(END, "This equation has one solution: ")
				resField.insert(END, "x = " + str(res))
				
			else:
				resField.insert(END, "This equation has two solution: ")
				resField.insert(END, "x1 = " + str(x1))
				resField.insert(END, "x2 = " + str(x2))

	except:
		resField.insert(END, "ERROR")

# Function clear listbox và các entry
def refreshAll():
	resField.delete(0, END)
	entry1.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)

#Tk() để tạo cửa sổ chính
window = Tk()

# Bỏ nút phóng to/thu nhỏ giao diện
window.resizable(0,0)

#Thay đổi title app
window.title("Quadratic Equation Solving")

#Đặt kích thước mặc định cho app
window.geometry("400x450")

#tạo object font mặc định
fontStyle = font.Font(family = "Time New Romans", size = 15)

label = Label(window, text="Quadratic equation: Ax^2 + Bx + C = 0", fg = "#b33939")

# Cài đặt font cho label
label.config(font = fontStyle)

# Thêm label vào giao diện
label.place(x = 22, y = 3)

# Tạo listbox hiển thị kết quả
resField = Listbox(window, height = 7, width = 32 , font = fontStyle)

#Thêm listbox vào giao diện
resField.place(x = 22, y = 40)

# Tạo label nhập số A
label1 = Label(window, text = "Enter A:")
# Cài đặt font cho label
label1.config(font = fontStyle)

# Thêm label vào giao diện
label1.place(x = 30, y = 240)


# Tạo field nhập vào số A
entry1 = Entry(window, width = 19, font = fontStyle)

# Thêm vào giao diện
entry1.place(x = 160, y = 245)

# Tạo label nhập số B
label2 = Label(window, text = "Enter B:")

# Cài đặt font cho label
label2.config(font = fontStyle)

# Thêm label vào giao diện
label2.place(x = 30, y = 280)

# Tạo field nhập vào số B
entry2 = Entry(window, width = 19, font = fontStyle)

# Thêm vào giao diện
entry2.place(x = 160, y = 285)


# Tạo label nhập số C
label3 = Label(window, text = "Enter C:")

# Cài đặt font cho label
label3.config(font = fontStyle)

# Thêm label vào giao diện
label3.place(x = 30, y = 330)

# Tạo field nhập vào số C
entry3 = Entry(window, width = 19, font = fontStyle)

# Thêm vào giao diện
entry3.place(x = 160, y = 335)


# Tạo button tính
submitBtn = Button(window, 
	command = lambda: quadratic_equation(entry1.get(), entry2.get(), entry3.get()), 
	text = "Submit", 
	bg = "#55efc4", 
	fg = "#eb2f06",
	height = 1,
	width = 6,
	cursor = "hand2"
)

# Thay đổi font chữ cho button
submitBtn['font'] = fontStyle

# Thêm button vào giao diện
submitBtn.place(x = 90, y = 390)

# Tạo button refresh
refreshBtn = Button(window, 
	command = lambda: refreshAll(), 
	text = "Refresh", 
	bg = "#55efc4", 
	fg = "#eb2f06",
	height = 1,
	width = 6,
	cursor = "hand2"
)

# Thay đổi font chữ cho button
refreshBtn['font'] = fontStyle

# Thêm button vào giao diện
refreshBtn.place(x = 250, y = 390)

#chạy giao diện cho đến khi người dùng đóng lại
window.mainloop()
