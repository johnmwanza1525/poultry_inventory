from django.db import models


class EntryType(models.Model):
    """
    Defines type (category) object
    """

    name = models.CharField(max_length=80)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.friendly_name.replace(' ', '-')
        super().save(*args, **kwargs)


class Entry(models.Model):
    """ Creates instance of forum entry """

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    create_date = models.DateField(auto_now_add=True)
    entry_type = models.ForeignKey(
        EntryType, on_delete=models.PROTECT, default=1, related_name="type")
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-create_date']
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def approved_responses(self):
        """
        helper method to return number of approved responses only
        """
        return self.response.filter(approved=True)

    def get_img_alt_value(self):
        """
        returns descriptive name for alt attribute on entry image
        """
        img_alt_value = self.image.name.replace('-', ' ').split('.', 1)[0]

        return img_alt_value


class Response(models.Model):
    """
    Defines model for response to forum entry
    """
    entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE, related_name='response')
    author = models.CharField(max_length=60)
    body = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f"{self.author} commented on this post"
