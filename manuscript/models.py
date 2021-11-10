from django.db import models
from accounts.models import Author , Reviewer



class Keywords(models.Model):
    keyword = models.CharField(max_length=50,primary_key=True)

class Manuscript(models.Model):
    table =['CAREERS', 'COMPUTER SCIENCE', 'PSYCHOLOGY','ECONOMIE','HEALTH', 
            'BIOLOGY', 'CHEMISTRY','PHYSICS']
    manuscript_id = models.BigAutoField(primary_key=True)
    Title = models.TextField(max_length=100)
    Manu_abstract =models.TextField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    manuscript_category = models.TextField(max_length=200)
    #category = models.(max_length=200,choices=table)
    reviewers= models.ManyToManyField(Reviewer, blank=True)
    file = models.FileField(upload_to='manuscript/FILES/')
    keyword = models.ManyToManyField(Keywords,through='Manu_keyword')

    def __str__(self) :
        return f'{self.Title} {self.manuscript_category} {self.author}'



class Manuscript_Authors(models.Model):
    manuscript_id = models.ForeignKey(Manuscript,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()


class Manu_keyword(models.Model):
    manuscript = models.ForeignKey(Manuscript,on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keywords,on_delete=models.CASCADE)
    



class Article(Manuscript):
    article_id = models.BigAutoField(primary_key=True)
    keywords = models.TextField()
  #  editor = models.ForeignKey(Editors,on_delete=models.CASCADE)


class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    manuscript_id = models.ForeignKey(Manuscript,on_delete=models.CASCADE)
    reviewer_id = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    remarks = models.TextField()


class Category(models.Model):
    categ_id = models.BigAutoField(primary_key=True)
    Category = models.CharField(max_length=200)








