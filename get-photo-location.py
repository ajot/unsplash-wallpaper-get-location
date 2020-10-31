# TODO
# 1. Get photo info from Unsplash given a photo ID
# 2. Get the location info from this information, and print it
# 3. Get the photo ID from a file
# 4. Rename the file

import requests
import glob, os
import config

# photo_id = "h_f5Bo0lYBU"
# file_name = "kyler-trautner-XwycqkgINGw"

def get_photo_info_from_unsplash(file_name):
  print_log(f"Getting stuff for {file_name}")
  photo_id = get_photo_id_from_file(file_name)
  print(f"photo_id => {photo_id[0]}")
  print(f"file_name => {file_name}")

  #Get your Unsplash Developer access key at https://unsplash.com/developers, and then update the config.py file
  api_url = (f"https://api.unsplash.com/photos/{photo_id[0]}/?client_id={config.access_key}")

  # Source: https://www.dataquest.io/blog/python-api-tutorial/
  response = requests.get(api_url)

  if (response.status_code == 200):
    #  Response was received
    json_response = response.json()
    photoLocation = json_response["location"]["title"]
    photoDescription = json_response["description"]
  else:
    print(f"Retrieval failed with {photo_id[0]}. Attempting with {photo_id[1]}")
    api_url = (f"https://api.unsplash.com/photos/{photo_id[1]}/?client_id={config.access_key}")
    print_log(f"Filename is {file_name}. Attempting to get info for the photo ID - {photo_id[0]}")
    response = requests.get(api_url)
    if (response.status_code == 200):
      #  Response was received
      json_response = response.json()
      photoLocation = json_response["location"]["title"]
      photoDescription = json_response["description"]
    else:
      # Some problem with response
      print(f"=====ERROR===== {photo_id} - not found on Unsplash")
      photoLocation = "not found"
      photoDescription = "not found"
  printLocationInfo(photoLocation,photoDescription)
  return(photoLocation,photoDescription)



def printLocationInfo(photoLocation,photoDescription):
    print(f"Location => {photoLocation}")
    print(f"Description => {photoDescription}")

def get_photo_id_from_file(file_name):
  # Based on the observation that the typical format the files downloaded from Unsplash follow this format -
  # uploader_fname-lname-photo_id.jpg or
  # uploader_name-photo_id.jpg

  # This logic of splitting the file name into an array, and then picking the last item should always get the photo_id
  arr = file_name.split("-")
  print(f"{len(arr)} arguments in the filename {arr}")
  if (len(arr) == 4) and (arr[3] != "unsplash.jpg"):
    # To handle files of the format - zetong-li-rXXSIr8-f9w.jpg
    # Some photos downloaded using the Mac app follow this format
    print("Matched Pattern 1")
    photo_id_with_extension_option_1 = arr[2] + "-" + arr[3]
    photo_id_with_extension_option_2 = photo_id_with_extension_option_1
  elif (len(arr) == 4) and (arr[3] == "unsplash.jpg"):
    # To handle files of the format - george-cox-1BX1aAQlydo-unsplash.jpg
    # Photos downloaded from Unsplash.com
    photo_id_with_extension_option_1 = arr[2]
    photo_id_with_extension_option_2 = photo_id_with_extension_option_1
  elif (len(arr) == 3):
    # To handle files of the format - kyler-trautner-XwycqkgINGw.jpg
    # Most Photos downloaded using the Mac app follow this format
    # Also handles some odd formats like - will-swann--hMgQqhiyos.jpg
    print("Matched Pattern 2")
    photo_id_with_extension_option_1 = arr[len(arr) - 1]
    photo_id_with_extension_option_2 = photo_id_with_extension_option_1
  elif (len(arr) == 6):
    # To handle files of the rare format -
    # pineapple-supply-co-t-W4_309hi8-unsplash.jpg
    print("Matched Pattern 3")
    photo_id_with_extension_option_1 = arr[3] + "-" + arr[4]

    # tanislav-rozhkov-a3-gW-qB574-unsplash.jpg - this one fails here
    photo_id_with_extension_option_2 = arr[2] + "-" + arr[3] + "-" + arr[4]
  else:
    print("No known pattern found")
    # Unknown format encountered
    photo_id_with_extension_option_1 = "unknown"
    photo_id_with_extension_option_2 = "unknown"

  print("Photo ID with extension:",photo_id_with_extension_option_1, photo_id_with_extension_option_2)
  photo_id_without_extension_option_1 = photo_id_with_extension_option_1.split(".")[0]
  photo_id_without_extension_option_2 = photo_id_with_extension_option_2.split(".")[0]
  photo_ids = [photo_id_without_extension_option_1,photo_id_without_extension_option_2]
  print("this is what's getting returned in the array")
  print(photo_ids)
  return photo_ids

def print_log(str):
  print("=" * len(str))
  print(str)
  print("=" * len(str))

def main():
  print_log("Begin")
  # Source: https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
  folder_path = "/Users/ajot/Desktop/Test"
  os.chdir(folder_path)

  for file_name in glob.glob("*.jpg"):
    #cycle through the list of photos in the current directory
    photo_info = get_photo_info_from_unsplash(file_name)
    print("Printing PHOTO INFO")
    print(photo_info)
    if photo_info[0] is None:
      new_file_name = file_name
    else:
      new_file_name = file_name + "-" + photo_info[0] + ".jpg"

    rename_file(file_name,new_file_name)

def rename_file(src, dest):
  # Source: https://www.geeksforgeeks.org/rename-multiple-files-using-python/
  folder_path = "/Users/ajot/Desktop/Test"
  os.chdir(folder_path)
  os.rename(src, dest)

main()