import kociemba
import cv2


# detects the color
def color(pixel_center):
    hue = pixel_center[0]
    saturation = pixel_center[1]

    color = None
    if saturation <= 60:
        color = 'W'
    else:
        if hue < 5:
            color = 'R'
        elif hue < 23:
            color = 'O'
        elif hue < 40:
            color = 'Y'
        elif hue < 85:
            color = 'G'
        elif hue < 135:
            color = 'B'
        else:
            color = 'R'
    
    return color

class cube:
    cube_stickers =  {
                        'up'   :[''],
                        'right':[''],
                        'front':[''],
                        'down' :[''],
                        'left' :[''],
                        'back' :['']
                        } 
    
    def getvalues(self):

        # capture --args 0, 1, ... --> no of webcam
        cap =  cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while True:
            # ret is boolean var which returns True if frame is available
            ret, frame = cap.read()

            # converting BGR color from img to hsv 
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


            # location of target pixels
            width = int(cap.get(3))
            height = int(cap.get(4))
            # mid line
            mc_x, mc_y = int(width / 2), int(height / 2)
            ml_x, ml_y  = int(mc_x - 80), int(mc_y)
            mr_x, mr_y = int(mc_x + 80), int(mc_y)

            # top line
            tc_x, tc_y = int(width / 2), int(mc_y - 70)
            tl_x, tl_y = int(tc_x - 80), int(tc_y)
            tr_x, tr_y = int(tc_x + 80), int(tc_y)

            # bottom line
            bc_x, bc_y= int(width / 2), int(mc_y + 70)
            bl_x, bl_y = int(bc_x - 80), int(bc_y)
            br_x, br_y = int(bc_x + 80), int(bc_y)


            # visual ref of target pixels
            # args -- frame, coordinates, radius, color, thickness*
            cv2.circle(frame, (ml_x, ml_y), 5, (255, 255, 255))
            cv2.circle(frame, (mc_x, mc_y), 5, (255, 255, 255))
            cv2.circle(frame, (mr_x, mr_y), 5, (255, 255, 255))

            cv2.circle(frame, (tl_x, tl_y), 5, (255, 255, 255))
            cv2.circle(frame, (tc_x, tc_y), 5, (255, 255, 255))
            cv2.circle(frame, (tr_x, tr_y), 5, (255, 255, 255))
            
            cv2.circle(frame, (bl_x, bl_y), 5, (255, 255, 255))
            cv2.circle(frame, (bc_x, bc_y), 5, (255, 255, 255))
            cv2.circle(frame, (br_x, br_y), 5, (255, 255, 255))

            
            # get value from the pixel in list/array format
            # top row
            pixel_center_tl = hsv_frame[tl_y, tl_x]
            pixel_center_tc = hsv_frame[tc_y, tc_x]
            pixel_center_tr = hsv_frame[tr_y, tr_x]
            
            # middle row
            pixel_center_ml = hsv_frame[ml_y, ml_x]
            pixel_center_mc = hsv_frame[mc_y, mc_x]
            pixel_center_mr = hsv_frame[mr_y, mr_x]

            # bottom row
            pixel_center_bl = hsv_frame[bl_y, bl_x]
            pixel_center_bc = hsv_frame[bc_y, bc_x]
            pixel_center_br = hsv_frame[br_y, br_x]

            
            # txt representation of colors detected
            # args -- frame, txt, placement, font, size, color, thickness
            cv2.putText(frame, color(pixel_center_tl), (10, 30), 0, 1, (255, 255, 255), 1)
            cv2.putText(frame, color(pixel_center_tc), (40, 30), 0, 1, (255, 255, 255), 1)
            cv2.putText(frame, color(pixel_center_tr), (70, 30), 0, 1, (255, 255, 255), 1)
            
            cv2.putText(frame, color(pixel_center_ml), (10, 60), 0, 1, (255, 255, 255), 1)
            cv2.putText(frame, color(pixel_center_mc), (40, 60), 0, 1, (255, 255, 255), 1)
            cv2.putText(frame, color(pixel_center_mr), (70, 60), 0, 1, (255, 255, 255), 1)

            cv2.putText(frame, color(pixel_center_bl), (10, 90), 0, 1, (255, 255, 255), 1)
            cv2.putText(frame, color(pixel_center_bc), (40, 90), 0, 1, (255, 255, 255), 1)
            cv2.putText(frame, color(pixel_center_br), (70, 90), 0, 1, (255, 255, 255), 1)


            # storing through all the colors at all 9 points at all time
            # when pressed a key, the colors at the time would be added to the 'cube_stickers'
            pixel_center = [pixel_center_tl, pixel_center_tc, pixel_center_tr, pixel_center_ml,pixel_center_mc, pixel_center_mr, pixel_center_bl, pixel_center_bc, pixel_center_br]
            data = []
            for index in pixel_center:
                color_name = color(index)
                data.append(color_name)
            
            cv2.imshow("Camera", frame)

            key = cv2.waitKey(5)
            if key == ord('e'):
                break
            elif key == ord('f'):
                self.cube_stickers['front'] = data
            elif key == ord('b'):
                self.cube_stickers['back'] = data
            elif key == ord('u'):
                self.cube_stickers['up'] = data
            elif key == ord('d'):
                self.cube_stickers['down'] = data
            elif key == ord('l'):
                self.cube_stickers['left'] = data
            elif key == ord('r'):
                self.cube_stickers['right'] = data

        cap.release()
        cv2.destroyAllWindows()
        

    def getans(self):
        print(self.cube_stickers)
        front_ch = self.cube_stickers['front'][4]
        back_ch = self.cube_stickers['back'][4]
        left_ch = self.cube_stickers['left'][4]
        right_ch = self.cube_stickers['right'][4]
        up_ch = self.cube_stickers['up'][4]
        down_ch = self.cube_stickers['down'][4]

        cube_str = ''

        for face in self.cube_stickers:
            for index in self.cube_stickers[face]:
                if index == front_ch:
                    cube_str += 'F'
                elif index == back_ch:
                    cube_str += 'B'
                elif index == left_ch:
                    cube_str += 'L'
                elif index == right_ch:
                    cube_str += 'R'
                elif index == up_ch:
                    cube_str += 'U'
                elif index == down_ch:
                    cube_str += 'D'
    
        return cube_str

obj = cube()

obj.getvalues()

def solve():
    raw = obj.getans()

    print(kociemba.solve(raw))
try:
    solve()
except:
    print("Wrong Input")