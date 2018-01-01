from django.conf.urls import url
from website import views

urlpatterns = [

        url(r'^$', views.home, name="index"),

        #contact us
        url(r'^contact/', views.contact, name="contact"),

        # about
        url(r'^about/vision/', views.vision, name="vision"),
         url(r'^about/success_stories/', views.success_stories, name = "success_stories"),

        # events
        url(r'^events/', views.events, name="events"),

        # associates
        url(r'^associates/associates/', views.associates, name="associates"),
        url(r'^associates/partners/', views.partners, name="partners"),
        url(r'^associates/sponsors/', views.sponsors, name="sponsors"),

        # gallery
        url(r'^gallery/', views.gallery, name="gallery"),

        # mentors
        url(r'^mentors/industry/', views.industry, name="industry"),
        url(r'^mentors/students/', views.students, name="students"),
        url(r'^mentors/faculty/', views.faculty, name="faculty"),

        # e resources
         #url(r'^e-resources/', views.e_resources, name = "e-resources"),
        # team
        url(r'^team/', views.team, name="team"),

        # gallery
        url(r'^gallery/', views.gallery, name="gallery")
]
