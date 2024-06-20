
from django.test import TestCase
from .models import Task 

class TaskModelTestCase(TestCase):
    
    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            status='pending'
        )
    
    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.status, 'pending')
    
    def test_task_update(self):
        self.task.description = 'Updated description.'
        self.task.save()
        self.assertEqual(self.task.description, 'Updated description.')
    
    def test_task_deletion(self):
        task_id = self.task.id
        self.task.delete()
        self.assertFalse(Task.objects.filter(id=task_id).exists())

