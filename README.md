# Serializers

* bu projede pip install django-extensions paketini kullandım.
   
   - pip install ipython, python manage.py shell_plus, daha interaktif özellikleri var bu shell paketinin

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