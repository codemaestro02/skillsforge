from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, HttpResponse

from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

# Create your views here.
def index(request):
    return HttpResponse("I am here.")

def blog_create(request):
    if request.method == 'POST': # If the form has been submitted...
        title = request.POST['title'] # A dictionary-like object containing all given HTTP POST parameters.
        
        content = request.POST['content'] # The data passed in the "Content" section of the request (HTTP body).
        
        # Construct a Blog instance with the data received from the request:        
        blog = Blog(title=title, content=content) 
        # Save the new Blog instance into the database:
        blog.save()
        # Redirect to a URL after the successful addition of a blog entry (instead of displaying the blog entry page).
        return HttpResponseRedirect('/')
    else:
        # If the request was not a POST request, display the blank form.
        return render(request,'blog_create.html', {})      

def blog_detail(request, blog_id):    
    """A view that displays details of a single blog entry."""
    try:
        # Get the blog entry using the ID from the URL.
        # This will raise a 404 if the entry does not exist.
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        # Return a special "HTTP 404 Not Found" response.
        return HttpResponseNotFound('<p>Sorry, the blog you are looking for does not exist.</p>')
    # There is a blog with this id, so render the detail page with it.
    return render(request, 'blog_detail.html', {'blog': blog})    

def delete_blog(request, blog_id):
    """A view that deletes a specific blog entry when requested by user."""
    # First, attempt to look up the blog based on its ID.
    # If it doesn't exist, return a 404 response.
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return HttpResponseNotFound("Blog does not exist")

    # Check that the person trying to edit the blog is the owner of the blog.
    if request.user != blog.owner:          
        return HttpResponseForbidden("You do not have permission to delete this blog.")

    # Otherwise, delete the blog and go back to the main page.
    blog.delete()
    return HttpResponseRedirect("/")


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user



class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    
    def search_blog(self,query):
        qs = self.get_queryset().filter(title__icontains=query)| \
             self.get_queryset().filter(content__icontains=query)
        return list(qs)
        
    # def get(self, request, *args, **kwargs):
    #     """Support searching for entries via GET parameters."""
    #     query = request.GET.get('search','')
    #     if query:
    #         return Response(self.search_blog(query))
    #     else:
    #         return super(BlogList, self).get(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     """Create a new blog entry."""
    #     serializer = self.get_serializer(data=request.DATA)
    #     serializer.is_valid()
    #     blog = serializer.object
    #     blog.owner = request.user
    #     blog.save()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer