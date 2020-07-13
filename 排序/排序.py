def find(names, content, outp):
	names=open(names, 'r')
	n_ = names.readlines()
	#print(n_)
	n2_ = [s.replace('\n', '') for s in n_]
	#print(n2_)
	names = n2_
	nums = [m.replace('\n', '') for m in open(content, 'r').readlines()]

	li = []
	for m in nums:
		if nums.index(m) % 4 == 0:
			pass
		else:
			li.append(m)
			
	print(li)

	lll=[]
	for m in li:
		if m[0] == '/':
			lll.append([li[li.index(m) - 2], li[li.index(m) - 1].replace('分', ''), m.replace('/', '')])
			
	print(lll)

	llll = []
	
	print(names)
	for m in lll:
		if m[0] in names:
			llll.append(m)
			
	#llll.pop(6)
	print(llll)
	import xlwt
	wbk = xlwt.Workbook()

	sheet = wbk.add_sheet('ss', cell_overwrite_ok=True)
	#sheet.write(0,1,'test text')#第0行第一列写入内容
	for n in llll:
		sheet.write(llll.index(n) + 1, 0, n[0])
		sheet.write(llll.index(n) + 1, 1, n[1])
		sheet.write(llll.index(n) + 1, 2, n[2])
	wbk.save(outp)
	
if __name__ == '__main__':
	find('10ban.txt', 'num.txt', '10.xls')