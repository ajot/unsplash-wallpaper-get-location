## Python script to get Location information for downloaded Unsplash Photos/Wallpapers

I love [https://unsplash.com/](https://unsplash.com/), which in their words is a service that provides access to beautiful, free images and photos that you can download and use for any project. They’re totally royalty free, and make gorgeous desktop wallpapers. I use their Official Mac app - [https://apps.apple.com/us/app/unsplash-wallpapers/id1284863847?mt=12](https://apps.apple.com/us/app/unsplash-wallpapers/id1284863847?mt=12), which updates the Desktop Wallpaper everyday.

More often than not, I would come back to my computer in the morning, and be blown away with the wallpaper on my screen. Fortunately, the app provides a way to download these, which is pretty awesome.  The downside, however is that the downloaded files do not not include the location information.  This means that as I am cycling through these pictures later to get inspiration for the next vacation, I have no idea what part of the word that picturesque location was. It would have been great if Unsplash app included the location in the file name, or better yet, include the EXIF data as part of the downloaded file. The only way to do that would be to click on the name of the uploader to open the browser, and view the location info (when included by the uploader).

So, I set out to see if there’s a way I could write a quick script that looks at a JPG file downloaded using the Unsplash app, somehow gets the location of that photo, and then then finally rename the file to include the location?

It’s a good thing Unsplash has a pretty awesome API. It’s also helpful that the app at least includes the Photo ID as part of the downloaded file. So, all I needed the script to do was:

1. Cycle through was JPG file downloaded in a given directory
2. Get the Photo ID from the file name
3. Call the Unsplash API to get the location, and description of the photo*
4. Rename the file to include the location, and description of the photo*
5. [TODO] Update the exif data to include the location, and description of the photo

Here’s the plan I came up with

1. Hit the download button
2. Run a script once a week, that does the following -

## Get a specific Photo from Unsplash
Here’s the endpoint to get a specific photo using the Unsplash API. You need an Access Key(client ID) to use the Unsplash API. You get yours for free [here](https://unsplash.com/developers).  You would obviously also need the Photo ID. This is included in the file name downloaded by the Unsplash app. It’s something like - markus-spiske-bhaXeiBGWw4.jpg (uploader_first_name-last_name-photo_id). 

GET /photos/:id

https://api.unsplash.com/photos/PHOTO_ID/?client_id=YOUR_ACCESS_KEY

So, the file name is something along the lines of ‘markus-spiske-bhaXeiBGWw4.jpg’, where
‘bhaXeiBGWw4’ is the photo ID.

## Using the script
1. Update the access_key in config.py
2. Install dependencies
```
  pip install -r requirements.txt
```

2. Run the script
  ```python
    python3 get-photo-location.py
  ```