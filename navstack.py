import aprildetect as apr
import robot as r

def is_start_signal_given():
    pass

def is_at_destination(dest_tag, img):
    '''
    Check if robot is at destination.

    :param dest_tag: apriltag id for destination tag
    :return: True if robot is at destination, False otherwise
    '''
    results = apr.extract_tags_from_image(img)
    for r in results:
        if r.tag_id == dest_tag:
            print("dest tag is in frame")
            # need more detailed implementation
            # only IF dest tag is in center of screen and within a certain rectangle (where it's roughly above the bot)
            return True
    return False

def is_at_corner(corner_tag, img):
    '''
    Check if robot is at corner.

    :param corner_tag: apriltag id for corner tag
    :return: True if robot is at corner, False otherwise
    '''
    results = apr.extract_tags_from_image(img)
    for r in results:
        if r.tag_id == corner_tag:
            print("corner tag is in frame")
            # need more detailed implementation
            # only IF corner tag is in center of screen and within a certain rectangle (where it's roughly above the bot)
            return True
    return False

def move_straight(straight_tag, vid_stream):
    '''
    Move straight.

    :param straight_tag: apriltag id for straight hallways
    '''
        

def turn_corner(corner_tag, confirm_tag):
    '''
    Turn corner.

    :param corner_tag: apriltag id for corner tag
    '''
    while confirm_tag: # is not at center idk
        r.turn_left()
    
def is_return_signal_given():
    '''
    Funky network stuff
    '''
    pass

def is_at_home(home_tag, img):
    '''
    Check if robot is at home.

    :return: True if robot is at home, False otherwise
    '''
    results = apr.extract_tags_from_image(img)
    for r in results:
        if r.tag_id == home_tag:
            print("dest tag is in frame")
            # need more detailed implementation
            # only IF dest tag is in center of screen and within a certain rectangle (where it's roughly above the bot)
            return True
    return False

def complete_delivery(straight_tag, corner_tag, confirm_one, confirm_two,
                        home_tag, dest_tag):
    '''
    Complete the delivery.

    :param straight_tag: apriltag id for straight hallways
    :param corner_tag: apriltag id for corners
    :param confirm_one: apriltag id for corner confirm tags on way to destination
    :param confirm_two: apriltag id for corner confirm tags on way back home
    :param home_tag: apriltag id for home tag (place from where robot sets off)
    :param dest_tag: apriltag id for destination tag (place to which robot delivers)
    '''
    while not is_at_destination(dest_tag):
        while not is_at_corner(corner_tag):
            move_straight(straight_tag)
        else:
            turn_corner(corner_tag, confirm_one)
    while not is_return_signal_given():
        print("waiting")
    # TURN 180 degrees
    while not is_at_home(home_tag):
        while not is_at_corner(corner_tag):
            move_straight()
        else:
            turn_corner(corner_tag, confirm_two)
    print("At home!")

if __name__ == "__main__":
    while True:
        if is_start_signal_given():
            print("Start signal given")
            complete_delivery(1, 2, 3, 4)
            print("Delivery completed")
            break