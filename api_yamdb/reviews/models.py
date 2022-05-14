from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField('Категория', max_length=256)
    slug = models.SlugField('Идентификатор категории',
                            max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=100)
    slug = models.SlugField('Идентификатор жанра', max_length=50, unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.TextField('Прозведение')
    year = models.IntegerField('Год издания произведения')
    description = models.TextField('Описание произведения', blank=True)
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        blank=False,
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='title',
        null=True,
        blank=False,
        verbose_name='Категория',
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,
                              verbose_name='Жанр',
                              on_delete=models.CASCADE)


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.TextField('Текст отзыва')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    score = models.PositiveIntegerField(blank=True, null=True,
                                        verbose_name='Рейтинг',)
    pub_date = models.DateTimeField(
        'Дата публикации отзыва', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField(
        'Дата публикации комментария',
        auto_now_add=True
    )
