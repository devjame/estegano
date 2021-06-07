import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox as mg

from PIL import Image, ImageTk
import cv2

from estegano import encode, decode


# GUI
class App(tk.Tk):
	def __init__(self):
		super().__init__()

		# root window
		self.title('Esteganografia')
		self.resizable(False, False)
		self.geometry('580x310')
		self.style = ttk.Style(self)

		# initial variables
		self.image_display_size = 300, 300
		self.path_image = None
		self.image_file = None

		self.fr_img = ttk.Frame()
		self.fr_content = ttk.Frame()
		self.fr_placeholder = ttk.Frame()
		self.fr_decode = ttk.Frame()
		self.fr_option = ttk.Frame()

		self.selected_value = tk.IntVar()

		self.rb_value1 = ttk.Radiobutton(
			self.fr_option,
			text='Codificar',
			value=0,
			variable=self.selected_value,
			command=self.change_frame)

		self.rb_value2 = ttk.Radiobutton(
			self.fr_option,
			text='Descodificar',
			value=1,
			variable=self.selected_value,
			command=self.change_frame)

		self.btn_file = ttk.Button(text="Escolher Imagem", command=self.load_file)
		self.lbl_img = ttk.Label(self.fr_img)

		self.txt_mensagem = tk.Text(self.fr_content, height=10, width=25)
		self.btn_encode = ttk.Button(self.fr_content, text="Codificar", command=self.codificar)

		self.lbl_text = ttk.Label(self.fr_placeholder, text="Escolha uma imagem.", background="cyan", width=30)

		self.btn_decode = ttk.Button(self.fr_content, text="Descodificar", command=self.descodificar)

		self.lbl_img.pack()
		self.btn_file.pack(pady=5, padx=5)

		# encode
		self.txt_mensagem.pack()
		self.btn_encode.pack(pady=6)
		self.btn_decode.pack(pady=6)

		self.lbl_text.pack(anchor="center", fill=tk.Y, ipady=5)

		# options
		self.rb_value1.pack(side="left", padx=5)
		self.rb_value2.pack(side="left", padx=5)

		# pack frames
		self.fr_img.pack(side="left", padx=5, pady=8, fill=tk.BOTH)
		self.fr_placeholder.pack(side="left", padx=5, pady=8, fill=tk.BOTH)
		self.fr_option.pack(side="bottom", fill=tk.X, pady=5)
		self.fr_content.pack(side="right", padx=5, pady=8, fill=tk.BOTH)
		self.fr_decode.pack(side="right", padx=5, pady=8, fill=tk.BOTH)

		self.change_frame()

	def codificar(self):
		# file type
		filetypes = (
			('Jpg files', '*.jpg'),
			('Png files', '*.png'),
			('All files', '*.*')
		)

		mensagem = self.txt_mensagem.get("1.0", "end")
		print(mensagem)
		if mensagem == " " or mensagem == "\n":
			mg.showinfo(title="Erro", message="Escrever uma mensagem.")
		imagem = self.path_image
		if not imagem:
			mg.showinfo(title="Erro", message="Escolha uma imagem!")
		else:
			# show the open file dialog
			print(mensagem)
			encoded_imagem = encode(imagem, mensagem)
			output_imagem = fd.asksaveasfilename(filetypes=filetypes)
			cv2.imwrite(output_imagem, encoded_imagem)
			self.txt_mensagem.delete('1.0', tk.END)
			mg.showinfo(title="Info", message="Mensagem Codificada com Sucesso!")

	def descodificar(self):
		# file type
		filetypes = (
			('Jpg files', '*.jpg'),
			('Png files', '*.png'),
			('All files', '*.*')
		)
		imagem = self.path_image
		if not imagem:
			mg.showinfo(title="Erro", message="Escolha uma imagem!")
		else:
			# show the open file dialog
			decoded_mensagem = decode(imagem)
			self.txt_mensagem["state"] = 'normal'
			self.txt_mensagem.delete('1.0', tk.END)
			self.txt_mensagem.insert('1.0', decoded_mensagem)
			print(decoded_mensagem.encode())
			self.txt_mensagem["state"] = 'disabled'

	def change_frame(self):
		self.txt_mensagem.delete('1.0', tk.END)
		if self.selected_value.get() == 0:
			self.btn_decode.pack_forget()
			self.btn_encode.pack_configure(pady=6)
			self.txt_mensagem["state"] = 'normal'
		else:
			self.btn_encode.pack_forget()
			self.btn_decode.pack_configure(pady=6)
			self.txt_mensagem["state"] = 'disabled'

	def load_file(self):
		self.path_image = fd.askopenfilename()

		if self.path_image:
			try:
				pil_img = Image.open(self.path_image)
				pil_img.thumbnail(self.image_display_size, Image.ANTIALIAS)
				self.image_file = ImageTk.PhotoImage(pil_img)
				print(self.image_file)
				self.lbl_img.config(image=self.image_file)
				self.fr_placeholder.pack_forget()
			except Exception as e:
				mg.showerror(title="Erro", mensagem="Ficheiro nã aberto! Tente novamente.")
				print(e)
				return


def main():
	app = App()
	app.mainloop()


if __name__ == "__main__":
	main()
