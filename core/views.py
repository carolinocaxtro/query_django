from django.shortcuts import render
from .models import Book, Author, Review, Profile, Tag
from django.db.models import Count
from django.db.models.functions import Length

def query_examples(request):

    autor = Author.objects.first()
    tag = Tag.objects.first()
    tag2= Tag.objects.last()
    
    books_by_author = Book.objects.filter(author__name=autor.name)
   
    books_with_tag = Book.objects.filter(tags__name=tag.name)
 
  
    authors_with_specific_bio = Author.objects.filter(bio__icontains='Ex')

    
    books_high_ratings = Book.objects.filter(reviews__rating__gte=4).distinct()


    profiles_with_specific_website = Profile.objects.filter(website='https://rocha.com/')

    books_without_reviews = Book.objects.filter(reviews__isnull=True)

    authors_by_books_count = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')


    books_long_summaries = Book.objects.annotate(summary_len=Length('summary')).filter(summary_len__gt=150)

    reviews_of_author_books = Review.objects.filter(book__author__name=autor.name)

    books_with_multiple_tags = Book.objects.filter(tags__name__in=[tag, tag2]).annotate(tag_count=Count('tags')).filter(tag_count=2)

 
    context = {
        'books_by_author': books_by_author,
        'books_with_tag': books_with_tag,
        'authors_with_specific_bio': authors_with_specific_bio,
        'books_high_ratings': books_high_ratings,
        'profiles_with_specific_website': profiles_with_specific_website,
        'books_without_reviews': books_without_reviews,
        'authors_by_books_count': authors_by_books_count,
        'books_long_summaries': books_long_summaries,
        'reviews_of_author_books': reviews_of_author_books,
        'books_with_multiple_tags': books_with_multiple_tags,
    }

    return render(request, 'core/teste1.html', context)

