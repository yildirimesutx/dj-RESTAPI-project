# Django RestFramework

Sıradan bir web framework ile bir çok işlem gerçekleştirebiliriz Ancak, browserlar ile sınırlı kalırız. Ancak, uygulama backendimizi rest api beslemeleri şeklinde yaparsak ,tek bir sunucudan, hem web sayfaları (dinamik), hem mobil aplikasyonlar yaratabiliriz. Bunun yanında, API akışlarımız olacağından, internete bağlı çalışan herhangi bir uygulama ile backendimiz arasında rahatlıkla iletişim kurabiliriz.

Normal Django versiyonunda, backendimizi yaratırken, frontend ile de uğraşmak durumundayız. Çünkü, yarattığımız model ve viewleri eş zamanlı olarak kontrol de etmeliyiz.

Ancak Django RestFramework ile, hali hazırda bir borwsable api yapısı geldiğinden, geliştiriciler için gerekli tüm html yapıları da birlikte geliyor. Bu da demek oluyor ki, çok daha kısa bir sürede çok daha hızlı yol alabiliriz.

# Serializers

* bu projede pip install django-extensions paketini kullandım.
   
   - pip install ipython(shell de jupyter notebok kullanımı sağlıyor), python manage.py shell_plus, daha interaktif özellikleri var bu shell paketinin

- JSON, XML gibi veri tiplerinin python veri türlerine dönüştürülmesine izin verir.


- Serializer oluşturmak için farklı yöntemleri bulunmaktadır.

- modeldeki fieldları olduğu gibi alıp baştan oluşturuyoruz. Bu yöntemde crud işlemleri için ek func lar tanımlıyoruz.

- bu create, update func override işlemlerinde de kullanacağız.

```html
def create(self, validated_data):
       print(validated_data) 
       return Makale.objects.create(**validated_data)

```

- validated_data ** ile çağırmamızın sebebi, dictionary olarak geldiği için ilk önce key ve value ile açıyoruz. sonra create ediyoruz.


- DateTimeField(auto_now_add=True), ilk eklemede zamanını verir,
- DateTimeField(auto_now=True)  güncellendiği zaman 

- SHELL kullanılarak devam ediliyorsa; ilgili model ve serializer import edilmeli shell içinde

```
Modelimizde bulunan veriyi SHELL komutları yardımı ile JSON veri tipine çevireceğiz;

from haberler.models import Makale
from haberler.api.serializers import MakaleSerializer
makale_instance.baslik
serializer = MakaleSerializer(makale_instance)
serializer.data
from pprint import pprint
pprint(serializer.data)
from rest_framework.renderers import JSONRenderr
from rest_framework.renderers import JSONRenderer
data
data = JSONRenderer().render(serializer.data)
data
pprint(data)
type(data)

```

- SHELL komutları yardımıyla yeni bir model oluşturuyoruz

```
import io
from rest_framework.parsers import JSONParser
data
stream = io.BytesIO(data)
stream
data = JSONParser().parse(stream)
data
serializer = MakaleSerializer(data=data)
serializer
serializer.is_valid()
serializer.validated_data
serializer.save()
Makale.objects.count()
```


# Views


- @api_view dekoratörümüz ile ilk view ve end pointumuzun (url) yaratılması - Function Based Views [list_create_api_view(request)]

- @api_view dekoratörümüz ile ikinci view ve end pointumuzun (url) yaratılması - Function Based Views [detail_api_view(request)]


