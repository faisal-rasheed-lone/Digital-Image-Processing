import cv2 as cv

cap = cv.VideoCapture("Samples/video.mp4")
_, frame1 = cap.read()
_, frame2 = cap.read()

def rescale_frame(frame, percent=50):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

while cap.isOpened():
    _, frame = cap.read()
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 1)
    _, thresh = cv.threshold(blur, 60, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=10)
    countours , _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for countour in countours:
        (x, y, w, h) = cv.boundingRect(countour)

        if cv.contourArea(countour) < 1800:
            continue

        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, "status {}".format("Movement"), (10, 20), cv.FONT_HERSHEY_SIMPLEX,
                    1, (0,0, 255), 3)

    frame1 = rescale_frame(frame1, percent=50)
    cv.imshow("My Video ", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

cap.release()
cv.destroyAllWindows()