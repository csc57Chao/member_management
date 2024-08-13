from django.test import TestCase
from .models import Member, Role, Team
from django.urls import reverse

# Create your tests here.

class MemberManagementTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name='test')
        role = Role.objects.create(name='Regular', description='can\'t delete')
        role2 = Role.objects.create(name='Admin', description='can delete')
        Member.objects.create(first_name="John", last_name="Doe", email='john@gmail.com', phone='123-444-5555', teammember=team, role=role)
        Member.objects.create(first_name="Dummy", last_name="Dummy", email='dummy@gmail.com', phone='222-444-5555', teammember=team, role=role2)


    def modelCreation(self):
        members = Member.objects.all
        self.assertEqual(len(members),2)
        regular = Member.objects.get(name='John')
        admin = Member.objects.get(name='Dummy')
        self.assertEqual(regular.role.name, 'Regular')
        self.assertEqual(admin.role.name, 'Admin')

    def test_member_list(self):
        """test to make sure the list view is correct with team members."""
        response = self.client.get("/playground/")
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No team members.")
        self.assertContains(response, "You have 2 team members.")
