import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
height = 350
length = 600

def distBetween(pointA, pointB, distA, distB):
    x = length * (pointA.x - pointB.x)
    y = height * (pointA.y - pointB.y)
    dist = x**2 + y**2
    dist = dist**(0.5)
    if dist > distA and dist < distB:
        return True
    return False
def distance(pointA, pointB):
    x = length * (pointA.x - pointB.x)
    y = height * (pointA.y - pointB.y)
    dist = x**2 + y**2
    dist = dist**(0.5)
    return dist

jab = False
cross = False
counter = 0
cap = cv2.VideoCapture(0)
while cap.isOpened():
    # read frame
    _, frame = cap.read()
    try:
         # resize the frame for portrait video
         # frame = cv2.resize(frame, (350, 600))
         # convert to RGB
         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
         # process the frame for pose detection
         pose_results = pose.process(frame_rgb)
         R_shoul = pose_results.pose_landmarks.landmark[12]
         L_shoul = pose_results.pose_landmarks.landmark[11]
         R_wrist = pose_results.pose_landmarks.landmark[16]
         L_wrist = pose_results.pose_landmarks.landmark[15]
         R_elbow = pose_results.pose_landmarks.landmark[14]
         L_elbow = pose_results.pose_landmarks.landmark[13]
         R_eye = pose_results.pose_landmarks.landmark[6]
         L_eye = pose_results.pose_landmarks.landmark[3]
         R_knuck = pose_results.pose_landmarks.landmark[20]
         L_knuck = pose_results.pose_landmarks.landmark[19]

         if distBetween(L_elbow,L_shoul, 0, 40):
              jab = True
         elif jab:
              print("jab")
              jab = False
         if distBetween(R_elbow,R_shoul, 0, 40):
              cross = True
         elif cross:
              print("cross")
              cross = False
         
         pos = abs(distance(L_shoul, R_shoul) - 50) * 2

         
         counter= counter +1
         if counter%28 == 0:
              print(pos)
         
         # draw skeleton on the frame
         mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
         # display the frame
         cv2.imshow('Output', frame)
         
    except:
         break
    if cv2.waitKey(1) == ord('q'):
          break
          
cap.release()
cv2.destroyAllWindows()