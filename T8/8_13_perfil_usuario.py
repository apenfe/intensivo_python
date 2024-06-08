def build_profile(first,last,**user_info):
    user_info['firstname'] = first
    user_info['lastname'] = last
    return user_info

user_profile = build_profile('adrian','peñalver',location='murcia',field='programacion',hobby='viajar')
print(user_profile)