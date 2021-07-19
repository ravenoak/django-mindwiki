# django-mindwiki

`django-mindwiki`, or just 'MindWiki', is a Django App intended to be a Personal Wiki.

# Quick start

1. Add "mindwiki" to your INSTALLED_APPS setting like this:
   ```python
   INSTALLED_APPS = [
        ...,
        'mindwiki',
      ]
   ```

2. Include the `mindwiki` URLconf in your project urls.py like this:
   ```python
   from django.urls import include, path
   
   urlpatterns = [
        path('mindwiki/', include('mindwiki.urls')),
   ]
   ```

3. Run `python manage.py migrate` to create the mindwiki models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create and edit wiki items (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/mindwiki/ to view the MindWiki.
