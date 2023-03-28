from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Tasks


class TasksApiTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='testpass1')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass2')
        self.task1 = Tasks.objects.create(title='Тестовая задача юзера 1',
                                          description='Описание тестовой задачи юзера 1', deadline=date.today(),
                                          user=self.user1)
        self.task2 = Tasks.objects.create(title='Тестовая задача юзера 2',
                                          description='Описание тестовой задачи юзера 2', deadline=date.today(),
                                          user=self.user2)

    def test_get_tasks(self):
        """
        Ensure we can retrieve tasks
        """
        url = reverse('TaskApiList')
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        """
        Ensure we can create a new task
        """
        url = reverse('TaskApiCreate')
        self.client.force_authenticate(user=self.user1)
        data = {'title': 'Новая тестовая задача', 'description': 'описание новой тестовой задачи',
                'deadline': date.today()}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tasks.objects.count(), 3)

    def test_get_task_detail(self):
        """
        Ensure we can retrieve a task detail
        """
        url = reverse('TaskApiDetail', args=[self.task1.id])
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task1.title)

    def test_update_task(self):
        """
        Ensure we can update a task
        """
        url = reverse('TasksApiUpdate', args=[self.task1.id])
        self.client.force_authenticate(user=self.user1)
        data = {'is_done': 'True'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tasks.objects.get(id=self.task1.id).is_done, True)

    def test_delete_task(self):
        """
        Ensure we can delete a task
        """
        url = reverse('TasksApiDelete', args=[self.task1.id])
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tasks.objects.count(), 1)

    def test_create_task_with_invalid_data(self):
        """
        Ensure we can't create a new task with invalid data
        """
        url = reverse('TaskApiCreate')
        self.client.force_authenticate(user=self.user1)
        data = {'title': '', 'description': 'описания задачи без названия', 'deadline': date.today()}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tasks.objects.count(), 2)

    def test_get_nonexistent_task(self):
        """
        Ensure we get a 404 response when trying to retrieve a nonexistent task
        """
        url = reverse('TaskApiDetail', args=[999])
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_task_with_not_owner_user(self):
        """
        Ensure we can't update someone else's task
        """
        url = reverse('TasksApiUpdate', args=[self.task1.id])
        self.client.force_authenticate(user=self.user2)
        data = {'title': 'новое название задачи'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Tasks.objects.get(id=self.task1.id).title, 'Тестовая задача юзера 1')

    def test_delete_task_with_not_owner_user(self):
        """
        Ensure we can't update someone else's task
        """
        url = reverse('TasksApiDelete', args=[self.task2.id])
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Tasks.objects.count(), 2)

    def test_user_authorization(self):
        """
        Ensure we can log in
        """
        url = reverse('rest_framework:login')
        self.client = APIClient()
        response_get = self.client.get(url)
        csrftoken = response_get.cookies['csrftoken'].value
        data = {'username': 'testuser1', 'password': 'testpass1'}
        response_post = self.client.post(url, data, HTTP_X_CSRFTOKEN=csrftoken, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_200_OK)
        self.assertEqual(Tasks.objects.count(), 2)
