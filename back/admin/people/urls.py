from django.urls import path

from . import new_hire_views, views, access_views

app_name = "people"
urlpatterns = [
    path("", new_hire_views.NewHireListView.as_view(), name="new_hires"),
    path("new_hire/add/", new_hire_views.NewHireAddView.as_view(), name="new_hire_add"),
    path(
        "new_hire/<int:pk>/overview/",
        new_hire_views.NewHireSequenceView.as_view(),
        name="new_hire",
    ),
    path(
        "new_hire/<int:pk>/profile/",
        new_hire_views.NewHireProfileView.as_view(),
        name="new_hire_profile",
    ),
    path(
        "new_hire/<int:pk>/notes/",
        new_hire_views.NewHireNotesView.as_view(),
        name="new_hire_notes",
    ),
    path(
        "new_hire/<int:pk>/welcome_messages/",
        new_hire_views.NewHireWelcomeMessagesView.as_view(),
        name="new_hire_welcome_messages",
    ),
    path(
        "new_hire/<int:pk>/admin_tasks/",
        new_hire_views.NewHireAdminTasksView.as_view(),
        name="new_hire_admin_tasks",
    ),
    path(
        "new_hire/<int:pk>/forms/",
        new_hire_views.NewHireFormsView.as_view(),
        name="new_hire_forms",
    ),
    path(
        "new_hire/<int:pk>/progress/",
        new_hire_views.NewHireProgressView.as_view(),
        name="new_hire_progress",
    ),
    path(
        "new_hire/<int:pk>/remind/<str:template_type>/<int:template_pk>/",
        new_hire_views.NewHireRemindView.as_view(),
        name="new_hire_remind",
    ),
    path(
        "new_hire/<int:pk>/reopen/<str:template_type>/<int:template_pk>/",
        new_hire_views.NewHireReopenTaskView.as_view(),
        name="new_hire_reopen",
    ),
    path(
        "new_hire/<int:pk>/course_answers/<int:resource_user>/",
        new_hire_views.NewHireCourseAnswersView.as_view(),
        name="new-hire-course-answers",
    ),
    path(
        "new_hire/<int:pk>/tasks/",
        new_hire_views.NewHireTasksView.as_view(),
        name="new_hire_tasks",
    ),
    path(
        "new_hire/<int:pk>/access/",
        access_views.NewHireAccessView.as_view(),
        name="new_hire_access",
    ),
    path(
        "user/<int:pk>/check_access/<int:integration_id>/",
        access_views.UserCheckAccessView.as_view(),
        name="user_check_integration",
    ),
    path(
        "user/<int:pk>/check_access/<int:integration_id>/compact/",
        access_views.UserCheckAccessView.as_view(),
        name="user_check_integration_compact",
    ),
    path(
        "user/<int:pk>/give_access/<int:integration_id>/",
        access_views.UserGiveAccessView.as_view(),
        name="user_give_integration",
    ),
    path(
        "user/<int:pk>/toggle_access/<int:integration_id>/",
        access_views.UserToggleAccessView.as_view(),
        name="toggle_access",
    ),
    path(
        "new_hire/<int:pk>/task/<slug:type>/",
        new_hire_views.NewHireTaskListView.as_view(),
        name="new_hire_task_list",
    ),
    path(
        "new_hire/<int:pk>/task/<int:template_id>/<slug:type>/",
        new_hire_views.NewHireToggleTaskView.as_view(),
        name="toggle_new_hire_task",
    ),
    path(
        "new_hire/<int:pk>/send_login_email/",
        new_hire_views.NewHireSendLoginEmailView.as_view(),
        name="send_login_email",
    ),
    path(
        "new_hire/<int:pk>/extra_info/",
        new_hire_views.NewHireExtraInfoUpdateView.as_view(),
        name="new_hire_extra_info",
    ),
    path(
        "new_hire/<int:pk>/migrate_to_normal/",
        new_hire_views.NewHireMigrateToNormalAccountView.as_view(),
        name="migrate-to-normal",
    ),
    path(
        "new_hire/<int:pk>/add_sequence/",
        new_hire_views.NewHireAddSequenceView.as_view(),
        name="add_sequence",
    ),
    path(
        "new_hire/<int:pk>/trigger_condition/<int:condition_pk>/",
        new_hire_views.NewHireTriggerConditionView.as_view(),
        name="trigger-condition",
    ),
    path(
        "new_hire/<int:pk>/remove_sequence/<int:sequence_pk>/",
        new_hire_views.NewHireRemoveSequenceView.as_view(),
        name="remove_sequence",
    ),
    path(
        "new_hire/<int:pk>/send_preboarding_notification/",
        new_hire_views.NewHireSendPreboardingNotificationView.as_view(),
        name="send_preboarding_notification",
    ),
    path("colleagues/", views.ColleagueListView.as_view(), name="colleagues"),
    path(
        "colleagues/create/",
        views.ColleagueCreateView.as_view(),
        name="colleague_create",
    ),
    path(
        "colleagues/syncslack/",
        views.ColleagueSyncSlack.as_view(),
        name="sync-slack",
    ),
    path(
        "colleagues/<int:pk>/access/",
        access_views.ColleagueAccessView.as_view(),
        name="colleague_access",
    ),
    path(
        "colleagues/<int:pk>/connect_to_slack/",
        views.ColleagueGiveSlackAccessView.as_view(),
        name="connect-to-slack",
    ),
    path(
        "colleagues/<int:pk>/toggle_portal_access/",
        views.ColleagueTogglePortalAccessView.as_view(),
        name="toggle-portal-access",
    ),
    path("colleagues/<int:pk>/", views.ColleagueUpdateView.as_view(), name="colleague"),
    path(
        "colleagues/<int:pk>/resource/",
        views.ColleagueResourceView.as_view(),
        name="add_resource",
    ),
    path(
        "colleagues/<int:pk>/resource/<int:template_id>/",
        views.ColleagueToggleResourceView.as_view(),
        name="toggle_resource",
    ),
    path(
        "colleagues/<int:pk>/import/",
        views.ColleagueImportView.as_view(),
        name="import",
    ),
    path(
        "colleagues/<int:pk>/import/users/",
        views.ColleagueImportFetchUsersHXView.as_view(),
        name="import-users-hx",
    ),
    path(
        "colleagues/<int:pk>/delete/",
        access_views.UserDeleteView.as_view(),
        name="delete",
    ),
    path(
        "colleagues/<int:pk>/revoke/",
        access_views.UserRevokeAllAccessView.as_view(),
        name="revoke_all_access",
    ),
    path(
        "colleagues/import/ignore/",
        views.ColleagueImportIgnoreUserHXView.as_view(),
        name="import-ignore-hx",
    ),
    path(
        "colleagues/import/create/",
        views.ColleagueImportAddUsersView.as_view(),
        name="import-create",
    ),
]
