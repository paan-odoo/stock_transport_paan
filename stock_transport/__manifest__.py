{
    'name' : 'stock_transport',
    'depends' : ['web_gantt','stock_picking_batch','fleet'],
    'license' : 'LGPL-3',
    'version' : '17.0.0.0',
    'data' : [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
        'stock_transport/static/src/views/*',
        ],
    },
}