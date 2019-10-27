while True:
    import datetime
    x = datetime.datetime.now().hour
    print(x)
    y = datetime.datetime.now().minute
    print(y)
    if x == 15 and y == 45:
        print('wake up')    
        import pyglet
        music = pyglet.resource.media("sample.mp3")
        music.play()
        pyglet.app.run()

        break
    else:
        print('keep sleeping')
