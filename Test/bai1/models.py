from django.db import models
class Publisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(
        max_length=50,
        help_text="The name of the Publisher.")
    website = models.URLField(
        help_text="The Publisher's website.")
    email = models.EmailField(
        help_text="The Publisher's email address.")
    def __str__(self):
        return self.name
# Create your models here.
class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor, co
author."""
    first_names = models.CharField(
        max_length=50,
        help_text="The contributor's first name or names.")
    last_names = models.CharField(
        max_length=50,
        help_text="The contributor's last name or names.")
    email = models.EmailField(help_text="The contact email for the contributor.")
    def __str__(self):
        return self.first_names
class Book(models.Model):
    """A published book."""
    title = models.CharField(
        max_length=70,
        help_text="The title of the book.")
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    isbn = models.CharField(
        max_length=20,
        verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        'Contributor',
        through="BookContributor")
    def __str__(self):
        return self.title


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE)
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name="The role this contributor had in the book.",
        choices = ContributionRole.choices, max_length = 20)
