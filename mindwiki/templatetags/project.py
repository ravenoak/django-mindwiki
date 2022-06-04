from django import template

from mindwiki.models import Project

register = template.Library()


@register.inclusion_tag('mindwiki/project_status.html')
def project_status(project: Project):
    return {'status_code': project.status}
