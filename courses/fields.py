from typing import Any, List, Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class OrderField(models.PositiveIntegerField):
    # Додаємо анотації для аргументів конструктора
    def __init__(
        self, for_fields: Optional[List[str]] = None, *args: Any, **kwargs: Any
    ) -> None:
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    # Перевизначення __new__ з типом Any змусить лінтер ігнорувати обмеження django-stubs
    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        return super().__new__(cls)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # filter by objects with the same field values
                    # for the fields in "for_fields"
                    query = {
                        field: getattr(model_instance, field)
                        for field in self.for_fields
                    }
                    qs = qs.filter(**query)
                # get the order of the last item
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
