from django.db import models

# Create your models here.
class users(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.TextField(max_length=256)

    def __str__(self):
        return 'id: %s ,login:%s' % (self.id, self.login)


class follow_nodes(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.TextField(max_length=256)
    modularity = models.IntegerField(default=0)
    degree = models.IntegerField(default=0)
    inDegree = models.IntegerField(default=0)
    outDegree = models.IntegerField(default=0)

    def __str__(self):
        return 'id: %s ,label:%s, modularity: %s ,degree: %s ,inDegree:%s ,outDegree: %s' % (self.id,self.label,self.modularity,self.degree,self.inDegree,self.outDegree)

    def to_dict(self):
        return {"id": self.id, "label": self.label,"modularity":self.modularity,"degree":self.degree,
                 "inDegree":self.inDegree,"outDegree":self.outDegree}

class follow_edges(models.Model):
    target = models.IntegerField('target')
    source = models.IntegerField('source')

    def __str__(self):
        return 'target: %s,source: %s' % (self.target, self.source)

    def to_dict(self):
        return {"target":self.target,"source":self.source}

    class Meta:
        unique_together = (("target", "source"),)

class Collaborate_nodes(models.Model):
    project = models.TextField('project',max_length=256)
    uid = models.IntegerField('uid')
    label = models.TextField(max_length=256)
    modularity = models.IntegerField(default=0)
    degree = models.IntegerField(default=0)
    inDegree = models.IntegerField(default=0)
    outDegree = models.IntegerField(default=0)

    def __str__(self):
        return 'project: %s ,uid: %s ,label:%s, modularity: %s ,degree: %s ,inDegree:%s ,outDegree: %s' % (self.project,self.uid,self.label,self.modularity,self.degree,self.inDegree,self.outDegree)

    def to_dict(self):
        return {"uid": self.uid, "label": self.label, "modularity": self.modularity, "degree": self.degree,
                "inDegree": self.inDegree, "outDegree": self.outDegree}

    class Meta:
        unique_together = (("project", "uid"),)

class Collaborate_edges(models.Model):
    project = models.TextField('project',max_length=256)
    target = models.IntegerField('target')
    source = models.IntegerField('source')
    weight = models.IntegerField(default=0)

    def __str__(self):
        return 'project %s,target: %s,source: %s,weight: %s' % (self.project,self.target, self.source,self.weight)

    def to_dict(self):
        return {"target": self.target, "source": self.source, "weight":self.weight}

    class Meta:
        unique_together = (("project", "target", "source"),)

class Commit_nodes(models.Model):
    project = models.TextField('project',max_length=256)
    uid = models.IntegerField('uid')
    label = models.TextField(max_length=256)
    modularity = models.IntegerField(default=0)
    degree = models.IntegerField(default=0)
    inDegree = models.IntegerField(default=0)
    outDegree = models.IntegerField(default=0)

    def __str__(self):
        return 'project: %s ,uid: %s ,label:%s, modularity: %s ,degree: %s ,inDegree:%s ,outDegree: %s' % (self.project,self.uid,self.label,self.modularity,self.degree,self.inDegree,self.outDegree)

    def to_dict(self):
        return {"uid": self.uid, "label": self.label, "modularity": self.modularity, "degree": self.degree,
                "inDegree": self.inDegree, "outDegree": self.outDegree}

    class Meta:
        unique_together = (("project", "uid"),)

class Commit_edges(models.Model):
    project = models.TextField('project',max_length=256)
    target = models.IntegerField('target')
    source = models.IntegerField('source')
    weight = models.IntegerField(default=0)

    def __str__(self):
        return 'project %s,target: %s,source: %s,weight: %s' % (self.project,self.target, self.source,self.weight)

    def to_dict(self):
        return {"target": self.target, "source": self.source, "weight":self.weight}

    class Meta:
        unique_together = (("project", "target", "source"),)
