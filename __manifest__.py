{
    'name': 'Warehouse Stock API',
'summary': 'Provides an API to access warehouse stock and inventory details',
    'description': """
Warehouse Stock API

This Odoo 16 module allows you to access warehouse stock information via a REST API. 
Features include:
- Get product stock quantities per warehouse
- Retrieve stock movements
- Integrate with external systems using API calls

Ideal for e-commerce, ERP integrations, and reporting tools.
""",
    'version': '1.0',
    'author': 'Khawla',
    'depends': ['stock', 'web'],
    'data': [],
    'controllers': ['controllers/main.py'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}