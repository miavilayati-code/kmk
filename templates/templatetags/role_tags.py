from django import template

register = template.Library()

@register.filter
def get_role_color(role):
    """Return color class for role badges"""
    role_colors = {
        'admin_madin': 'danger',
        'koordinator_kmk': 'warning', 
        'kepala_madin': 'info',
        'muallimat': 'success',
    }
    return role_colors.get(role, 'secondary')

@register.filter
def get_role_icon(role):
    """Return icon class for role"""
    role_icons = {
        'admin_madin': 'fa-crown',
        'koordinator_kmk': 'fa-user-tie',
        'kepala_madin': 'fa-user-shield',
        'muallimat': 'fa-chalkboard-teacher',
    }
    return role_icons.get(role, 'fa-user')
