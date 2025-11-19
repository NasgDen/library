from django.db import models

from users.models import User


class News(models.Model):
    """Описание полей модели - Новости"""

    title = models.CharField(max_length=150, verbose_name="Название новости", help_text="Введите название новости")
    content = models.TextField(verbose_name="Содержание новости", help_text="Введите содержание новости")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news", verbose_name="Владелец", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Documents(models.Model):
    """Описание полей модели - Образцы документов"""

    title = models.CharField(max_length=150, verbose_name="Название документа", help_text="Укажите название документа")
    link_to_doc = models.URLField(verbose_name="Ссылка на документ", help_text="Укажите ссылку на документ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class EventScenarios(models.Model):
    """Описание полей модели - Сценарии мероприятий"""

    title = models.CharField(
        max_length=150, verbose_name="Название мероприятия", help_text="Укажите названия мероприятия"
    )
    description = models.TextField(
        verbose_name="Описание мероприятия", help_text="Укажите описание сценария мероприятия"
    )
    link_url = models.URLField(
        verbose_name="Ссылка на мероприятие", help_text="Укажите ссылка на сценарий мероприятия"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сценарий мероприятия"
        verbose_name_plural = "Сценарии мероприятий"


class WorkPlan(models.Model):
    """Описание полей модели - План работ"""

    title = models.CharField(max_length=150, verbose_name="Название работы", help_text="Укажите название работы")
    description = models.TextField(verbose_name="Описание работы", help_text="Укажите описание работы")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "План работ"
        verbose_name_plural = "План работ"


class CalendarSignificantDates(models.Model):
    """Описание полей модели - Календарь знаменательных дат"""

    title = models.CharField(
        max_length=150, verbose_name="Название знаменательной дата", help_text="Укажите названия знаменательной даты"
    )
    description = models.TextField(
        verbose_name="Описание знаменательной дата", help_text="Укажите описание знаменательной дата"
    )
    link_url = models.URLField(
        verbose_name="Ссылка на знаменательную дату", help_text="Укажите ссылка на знаменательную дату"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calendar", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Календарь знаменательных дат"
        verbose_name_plural = "Календарь знаменательных дат"


class Competitions(models.Model):
    """Описание полей модели - Конкурсы"""

    title = models.CharField(max_length=150, verbose_name="Название конкурса", help_text="Укажите названия конкурса")
    description = models.TextField(verbose_name="Описание конкурса", help_text="Укажите описание конкурса")
    link_url = models.URLField(verbose_name="Ссылка на конкурс", help_text="Укажите ссылка на конкурс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="сompetitions", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Конкурс"
        verbose_name_plural = "Конкурсы"


class RegulatoryDocuments(models.Model):
    """Описание полей модели - Нормативные документы"""

    title = models.CharField(
        max_length=150,
        verbose_name="Название нормативного документа",
        help_text="Укажите название нормативного документа",
    )
    link_url = models.URLField(
        verbose_name="Ссылка на нормативный документ", help_text="Укажите ссылку на нормативный документ"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="regulatory", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Нормативный документ"
        verbose_name_plural = "Нормативные документы"


class ProfessionalPublications(models.Model):
    """Описание полей модели - Профессиональные издания"""

    title = models.CharField(
        max_length=150, verbose_name="Название публикации", help_text="Укажите название публикации"
    )
    link_url = models.URLField(verbose_name="Ссылка на публикацию", help_text="Укажите ссылку на публикацию")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publications", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Профессиональное издание"
        verbose_name_plural = "Профессиональные издания"


class HistoryLibrarianship(models.Model):
    """Описание полей модели - История библиотечного дела"""

    title = models.CharField(max_length=150, verbose_name="Название", help_text="Укажите название")
    link_url = models.URLField(
        verbose_name="Ссылка на историю библиотечного дела", help_text="Укажите ссылку на историю библиотечного дела"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="history", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "История библиотечного дела"
        verbose_name_plural = "Истории библиотечного дела"


class Certification(models.Model):
    """Описание полей модели - Аттестация"""

    title = models.CharField(
        max_length=150, verbose_name="Название аттестации", help_text="Укажите названия аттестации"
    )
    description = models.TextField(verbose_name="Описание аттестации", help_text="Укажите описание аттестации")
    link_url = models.URLField(verbose_name="Ссылка на аттестацию", help_text="Укажите ссылка на аттестацию")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certification", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аттестация"
        verbose_name_plural = "Аттестации"


class MethodicalRecommendations(models.Model):
    """Описание полей модели - Методические рекомендации"""

    title = models.CharField(
        max_length=150, verbose_name="Название методической рекомендации", help_text="Укажите названия методической рекомендации"
    )
    description = models.TextField(
        verbose_name="Описание методической рекомендации", help_text="Укажите описание методической рекомендации"
    )
    link_url = models.URLField(
        verbose_name="Ссылка на методическую рекомендацию", help_text="Укажите ссылка на методическую рекомендацию"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_ut = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="methodical", verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Методическая рекомендации"
        verbose_name_plural = "Методические рекомендации"