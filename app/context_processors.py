def categories(request):
    from category.models import Category
    return {'categories': Category.objects.all()}