from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField# for featured image


STATUS = ((0, "Draft"), (1, "Published"))# this is tuble for the status


class Post(models.Model):# for the posts table in the database
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)# slug field is a description containing only letters, hyphens, numbers or underscores.It is often used in url's to make them easier to read, but also to make them more search engine friendly.
    author = models.ForeignKey(# foreign key relationship one to many relation
        User, on_delete=models.CASCADE, related_name="blog_posts"# cascade deletes any feilds related to this field
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"] #

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):# comments model for database
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"