import apriltag
import cv2

def extract_tags_from_image(image):
    # print("[INFO] reading images")
    # image = cv2.imread(image) # CAUSES BUG IF ALREADY A CV2 IMAGE
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # print("[INFO] detecting AprilTags...")
    options = apriltag.DetectorOptions(families="tag36h11") # apriltag family
    detector = apriltag.Detector(options)
    results = detector.detect(gray)
    if len(results) > 0:
        print("[INFO] {} total AprilTags detected".format(len(results)))

    process_detection_results(results, image)
    return results

def process_detection_results(results, image):
    # loop over the AprilTag detection results
    for r in results:
        # extract the bounding box (x, y)-coordinates for the AprilTag
        # and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = r.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))
        # draw the bounding box of the AprilTag detection
        cv2.line(image, ptA, ptB, (0, 255, 0), 2)
        cv2.line(image, ptB, ptC, (0, 255, 0), 2)
        cv2.line(image, ptC, ptD, (0, 255, 0), 2)
        cv2.line(image, ptD, ptA, (0, 255, 0), 2)
        # draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(r.center[0]), int(r.center[1]))
        cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
        # draw the tag family on the image
        tagFamily = r.tag_family.decode("utf-8")
        cv2.putText(image, tagFamily, (ptA[0], ptA[1] - 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # print("[INFO] tag family: {}".format(tagFamily))
    return image

def print_results(results):
    for r in results:
        print("ID:", r.tag_id, "Center:", r.center, "Corners:\n", r.corners, "\n")

def monitor_apriltags(vid):
    ret, frame = vid.read()
    # orig = cv2.resize(frame, (640,320), interpolation = cv2.INTER_AREA)
    try:
        results = extract_tags_from_image(frame)
        if len(results) > 0:
            print_results(results)
        cv2.imshow("Image", frame)
    except:
        print("Frame skipped")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False
    return True

if __name__ == "__main__":
    # define a video capture object
    vid = cv2.VideoCapture(1)
    print("Initializing video capture...")
    streamWidth = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    while(monitor_apriltags(vid)):
        pass

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()