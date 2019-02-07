import urllib.request
import re

def main():
	url = "https://search.usa.gov/search?v%3Aproject=firstgov&query=pdf&affiliate=nws.noaa.gov"
	result = urllib.request.urlopen(url)
	filt = urllib.request.urlopen(url).read().decode("utf-8")
	search = re.findall(r'\"(.*?\.pdf)\"', filt)
	file = open("./pdfsearch.txt", "wt")
	i = 0
	for line in search:
		file.write(line + "\n")
		i += 1
	print("Fetched {} lines".format(i))



if __name__ == '__main__' : main()	 