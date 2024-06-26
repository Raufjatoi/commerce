from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing,name="create"),
    path('displayCategory',views.displayCategory,name='displayCategory'),
    path("listing/<int:id>", views.listing,name="listing"),
    path("removeWatchlist<int:id>",views.removeWatchlist,name="removeWatchlist"),
    path("addWatchlist<int:id>",views.addWatchlist,name="addWatchlist"),
    path("displayWatchlist", views.displayWatchlist,name="watchlist"),
    path("addcomment/<int:id>", views.addcomment,name="addComment"),
    path("addBid/<int:id>", views.addBid,name="addBid"),
    path("closeBid/<int:id>", views.closeBid,name="closeBid"),
]
