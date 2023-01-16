


# loads the user into data before processing through serializer.
def extract_data_and_assign_user(request):
    user = request.user
    data = request.data       
    data["user"] = user.id
    return data

# remove empty string fields
def remove_empty_fields(data):
    for field in list(data.keys()):
            if data[field] == '':
                del data[field]
    return data