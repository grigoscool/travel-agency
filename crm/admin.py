from django.contrib import admin

from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('id', 'comment_text', 'comment_dt')
    readonly_fields = ('id', 'comment_dt')
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_dt', 'order_phone')
    list_display_links = ('order_name', 'id')
    search_fields = ('id', 'order_status', 'order_name', 'order_dt', 'order_phone')
    list_filter = ('order_status',)
    list_editable = ('order_status',)
    list_max_show_all = 100
    list_per_page = 10
    fields = ('id', 'order_status', 'order_name', 'order_dt', 'order_phone')
    readonly_fields = ('order_dt', 'id')

    inlines = [Comment, ]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
