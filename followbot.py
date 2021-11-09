# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'huseyin.bt'
insta_password = 'V4l4rMorghul1S'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    potency_ratio=0.70,
                                    max_followers=11000,
                                    min_followers=50,
                                    min_following=20)
                                    
    session.set_skip_users(skip_private=False, 
                          skip_no_profile_pic=True, no_profile_pic_percentage=100, 
                          skip_business=True)
    # activities
    session.follow_user_followers(['modacelikler'], amount=30,
                                  randomize=False, sleep_delay=600,
                                  interact=False)









