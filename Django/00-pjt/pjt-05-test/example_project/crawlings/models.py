from django.db import models

class Article(models.Model):
    query = models.TextField()
    title = models.TextField()



# class Article(models.Model):
#     title = models.TextField()

# # 여러개의 query로 여러 개의 게시글을 검색할 수 있음
# class Query(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#     name = models.TextField()