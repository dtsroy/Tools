from base64 import b64decode, b64encode
import tkinter as tk

class IsPass:
	def __init__(self):
		self.o = None
		self.win = tk.Tk()
		self.win.geometry('100x90')
		self.win.resizable(0, 0)
		tk.Label(self.win, text = 'Input Your Key:').pack()
		self.t1 = tk.Entry(self.win)
		self.t1.pack()
		tk.Button(self.win, text = 'Go!', command = self.cmd).pack()
		self.win.bind('<Control-s>', lambda e:self.cmd())
		self.win.bind('<Control-S>', lambda e:self.cmd())
		self.win.mainloop()

	def cmd(self):
		self.o = self.t1.get()
		self.win.quit()

	def IsPs(self):
		if self.o == 'z520' or self.o == 'a630':
			return True
		else:
			return False


class DEENCWin:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('300x300')
		#self.root.mainloop()
		self.root.resizable(0, 0)
		self.root.bind('<Control-q>', lambda e:self.root.quit())
		self.root.bind('<Control-Q>', lambda e:self.root.quit())
		self.root.bind('<Control-d>', lambda e:self.decode())
		self.root.bind('<Control-D>', lambda e:self.decode())
		self.root.bind('<Control-e>', lambda e:self.encode())
		self.root.bind('<Control-E>', lambda e:self.root.encode())
		tk.Label(self.root, text = 'Input').pack()
		FG = 'black'
		BG = 'green'
		self.t1 = tk.Text(self.root, bg = BG, fg = FG, height = 8)
		self.t1.pack()
		tk.Label(self.root, text = 'Output').pack()
		self.t2 = tk.Text(self.root, bg = BG, fg = FG, height = 8)
		self.t2.pack()
		tk.Button(self.root, text = 'Decode', command = self.decode).place(x = 0, y = 270)
		tk.Button(self.root, text = 'Encode', command = self.encode).place(x = 116, y = 270)
		tk.Button(self.root, text = 'Quit', command = self.root.quit).place(x = 260, y = 270)
		#self.root.mainloop()

	def decode(self, e=None):
		try:
			self.t2.delete(0.0, tk.END)
			self.t2.insert(tk.END, b64decode(self.t1.get(0.0, tk.END).encode('utf-8')).decode('utf-8'))
		except Exception as ex:
			with open('DecodeException.txt', 'w+') as f:
				f.write(str(ex))

	def encode(self, e=None):
		try:
			self.t2.delete(0.0, tk.END)
			self.t2.insert(tk.END, b64encode(self.t1.get(0.0, tk.END).encode('utf-8')).decode('utf-8'))
		except Exception as ex:
			#raise ex
			with open('EncodeException.txt', 'w+') as f:
				f.write(str(ex))

	def _main(self):
		self.root.mainloop()

def main():
	ip = IsPass().IsPs()
	if ip:
		DEENCWin()._main()
	else:
		print('WrongPwd')

if __name__ == '__main__':
	main()
