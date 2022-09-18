def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(f'./uploads/images/{filename}')
    return path

