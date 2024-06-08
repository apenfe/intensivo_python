def build_profile(first,last,**user_info):
    user_info['firstname'] = first
    user_info['lastname'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)