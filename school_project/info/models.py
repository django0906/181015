from django.db import models

__all__ = (
    'School',
    'Students',
)


class School(models.Model):
    school_name = models.CharField(max_length=16)


class Students(models.Model):
    student_school_name = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    student_name = models.CharField(max_length=10)
    friend_name_list = models.ManyToManyField('self')

    def __str__(self):
        # 이한영 (친구: a, b, c)
        #  QuerySet순회 및 문자열 포매팅
        friend_list = self.friend_name_list.all()
        friend_list_str = ', '.join([friend.student_name for friend in friend_list])
        return f'{self.student_name} (친구: {friend_list_str})'
