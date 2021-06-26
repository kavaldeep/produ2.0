from django.db import models

# Create your models here.

class Task:
	
	def __init__(self , Description , Priority , DeadLine , State , Duration ,CreationDate , id = ""):
		self.Description = Description 
		self.Priority = Priority
		self.DeadLine = DeadLine
		self.State = State
		self.Duration = Duration
		self.CreationDate = CreationDate
		self.id = id 