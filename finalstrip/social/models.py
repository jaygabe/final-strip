from django.db import models

from authentication.models import User

class ConnectFencers(models.Model):
  student = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE, blank=True)
  coach = models.ForeignKey(User, related_name='coach', on_delete=models.CASCADE, blank=True)
  s_accepts = models.BooleanField(default=False)
  c_accepts = models.BooleanField(default=False)

  @property
  def connected(self):
    if self.s_accepts == True and self.c_accepts == True:
      return True
    else:
      return False

  @property
  def pending(self):
    if (self.s_accepts == True and self.c_accepts != True) or \
      (self.s_accepts != True and self.c_accepts == True):
      return True
    else:
      return False
  
  def __str__(self):
        
        if self.connected == True:
          return str(self.student) + " is a student of " + str(self.coach)
        else:
          return str(self.student) + " and " + str(self.coach) + " are incomplete"
