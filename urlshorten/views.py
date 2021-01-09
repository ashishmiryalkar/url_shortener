from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import URLShortener
from rest_framework.parsers import JSONParser
import random,string
from django.views.generic import RedirectView


class UrlShortener(APIView):
    @staticmethod
    def get_or_create_url(url):
        """
        :param url: it will check if url is already present in db, in this case it will just return short-url of this obj. else
                   it will create a new object in db.
        :return: short-url and number of clicks on that short url
        """
        try:
            url_object = URLShortener.objects.get(actual_url = url)
            current_short_url = url_object.short_url
            url_clicks = url_object.clicks_count
        except URLShortener.DoesNotExist:
            url_clicks = 0
            for i in range(10):         #generating a random new string here if there is no collision then the for loop breaks.
                current_short_url = ''.join(random.choice(string.ascii_letters) for _ in range(6+i))
                try:
                    URLShortener.objects.get(short_url=current_short_url)
                    continue
                except URLShortener.DoesNotExist:
                    URLShortener.objects.create(short_url = current_short_url,actual_url=url)
                    break
            else:     #if there is collision 10 times then it raises the following exception
                raise Exception('Cannot hash this url at this moment, Please try again later', 1)
        return (current_short_url, url_clicks)

    def post(self,request):
        """
        create or gets short url here
        :param request:
        :return: short url and number of clicks
        """
        data = JSONParser().parse(request)
        actual_url = data["actual_url"]
        host = request.META['HTTP_HOST']
        current_url,url_clicks = self.get_or_create_url(actual_url)

        return Response({'shortened_url': host+'/'+current_url, 'clicks_count':url_clicks})


class Redierect(RedirectView):
    """
        query for short url and redierect for related actual url.
    """
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        try:
            print(kwargs,kwargs["short_url"])
            url_object = URLShortener.objects.get(short_url = kwargs["short_url"])
            self.url = url_object.actual_url
            url_object.clicks_count = url_object.clicks_count+1     #increments short url click everytime the page is redierected.
            url_object.save()
        except URLShortener.DoesNotExist:
            raise Exception('Invalid URL',2)
        return super().get_redirect_url(*args, **kwargs)
