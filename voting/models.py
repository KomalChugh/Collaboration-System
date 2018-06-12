from django.db import modelsfrom django.contrib.auth.models import Userfrom django.contrib.auth.models import Group as Rolesfrom Group.models import Groupfrom Community.models import get_file_path, Community,CommunityMembership,CommunityArticles,CommunityGroups,CommunityCourses,RequestCommunityCreationfrom BasicArticle.models import Articles,ArticleViewLogs,get_file_pathfrom workflow.models import Statesfrom Course.models import Courseclass Law(models.Model):	article = models.OneToOneField(Articles,on_delete=models.CASCADE)	upvote = models.PositiveIntegerField(default=0)	downvote = models.PositiveIntegerField(default=0)	def __str__(self):		return self.article.titleclass Voting(models.Model):	article = models.ForeignKey(Articles,on_delete=models.CASCADE)	user = models.ForeignKey(User,on_delete=models.CASCADE)	upflag = models.BooleanField(default=False)	downflag = models.BooleanField(default=False)    	def __str__(self):		return self.article.title + "-" + self.user.username