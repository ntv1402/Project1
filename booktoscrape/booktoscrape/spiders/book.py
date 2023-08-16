import scrapy
import re

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/index.html"]

    def parse(self, response):
        # Tách lấy url của từng sách và truy cập vào url đó
        for book_url in response.xpath("//article/div[1]/a/@href").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        
        # Sau khi crawl hết 1 trang thì sang trang tiếp theo
        base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        for i in range(1, 50+1):
            url = base_url.format(i)
            yield scrapy.Request(url, callback=self.parse)
        # next_page = response.xpath("//a/@href").get()
        # if next_page:
        #     yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
    
    def parse_book_page(self, response):
        # book_title = response.xpath("//h1/text()").get()
        # book_category = response.xpath("//li[3]/a/text()").get()
        # book_price_notax = response.xpath("//tr[3]/td/text()").get().replace('£','')
        # book_price_tax = response.xpath("//tr[4]/td/text()").get().replace('£','')
        # book_tax = response.xpath("//tr[5]/td/text()").get().replace('£','')
        # book_rating = response.xpath("//div[2]/p[3]/@class").get().replace('star-rating ','')
        # book_status = response.xpath("//tr[6]/td/text()").get()
        # book_code = response.xpath("//tr[1]/td/text()").get()
        # book_review = response.xpath("//tr[7]/td/text()").get()
        # available_left = re.sub(r'\D', '', book_status)
        # cleaned_status = self.clean_status(book_status)

        yield {
            'title': response.xpath("//h1/text()").get(),
            'category': response.xpath("//li[3]/a/text()").get(),
            'price(excl. tax)': response.xpath("//tr[3]/td/text()").get().replace('£',''),
            'price(incl. tax)': response.xpath("//tr[4]/td/text()").get().replace('£',''),
            'tax': response.xpath("//tr[5]/td/text()").get().replace('£',''),
            'rating': self.class_to_int(response.xpath("//div[2]/p[3]/@class").get().replace('star-rating ','')),
            'status': self.clean_status(response.xpath("//tr[6]/td/text()").get()),
            'available': re.sub(r'\D', '', response.xpath("//tr[6]/td/text()").get()), #Xóa tất cả kí tự không phải chữ số ra khỏi văn bản
            'UPC': response.xpath("//tr[1]/td/text()").get(),
            'Number of reviews': response.xpath("//tr[7]/td/text()").get(),
            'image': response.urljoin(response.xpath("//div/div/div/img/@src").get()) #Chuyển URL tương đối thành URL tuyệt đối
        }

        
    #Tách kết quả trả về của status lấy tình trạng sách còn hay hết
    def clean_status(self, book_status):
        # Sử dụng regex để trích xuất phần "in stock" và loại bỏ phần còn lại
        match = re.search(r'\bin stock\b', book_status, re.IGNORECASE)
        cleaned_status = match.group(0) if match else ""
        return cleaned_status
    
    #Chuyển rating từ chữ sang số
    def class_to_int(self, book_rating):
        if book_rating == "One":
            return "1"
        elif book_rating == "Two":
            return "2"
        elif book_rating == "Three":
            return "3"
        elif book_rating == "Four":
            return "4"
        elif book_rating == "Five":
            return "5"
        else:
            return 0 
