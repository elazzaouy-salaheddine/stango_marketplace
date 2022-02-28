from django.shortcuts import redirect, render
from rest_framework import generics
from .serializers import CommentSerializer
from rest_framework import permissions
from product.permissions import IsOwnerOrReadOnly
from .models import Comment
from .forms import CommentForm
from product.models import Product

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


def ProductReviewsForm(request):
    p_form = CommentForm(request.POST or None)
    #obj = get_object_or_404(Product, id = pk)
    if request.method == 'POST':
        if p_form.is_valid():
            form = p_form.save(commit=False)
            form.review = Product.objects.get(id='2')
            form.save()
            return redirect('/') # Redirect back to profile page
    else:
        #u_form = UserUpdateForm(instance=request.user)
        p_form = CommentForm()

    context = {
        'add_review': p_form
    }

    return render(request, 'comments/addcomment.html', context)