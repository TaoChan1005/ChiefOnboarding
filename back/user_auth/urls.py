from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.AuthenticateView.as_view(),
        name="login",
    ),
    path(
        "login/",
        views.PureAuthenticateView.as_view(),
        name="login_form",
    ),
    path(
        "mfa/",
        views.MFAView.as_view(),
        name="mfa",
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password/reset_request/",
        PasswordResetView.as_view(
            template_name="password_reset.html",
            email_template_name="email/reset.html",
            subject_template_name="email/reset_subject.txt",
        ),
        name="password-reset",
    ),
    path(
        "password/reset_request/done/",
        PasswordResetDoneView.as_view(
            template_name="password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "password/reset_change/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="password_change.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset_change/done/",
        PasswordResetCompleteView.as_view(
            template_name="password_change_done.html",
        ),
        name="password_reset_complete",
    ),
    path(
        "redirect/", views.LoginRedirectView.as_view(), name="logged_in_user_redirect"
    ),
    path("api/auth/oidc_login/", views.OIDCLoginView.as_view(), name="oidc_login"),
]
