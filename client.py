from imgurpython import ImgurClient
import os
def get_img():
    client_id = 'b9ae77105014a61'
    client_secret = '720fc83b0d748eb6131f987949280e15bf3a6e66'
    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('pin')
    print("Go to the following URL: {0}".format(authorization_url))
    if os.path.isfile('pin.txt'):
        with open('pin.txt','r') as f:
            pin = f.read()
    else:
        pin = input("Enter pin code: ")
        with open('pin.txt','w') as f:
            f.write(pin)
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    # Example request
    album_id = 'ARm1Dtq'
    config = {
            'album': album_id,
            'name': 'test-name!',
            'title': 'test-title',
            'description': 'test-description'
            }
    print(client.get_album('ARm1Dtq'))
    client.upload_from_path('D:/python/linebot/linebot/in.jpg',config=config,anon=False)
    images = client.get_album_images(album_id)
    url = images[len(images)-1].link
    return url
