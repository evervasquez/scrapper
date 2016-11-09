# -*- coding: utf-8 -*-
from storemapapp.models import Ruc


class ScrapRapiPagoPipeline(object):

    def process_item(self, item, spider):
        if Ruc.objects.filter(Ruc=item['Ruc']).count() == 0:
            item.save()
        return item