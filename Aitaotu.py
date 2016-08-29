#coding:utf-8
from __future__ import print_function
from multiprocessing import Pool
import multiprocessing
from bs4 import BeautifulSoup
import os, time, random, urllib
import socket
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getHtmlSoup(url):
	page = urllib.urlopen(url)
	html = page.read()
	Soup = BeautifulSoup(html, 'lxml')
	# print(Soup)
	return Soup

global ThemeInfo
ThemeInfo = [{'Href': 'http://www.aitaotu.com//tag/aiss.html', 'Number': 1, 'Title': u'AISS\u7231\u4e1d\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/tuinvlang.html', 'Number': 2, 'Title': u'\u63a8\u5973\u90ce\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/youguowang.html', 'Number': 3, 'Title': u'\u5c24\u679c\u7f51\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/tuinvshen.html', 'Number': 4, 'Title': u'\u63a8\u5973\u795e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/rosi.html', 'Number': 5, 'Title': u'ROSI\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/xiurenwang.html', 'Number': 6, 'Title': u'\u79c0\u4eba\u7f51\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/meiyuanguan.html', 'Number': 7, 'Title': u'\u7f8e\u5a9b\u9986\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/pansidong.html', 'Number': 8, 'Title': u'PANS\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/ligui.html', 'Number': 9, 'Title': u'\u4e3d\u67dc\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/3agirl.html', 'Number': 10, 'Title': u'3agirl\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/ddy.html', 'Number': 11, 'Title': u'DDY Pantyhose\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/meiyanshe.html', 'Number': 12, 'Title': u'\u9b45\u598d\u793e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/vnvlang.html', 'Number': 13, 'Title': u'\u4e1c\u839eV\u5973\u90ce\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/ruyixiezhen.html', 'Number': 14, 'Title': u'RU1MM\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/beautyleg.html', 'Number': 15, 'Title': u'beautyleg\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/disi.html', 'Number': 16, 'Title': u'DISI\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/sijianwu.html', 'Number': 17, 'Title': u'\u4e1d\u95f4\u821e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/dongganzhixing.html', 'Number': 18, 'Title': u'\u52a8\u611f\u4e4b\u661f\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/HeiSiAi.html', 'Number': 19, 'Title': u'HeiSiAi\u5199\u771f\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/jiamiannvhuang.html', 'Number': 20, 'Title': u'\u5047\u9762\u5973\u7687\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/boluoshe.html', 'Number': 21, 'Title': u'\u6ce2\u841d\u793e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/aimishe.html', 'Number': 22, 'Title': u'\u7231\u871c\u793e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/Leghacker.html', 'Number': 23, 'Title': u'Leghacker\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/sibao.html', 'Number': 24, 'Title': u'\u4e1d\u5b9d\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/chizuzhe.html', 'Number': 25, 'Title': u'\u8d64\u8db3\u8005\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/paimei.html', 'Number': 26, 'Title': u'\u62cd\u7f8eVIP\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/aixiu.html', 'Number': 27, 'Title': u'ISHOW\u7231\u79c0\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/simeivip.html', 'Number': 28, 'Title': u'\u4e1d\u9b45VIP\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/MFStar.html', 'Number': 29, 'Title': u'MFStar\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/ttns.html', 'Number': 30, 'Title': u'\u5934\u6761\u5973\u795e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/xixiwang.html', 'Number': 31, 'Title': u'\u897f\u897f\u4eba\u4f53\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/yannvshen.html', 'Number': 32, 'Title': u'\u989c\u5973\u795e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/shanghaixuancai.html', 'Number': 33, 'Title': u'\u4e0a\u6d77\u70ab\u5f69\u6444\u5f71\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/youxingguan.html', 'Number': 34, 'Title': u'\u4f18\u661f\u9986\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/niceleg.html', 'Number': 35, 'Title': u'NICE-LEG\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/Tyingart.html', 'Number': 36, 'Title': u'Tyingart\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/feilin.html', 'Number': 37, 'Title': u'FEILIN\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/mitaoshe.html', 'Number': 38, 'Title': u'\u871c\u6843\u793e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/meixiu.html', 'Number': 39, 'Title': u'\u7f8e\u79c0\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/tangsi.html', 'Number': 40, 'Title': u'\u7cd6\u4e1dTangs\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/tianshisheying.html', 'Number': 41, 'Title': u'\u5929\u4f7f\u651d\u5f71\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/51modozazhi.html', 'Number': 42, 'Title': u'51MODO\u6742\u5fd7\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/tangyun.html', 'Number': 43, 'Title': u'\u5510\u97f5\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/damingmowang.html', 'Number': 44, 'Title': u'\u5927\u540d\u6a21\u7f51\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/youwuguan.html', 'Number': 45, 'Title': u'\u5c24\u7269\u9986\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/zhongguotuimo.html', 'Number': 46, 'Title': u'\u4e2d\u56fd\u817f\u6a21\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/xiweisha.html', 'Number': 47, 'Title': u'\u5e0c\u5a01\u793e\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/feituwang.html', 'Number': 48, 'Title': u'\u98de\u56fe\u7f51\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/taste.html', 'Number': 49, 'Title': u'TASTE\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/moki.html', 'Number': 50, 'Title': u'MoKi\u7b71\u5624\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/meituibaobei.html', 'Number': 51, 'Title': u'\u7f8e\u817f\u5b9d\u8d1d\u5957\u56fe'}, {'Href': 'http://www.aitaotu.com//tag/yingsihui.html', 'Number': 52, 'Title': u'\u5f71\u79c1\u835f\u5957\u56fe'}]

def getAllThemepage(url):
	Soup = getHtmlSoup(url)
	pagelist = [url]

	nexttags = Soup.select('#pageNum > span > a')
	if nexttags:
		postfix = nexttags[-1].get('href')
		reg_num = r'/tag/.*/(.*)\.html'
		Lastpagenumber = int(re.findall(reg_num, postfix)[0])

		for i in range(2,Lastpagenumber + 1):
			pageurl = url[:-5] + '/' + str(i) + '.html'
			pagelist.append(pageurl)

	# print(pagelist)
	return pagelist

def getCurrentPageTaotuurl(url, pagenumber):
	TaotuList = []

	Soup = getHtmlSoup(url)
	taotutags = Soup.select('#mainbodypul > li > p > a')

	count = 0 + pagenumber * 20
	for title, href in zip(taotutags, taotutags):
		count += 1
		data = {
			'Number': count,
			'Title': title.get('title'),
			'Href': 'http://www.aitaotu.com/' + href.get('href')
		}
		TaotuList.append(data)
		print(data['Number'], data['Title'], data['Href'])

	return TaotuList

def getAllpageTaotuUrl(url):
	Pageurllist = getAllThemepage(url)
	pagenumber = 0
	TaoTuList = []
	for pageurl in Pageurllist:
		TaoTuList += getCurrentPageTaotuurl(pageurl,pagenumber)
		pagenumber += 1
	print("一共有 %s 套图" % len(TaoTuList))
	return TaoTuList

# 开始下载每页的图片
def getEachPageOriginalImageURL(url):
	Soup = getHtmlSoup(url)
	imageinfo = []
	imagetags = Soup.select('#big-pic > p > a > img')
	# print(imagetags)
	for src,filename in zip(imagetags,imagetags):
		data = {
		'src': src.get('src'),
		'filename': filename.get('alt')
		}
		# print(data)
		imageinfo.append(data)

	return imageinfo

# 找到当前套图所有页面
def getTaotuAllpage(url):
	Soup = getHtmlSoup(url)
	pagelist = [url]

	nexttags = Soup.select('body > div > div.photo > div.pages > ul > li > a')
	if nexttags:
		postfix = nexttags[-1].get('href')
		reg_num = r'/.*/.*_(.*)\.html'
		Lastpagenumber = int(re.findall(reg_num, postfix)[0])

		for i in range(2,Lastpagenumber + 1):
			pageurl = url[:-5] + '_' + str(i) + '.html'
			pagelist.append(pageurl)

	# print(pagelist)
	return pagelist

# def getAllImageURL(url):
# 	imagepageurllist = getTaotuAllpage(url)
# 	AllImageInfo = []
#
# 	for pageurl in imagepageurllist:
# 		AllImageInfo += getEachPageOriginalImageURL(pageurl)
#
# 	return AllImageInfo


def getFoldername(url):
	Soup = getHtmlSoup(url)
	foldernametag = Soup.select('#photos > h1')
	foldernames = foldernametag[0].get_text()
	reg_name = r'(.*)\(+?'
	foldername = re.findall(reg_name, foldernames)[0]
	# print(foldername)
	return foldername

def DownloadImage(url, foldername, PageNumber):
	ImageInfolist = getEachPageOriginalImageURL(url)
	photocount = 0

	for info in ImageInfolist:
		src = info['src']
		filename = info['filename']
		# print(src,filename)
		path = 'Aitaotu/%s/' % foldername

		if not os.path.exists(path):
			os.makedirs(path)

		target = path + '%s.jpg' % filename
		print("正在下载图片%s" % filename)

		socket.setdefaulttimeout(5.0)

		try:
			urllib.urlretrieve(src, target)
		except urllib.ContentTooShortError:
			print("Network error. Relaoding...")
			# socket.setdefaulttimeout(5.0)
			urllib.urlretrieve(src, target)

		photocount +=1

	# print("--------------------------------------------------\n"
	# 		  "第%s页下载完成,进程ID:%s\n"
	# 		  "--------------------------------------------------\n"
	# 	  % (PageNumber + 1, os.getpid()))

	countQueue.put(photocount)


def DownloadCurrentTaotu(url):

	print("--------------------------------------------------\n"
			"正在读取相册片信息...")
	Foldername = getFoldername(url)
	Pageurllist = getTaotuAllpage(url)
	Pagenumber = len(Pageurllist)

	count = 0
	global countQueue
	manager = multiprocessing.Manager()
	countQueue = manager.Queue()

	downloadphoto = multiProcess(DownloadImage, Pageurllist ,Pagenumber )
	downloadphoto.downloadworks(Foldername)


	# 从查找页面的所有进程中通过进程通信queue获得每一页的图片
	for i in range(Pagenumber):
		count += countQueue.get(True)

	print("这个相册有 %s 张图片" % count)


class multiProcess(multiprocessing.Process):
	"""docstring for multiProcess"""
	def __init__(self, func, arg, worknum):
		super(multiProcess, self).__init__()
		self.func = func
		self.arg = arg
		self.worknum = worknum

	def downloadworks(self, foldername):
		p = multiprocessing.Pool(self.worknum)
		for i in range(self.worknum):
			page_url = self.arg[i]
			p.apply_async( self.func, args = (page_url,foldername,(i + 1),))

		p.close()
		p.join()

def DownloadAllThemetaotu(url):
	PageURList = getAllpageTaotuUrl(url)
	number = int(raw_input("请输入从那个主题开始下载："))
	for data in PageURList:
		if data['Number'] >= number:
			print("正在下载套图 %s%s" % (data['Number'],data['Title']))
			DownloadCurrentTaotu(data['Href'])

def chooseNumber():
	global URL
	URL = 'http://www.aitaotu.com'

	print("0 直接粘贴指定的套图URL")
	for data in ThemeInfo:
		print(data['Number'], data['Title'], data['Href'])

	choice = -1
	while not (choice in range(0,53)):
		choice = int(raw_input("请输入对应的数字:"))

	if choice == 0:
		pageurl = 'Y'
		while not pageurl == 'N':
			pageurl = raw_input("请在此粘贴URL(如果要退出请输入'N'并回车):")
			if not pageurl == 'N':
				DownloadCurrentTaotu(pageurl)
	else:
		data = ThemeInfo[choice - 1]
		print(data['Number'], data['Title'], data['Href'])
		DownloadAllThemetaotu(data['Href'])

if __name__ == '__main__':

	t0 = time.time()
	print('''
		---------------------------------
		      欢迎使用相册批量下载器
		---------------------------------
		Author:  Sparrow
  		Created: 2016-8.21
  		Email: sparrow629@163.com
	''')

	chose_quit = 'Y'
	while not chose_quit == 'N':
		chooseNumber()
		print(time.time()-t0)
		chose_quit = raw_input('\n继续选择下载请按键[Y],退出请按键[N]:')



	


