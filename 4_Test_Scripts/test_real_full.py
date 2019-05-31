
import real_full
import cv2


def test_crop_image():
    im0=cv2.imread('button.png')
    shape=real_full.crop_image(im0,**{'start': (10, 10), 'end': (30, 30)})
    assert (shape - (20,20,3)).all()
    shape=real_full.crop_image(im0,**{'start': (10, 30), 'end': (50, 90)})
    assert (shape - (60,40,3)).all()


def test_write_image():
    img=cv2.imread('button.png')
    real_full.write_image(img,'button_test.png','')


def test_create_canny_edge():
    img=cv2.imread('button.png')
    canny=real_full.create_canny_edge(img)
    cv2.imwrite('button_canny.png',canny)

def test_detect_text():
    img=cv2.imread('test_image1.png')
    detected_text=real_full.detect_text(img)
    assert detected_text=="Test Text"