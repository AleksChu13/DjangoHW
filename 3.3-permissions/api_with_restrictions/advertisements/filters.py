from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    creator = filters.CharFilter(field_name='creator__id', lookup_expr="contains")
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    status = filters.CharFilter(field_name='status', lookup_expr="exact")


    class Meta:
        model = Advertisement
        fields = ["creator", "created_at", "status"]