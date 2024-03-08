import instaloader
import os
 
# Get instance
loader = instaloader.Instaloader()

# # Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(loader.context, 'username')

# # Print the profile details
print("Username: ", profile.username)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Posts: ", profile.mediacount)
print("Biography: ", profile.biography)
print("Profile Image: ", profile.get_profile_pic_url())
print("External URL: ", profile.external_url)
print("IGTV Count: ", profile.igtvcount)

# Define the directory where images will be stored
target_dir = 'images'


# Download all posts of a profile (If downloading without login is prohibited by Instagram, it will ask you to login)
loader.download_profile(profile.username, fast_update=True)  #If you want to download only the profile picture, set profile_pic_only=True

#path
# Get the path where the images are stored
full_path = os.path.abspath(target_dir)
print("Images are stored in:", full_path)