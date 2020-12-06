from django.db import models


class Type_answer(models.Model):
    """Класс типа ответа"""
    name = models.CharField("Название типа", max_length=20)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name = "Тип ответа"
        verbose_name_plural = "Типы ответов"

    def __str__(self):
        return self.name


class Type_surveys(models.Model):
    """Класс типа опроса"""
    name = models.CharField("Название типа", max_length=20)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name = "Тип опроса"
        verbose_name_plural = "Типы опросов"

    def __str__(self):
        return self.name


class Questions(models.Model):
    """Класс вопросов"""
    question = models.CharField("Вопрос", max_length=300)
    type_answer = models.ForeignKey(Type_answer, verbose_name="Тип ответа", on_delete=models.CASCADE,
                                    related_name="question")
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question


class Surveys(models.Model):
    """Класс опросов"""
    name = models.CharField("Название опроса", max_length=200)
    questions = models.ManyToManyField(Questions, verbose_name="Вопрос", related_name='survey')
    type_s = models.ForeignKey(Type_surveys, verbose_name="Тип опроса", on_delete=models.CASCADE, related_name="survey")
    create = models.DateTimeField("Дата создания", auto_now=True)
    update = models.DateTimeField("Дата обновления", auto_now_add=True)
    #slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.name


class Conditions(models.Model):
    """Класс условие"""
    name = models.CharField("Условие", max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = "Условие"
        verbose_name_plural = "Условии"

    def __str__(self):
        return self.name


class Method_survey(models.Model):
    """Класс условие"""
    name = models.CharField("Условие", max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = "Метод"
        verbose_name_plural = "Методы"

    def __str__(self):
        return self.name


class Parameters(models.Model):
    """Кдасс параметров"""
    survey = models.ForeignKey(Surveys, verbose_name="Опрос", on_delete=models.CASCADE, related_name="parameter")
    method = models.ForeignKey(Method_survey, verbose_name="Метод", on_delete=models.CASCADE, related_name="parameter")
    condition = models.ManyToManyField(Conditions, verbose_name="Условие", related_name="parameter")
    deadlines_start = models.DateTimeField()
    deadlines_stop = models.DateTimeField()

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"


