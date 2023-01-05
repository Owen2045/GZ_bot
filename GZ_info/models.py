from django.db import models
from django.utils import timezone


class UpdateInfo(models.Model):
    info_time_str = models.CharField(max_length=20, null=True, blank=True, verbose_name='更新時間_原文')
    info_time = models.DateTimeField(null=True, blank=True, verbose_name='更新時間')
    update_info_en = models.TextField(null=True, blank=True, verbose_name='更新內容_原文')
    update_info_zh = models.TextField(null=True, blank=True, verbose_name='更新內容_翻譯')    
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='全文網址')
    is_complete = models.BooleanField(default=False, verbose_name='是否完成全文爬取')
    
    class Meta:
        verbose_name = '更新資訊表'
        indexes = [
            models.Index(fields=['info_time_str']),
            models.Index(fields=['info_time']),
            models.Index(fields=['is_complete']),
        ]
