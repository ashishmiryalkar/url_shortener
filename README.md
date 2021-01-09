# url_shortener
 shorten the url

QuickStart:

    use http://65.1.29.228:8000/short-url/create/ to create short url by pasting it in the blank or typing it in the blank
    you will get short url for the above link. use that link from now on to navigate to that page.

Process:
    
    model: UrlShortener
    class URLShortener(models.Model):
        short_url = models.CharField(max_length=10)    #for storing created short url
        actual_url = models.CharField(max_length=200)   #actual url
        clicks_count = models.IntegerField(default=0)   #number of clicks on short url

    the above model is used for storing data of actual url, short url and clicks on short url for navigating to original url

    http://65.1.29.228:8000/short-url/create/ will take a url, create another short url i.e., just a string of characters these will be stored in 
    url shortener model with default clicks to 0. and the created string is returned in response which will be appended to host name.
    
    eg: for url  "https://aws.amazon.com/getting-started/hands-on/deploy-python-application/"
        created string is "SYFzEu" which are both stored in db with default clicks to 0, which is also shown in ui.

    now when shortened link {host_name}+created string which in this case http://65.1.29.228/SYFzEu can be used to navigate to the original url "https://aws.amazon.com/getting-started/hands-on/deploy-python-application/"

    short link just redierects to the original link by fetching the related actual link from the db.

    note that always a new unique str of is generated(if there is collision then it will try creating new str with new length for upto 10 times) and will thus reduce the collision. if still there is a collision then it will raise Exception(which has very low probability).

requrirements:
    
    all requirements are placed in requirements.txt file