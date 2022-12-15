# in this specific folder permission i want override the paermission i have already
from rest_framework import permissions


# the name of class refer the functionality i want to do
# the owner of specific order can edit or remove it
# if not owner just he can read the order
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        '''this fun. return for me a boolian
        check request(http: get ,post ,put,delete) and obj(is the record in data base)
        get -> ok show the record 
        post ,put,delete -> check if the id samw the owner -> ok you are allow ,, athor that No allow to make change on the record

        '''
        if request.method == 'GET':
            return True
        if request.user == obj.customer:
            return True
        else:
            return False
        
