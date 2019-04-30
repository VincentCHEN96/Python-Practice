import my_user, my_privileges


admin = my_privileges.Admin('Vincent', 'CHEN', 23, 'Beijing')
admin.describe_user()
admin.privileges.show_privileges()