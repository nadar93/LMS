from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    """ Default role are created at migration. See 'playexo/migrations/xxxx_add_role_data.py'
        If you add a new default role, do not forget to add it to the migration file. """
     
    ADMINISTRATOR = 'AD'
    TEACHER = 'TH'
    STUDENT = 'ST'
    ANTICHEAT = 'AC'
    ROLES = (
        (ADMINISTRATOR, 'Administrator'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (ANTICHEAT, 'Anticheat')
    )
    
    role = models.CharField(primary_key = True, max_length=2, choices=ROLES, null = False, default=LEARNER)
    
    def __str__(self):
        return self.role

class LMSUser(models.Model):
      
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE, null = False)
    role = models.ManyToManyField(Role, blank=True)
    
    def is_admin(self):
        return (Role.objects.get(role=Role.ADMINISTRATOR) in self.role.all() or self.user.is_staff or self.user.is_superuser)
  
    def have_role(self, role):
        return (Role.objects.get(role=role) in self.role.all())
    
    def set_role(self, role):
        if not self.have_role(role):
            self.role.add(role)
    
    def unset_role(self, role):
        if self.have_role(role):
            self.role.remove(role)

