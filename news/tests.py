from django.test import TestCase
from .models import Editor, Article, tags
# Create your tests here.

class EditorTestClass(TestCase):


    def setUp(self):
        self.james=Editor(
                        first_name = 'James', 
                        last_name ='Muriuki',
                        email ='james@moringaschool.com')
    
    # Testing  instance
    def test_instance(self):
        # import pdb; pdb.set_trace()
        self.assertTrue(isinstance(self.james, Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_object(self):
        self.james.save_editor()
        