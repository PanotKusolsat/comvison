import cv2
import csv
import time
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon = 0.8, maxHands = 2)
button = cv2.waitKey()


class MCQ():
    def __init__(self,data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.choice5 = data[6]
        self.answer = int(data[5])

        self.userAns = None

    def update(self, bboxs):
        for bbox in bboxs:
            x1, y1, x2, y2 = bbox
            if fingers == [0,1,0,0,0]:
                self.userAns = 1
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)
            if fingers == [0,1,1,0,0]:
                self.userAns = 2
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)
            if fingers == [0,1,1,1,0]:
                self.userAns = 3
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)
            if fingers == [0,1,1,1,1]:
                self.userAns = 4
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)
            if fingers == [1,0,0,0,0]:
                self.userAns = 5
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)

pathCSV = "testq.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))
    
print(len(mcqList))
qNo = 0
qNo2 = 0
qTotal = ((len(dataAll)))
cv2.destroyAllWindows()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if qNo<qTotal:
        mcq = mcqList[qNo2]

        
        
        if qNo2 < 7:
            img, bbox1 = cvzone.putTextRect(img,mcq.question,[100,100], 2,2, offset=50, border=5)
            img, bbox = cvzone.putTextRect(img,mcq.choice1,[100,250], 2,2, offset=50, border=5)
            img, bbox2 = cvzone.putTextRect(img,mcq.choice2,[450,250], 2,2, offset=50, border=5)
            img, bbox3 = cvzone.putTextRect(img,mcq.choice3,[100,400], 2,2, offset=50, border=5)
            img, bbox4 = cvzone.putTextRect(img,mcq.choice4,[450,400], 2,2, offset=50, border=5)
        else:
            img, bbox1 = cvzone.putTextRect(img,mcq.question,[500,100], 2,2, offset=50, border=5)
            img, bbox5 = cvzone.putTextRect(img,mcq.choice5,[500,500], 2,2, offset=50, border=5)
        
        

        if hands:
            hand1 = hands[0]
            Imlist1 = hand1["lmList"]
            bbox1 = hand1["bbox"]
            centerPoint1 = hand1["center"]
            handType1 = hand1["type"]

            fingers = detector.fingersUp(hand1)
            if qNo2 < 7:
                if fingers == [0,1,0,0,0]:
                    mcq.update([bbox])
                    if mcq.userAns is not None and mcq.userAns == mcq.answer:
                        qNo = 1
                        qNo2 += 1
                if fingers == [0,1,1,0,0]:
                    mcq.update([bbox2])
                    if mcq.userAns is not None and mcq.userAns == mcq.answer:
                        qNo = 2
                        qNo2 += 1
                if fingers == [0,1,1,1,0]:
                    mcq.update([bbox3])
                    if mcq.userAns is not None and mcq.userAns == mcq.answer:
                        qNo = 3
                        qNo2 += 1
                if fingers == [0,1,1,1,1]:
                    mcq.update([bbox4])
                    if mcq.userAns is not None and mcq.userAns == mcq.answer:
                        qNo = 4
                        qNo2 += 1
            if qNo2 == 7:
                if fingers == [1,0,0,0,0]:
                    mcq.update([bbox5])
                    if mcq.userAns is not None and mcq.userAns == mcq.answer:
                        qNo = 5
                        qNo2 += 1
                        
                
    
    #Progress Bar
    
    if qNo2 >= 7:
        barValue = 150 + (1150//qTotal)*(7)       
        cv2.rectangle(img,(150,600),(barValue,650), (0,255,0), cv2.FILLED)
    else:
        barValue = 150 + (1150//qTotal)*(qNo2)       
        cv2.rectangle(img,(150,600),(barValue,650), (0,255,0), cv2.FILLED)
    
    cv2.rectangle(img,(150,600),(1150,650), (255, 0, 255), 5)
    cv2.imshow("ImageWindow", img)
    cv2.waitKey(1)
   