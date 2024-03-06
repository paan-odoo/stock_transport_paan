{
    'name' : 'stock_transport',
    'depends' : ['stock_picking_batch','fleet'],
    'license' : 'LGPL-3',
    'version' : '17.0.0.0',
    'data' : [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ]
}