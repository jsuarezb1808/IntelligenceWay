from django.urls import path, include
from route import views

urlpatterns = [
    path('create/', views.CreateRoute.as_view(), name="crear_ruta"),
    path('my-routes/', views.MyRoutes.as_view(), name='my_routes'),
    path('my-routes/<int:pk>/', views.RutaDetail.as_view(), name='ruta_detail'),
    path('my-routes/favorites/', views.RutaFavoritasView.as_view(), name='ruta_favoritas'),
    path('my-routes/delete/', views.RutaEliminarView.as_view(), name='ruta_eliminar'),
    path('my-routes/delete/confirm/', views.RutaConfirmarEliminarView.as_view(), name='ruta_confirmar_eliminar'),
    path('contenido/<int:pk>/', views.ContenidoDetailView.as_view(), name='contenido_detail'),

]