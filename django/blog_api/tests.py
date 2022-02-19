from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post,Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class PostTests(APITestCase):
    def test_view_post(self):
        """
        Ensure we can visit all objects.
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url,format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_create_post(self):
        """
        Ensuring we can create new Post objects and view object.
        """
        #Creating data
        self.test_category = Category.objects.create(name='django') 
        self.testuser1 = User.objects.create_superuser(
            username='test_user1',password='123456789')

        #Logging in
        self.client.login(username=self.testuser1.username,password='123456789')

        data = {
            'title':'new', 'author':1,
            'excerpt':'new', 'content':'new'
        }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_post_update(self):
        

        client = APIClient()

        self.test_category =Category.objects.create(name= 'djanog')

        self.test_user1 = User.objects.create_user(
            username = 'testuser1',password = '123456789')
        self.test_user2 = User.objects.create_user(
            username = 'testuser2',password='123456789')
        
        test_post = Post.objects.create(
            category_id=1,title='Post Title', excerpt ='Post Excerpt', 
            content ='Post Content', slug='post-title', author_id=1, status='published'
        )


        client.login(username=self.test_user1.username,
                    password='123456789')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk':1})
        
        response = client.put(
            url,{
                #"id":1,
                "title":"New",
                "author":1,
                "excerpt": "New",
                "content": "New",
                "stutus":"published",
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
