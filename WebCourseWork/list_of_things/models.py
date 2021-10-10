from django.db import models

class Category(models.Model):
    """"Категории"""
    name = models.CharField("Категории", max_length=150)
    description = models.TextField("Описание")
    url =models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Brand(models.Model):
    """Модель и Бренд"""
    name = models.CharField("Имя", max_length=100)
    parametr = models.PositiveSmallIntegerField("Параметр", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="images/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель и Бренд"
        verbose_name_plural = "Модели и Бренды"

class Razdel(models.Model):
    """Разделы"""
    name = models.CharField("Имя",max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

class Product(models.Model):
    """Штука 2"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Подпись", max_length=100, default='')
    description = models.TextField("Описание")
    image = models.ImageField("Картинка", upload_to="Things_2/")
    cost = models.PositiveIntegerField("Цена", default=0, help_text="Указывать сумму в долларах")
    brand = models.ManyToManyField(Brand, verbose_name="Название", related_name="Brand_Product")
    brand = models.ManyToManyField(Brand, verbose_name="Брэнд", related_name="Brand_name")
    razdel = models.ManyToManyField(Razdel, verbose_name="Раздел")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null = True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Штука 2"
        verbose_name_plural = "Штуки 2"

class ThingShots(models.Model):
    """Дополнительные фотографии"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="thing_shots/")
    things_2 = models.ForeignKey(Product, verbose_name="Штука Мейн", on_delete=models.CASCADE)

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Штука", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"