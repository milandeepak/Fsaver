import requests
from bs4 import BeautifulSoup
from urllib.request import unquote
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
import schedule
import time

def flooddata():
    url= "https://mausam.imd.gov.in/imd_latest/contents/flash_flood.php"

    response = requests.get(url)

    content = BeautifulSoup(response.text, 'lxml')

    all_urls= content.find_all('a')

    pdf_urls=[]

    for url in all_urls:
        try:
         if 'pdf' in url['href']:
            if 'mausam' in url['href']:  
                a=url['href']
                print(a)
                pdf_urls.append(a) 
        except:
            pass    


    b, c= [pdf_urls[i] for i in (0,1)]

    url = b
    r = requests.get(url, stream=True)
    chunk_size=200
    with open('national.pdf', 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)


def get_pdf_file_content(path_to_pdf):
    
    
    
    resource_manager = PDFResourceManager(caching=True)
    
    
    out_text = StringIO()
    
    codec = 'utf-8'
    
 
    laParams = LAParams()
    
  
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(path_to_pdf, 'rb')
    
   
    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()

   
    fp.close()
    text_converter.close()
    out_text.close()
   
    return text

path_to_pdf = 'C:\\Users\\Milan\\Documents\\Webscraper\\national.pdf'  

all=get_pdf_file_content(path_to_pdf)

all1=all.split()


first=all1[244:252]
first1=' '.join(first)
print(first1)

file_object = open('sample.txt', 'a')
for i in first1:
    file_object.write(i)
file_object.close()   



# schedule.every(10).seconds.do(flooddata)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)

            










