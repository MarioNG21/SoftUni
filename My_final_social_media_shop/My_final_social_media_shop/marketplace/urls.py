from django.urls import path

from My_final_social_media_shop.marketplace.views import ShowHome, CreateAdvertisement, MarketplaceView, \
    ProductDetailsView, AddingObjectView, EditAdvertisementView, DeleteAdvertisementView, add_view, remove_view, \
    CartView, CheckOutView, PaymentView, CategoryCreateView, CategoryEditView, CategoryDeleteView, AfterPaymentView, \
    remove_product_from_order

urlpatterns = [
    path('', ShowHome.as_view(), name='index'),

    path('create_ad/', CreateAdvertisement.as_view(), name='add advertisement'),
    path('edit_ad/<int:pk>/', EditAdvertisementView.as_view(), name='edit advertisement'),
    path('delete_ad/<int:pk>/', DeleteAdvertisementView.as_view(), name='delete advertisement'),

    path('create_category', CategoryCreateView.as_view(), name='create category'),
    path('edit_category/<int:pk>/', CategoryEditView.as_view(), name='edit category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete category'),

    path('market/', MarketplaceView.as_view(), name='marketplace'),
    path('market/<slug:slug>/', MarketplaceView.as_view(), name='marketplace category'),


    path('cart', CartView.as_view(), name='cart'),
    path('product-detail/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('click-to-add/<int:pk>/', AddingObjectView.as_view(), name='click to add object'),
    path('click-to-remove/<int:pk>/', remove_product_from_order, name='click to remove'),

    path('check-out/', CheckOutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),

    # Single add and remove
    path('add/<int:pk>/', add_view, name='add_item_to_cart'),
    path('remove/<int:pk>/', remove_view, name='remove_item_from cart'),


    path('final-stage/', AfterPaymentView.as_view(), name='after-payment')
]
