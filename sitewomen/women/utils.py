menu = [
    {
        "title": "О сайте",
        "urlpath": "about"
    },
    {
        "title": "Добавить статью",
        "urlpath": "add_page"
    },
    {
        "title": "Обратная связь",
        "urlpath": "contact"
    },
]


class DataMixin:
    title_page = None
    extra_context = {}
    cat_selected = None
    paginate_by = 5

    def __init__(self):
        if self.title_page:
            self.extra_context["title"] = self.title_page

        if self.cat_selected is not None:
            self.extra_context["cat_selected"] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context["cat_selected"] = None
        context.update(kwargs)
        return context