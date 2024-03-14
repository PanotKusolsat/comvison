# import cv2
# import csv
# import time
# from cvzone.HandTrackingModule import HandDetector
# import cvzone
# import random

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
# detector = HandDetector(detectionCon = 0.8, maxHands = 2)
# button = cv2.waitKey()


# class MCQ():
#     def __init__(self,data):
#         self.question = data[0]
#         self.choice1 = data[1]
#         self.choice2 = data[2]
#         self.choice3 = data[3]
#         self.choice4 = data[4]
#         self.choice5 = data[6]
#         self.answer = int(data[5])

#         self.userAns = None

#     def update(self, bboxs):
#         for bbox in bboxs:
#             x1, y1, x2, y2 = bbox
#             if fingers == [0,1,0,0,0]:
#                 self.userAns = 1
#                 cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), cv2.FILLED)
#             if fingers == [0,1,1,0,0]:
#                 self.userAns = 2
#                 cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), cv2.FILLED)
#             if fingers == [0,1,1,1,0]:
#                 self.userAns = 3
#                 cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), cv2.FILLED)
#             if fingers == [0,1,1,1,1]:
#                 self.userAns = 4
#                 cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), cv2.FILLED)
#             if fingers == [1,0,0,0,0]:
#                 self.userAns = 5
#                 cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), cv2.FILLED)

# pathCSV = "testq.csv"
# with open(pathCSV, newline='\n') as f:
#     reader = csv.reader(f)
#     dataAll = list(reader)[1:]

# mcqList = []
# for q in dataAll:
#     mcqList.append(MCQ(q))
    
# print(len(mcqList))
# qNo = 0
# qNo2 = 0
# qNo3 = 0
# qTotal = ((len(dataAll)))
# list1 = [1, 2, 3, 4, 5, 6, 8]

# # listchoice = [mcq.]
# cv2.destroyAllWindows()

# while True:
#     success, img = cap.read()
    
#     img = cv2.flip(img, 1)
#     hands, img = detector.findHands(img, flipType=False)
    
#     if qNo<qTotal:
#         mcq = mcqList[qNo3]
#         if qNo2 < 7:
#             img, bbox1 = cvzone.putTextRect(img,mcq.question,[100,100], 2,2, offset=50, border=5)
#             img, bbox = cvzone.putTextRect(img,mcq.choice1,[100,250], 2,2, offset=50, border=5)
#             img, bbox2 = cvzone.putTextRect(img,mcq.choice2,[450,250], 2,2, offset=50, border=5)
#             img, bbox3 = cvzone.putTextRect(img,mcq.choice3,[100,400], 2,2, offset=50, border=5)
#             img, bbox4 = cvzone.putTextRect(img,mcq.choice4,[450,400], 2,2, offset=50, border=5)
#         else:
#             img, bbox1 = cvzone.putTextRect(img,mcq.question,[500,100], 2,2, offset=50, border=5)
#             img, bbox5 = cvzone.putTextRect(img,mcq.choice5,[500,500], 2,2, offset=50, border=5)
        
        

#         if hands:
#             hand1 = hands[0]
#             Imlist1 = hand1["lmList"]
#             bbox1 = hand1["bbox"]
#             centerPoint1 = hand1["center"]
#             handType1 = hand1["type"]

#             fingers = detector.fingersUp(hand1)
#             if qNo2 < 7:
#                 if fingers == [0,1,0,0,0]:
#                     mcq.update([bbox])
#                     if mcq.userAns is not None and mcq.userAns == mcq.answer:
#                         time.sleep(0.8)
#                         qNo = 1
#                         qNo2 += 1
#                         if qNo2 <= 7:
#                             qNo3 = random.choice(list1)
#                             list1.remove(qNo3)
#                             print(qNo2)
#                             print(qNo3)
#                             print(list1)
#                         else:
#                             qNo3 = 7
#                 if fingers == [0,1,1,0,0]:
#                     mcq.update([bbox2])
#                     if mcq.userAns is not None and mcq.userAns == mcq.answer:
#                         time.sleep(0.8)
#                         qNo = 2
#                         qNo2 += 1
#                         if qNo2 <= 7:
#                             qNo3 = random.choice(list1)
#                             list1.remove(qNo3)
#                             print(qNo2)
#                             print(qNo3)
#                             print(list1)
#                         else:
#                             qNo3 = 7
#                 if fingers == [0,1,1,1,0]:
#                     mcq.update([bbox3])
#                     if mcq.userAns is not None and mcq.userAns == mcq.answer:
#                         time.sleep(0.8)
#                         qNo = 3
#                         qNo2 += 1
#                         if qNo2 <= 7:
#                             qNo3 = random.choice(list1)
#                             list1.remove(qNo3)
#                             print(qNo2)
#                             print(qNo3)
#                             print(list1)
#                         else:
#                             qNo3 = 7
#                 if fingers == [0,1,1,1,1]:
#                     mcq.update([bbox4])
#                     if mcq.userAns is not None and mcq.userAns == mcq.answer:
#                         time.sleep(0.8)
#                         qNo = 4
#                         qNo2 += 1
#                         if qNo2 <= 7:
#                             qNo3 = random.choice(list1)
#                             list1.remove(qNo3)
#                             print(qNo2)
#                             print(qNo3)
#                             print(list1)
#                         else:
#                             qNo3 = 7
#             if qNo2 == 7:
#                 qNo3 = 7
#                 if fingers == [1,0,0,0,0]:
#                     mcq.update([bbox5])
#                     if mcq.userAns is not None and mcq.userAns == mcq.answer:
#                         qNo = 5
#                         qNo2 += 1
#                         mcq = mcqList[800000000000]
                        
                
    
#     #Progress Bar
    
#     if qNo2 >= 7:
#         barValue = 150 + (1150//qTotal)*(7)       
#         cv2.rectangle(img,(150,600),(barValue,650), (0,255,0), cv2.FILLED)
#         img, _ = cvzone.putTextRect(img,f'7 / 7',[1130,635], 2,2, offset=50)
#     else:
#         barValue = 150 + (1150//qTotal)*(qNo2)       
#         cv2.rectangle(img,(150,600),(barValue,650), (0,255,0), cv2.FILLED)
#         img, _ = cvzone.putTextRect(img,f'{qNo2} / 7',[1130,635], 2,2, offset=50)
    

#     cv2.rectangle(img,(150,600),(1150,650), (255, 0, 255), 5)
#     cv2.imshow("ImageWindow", img)
#     cv2.waitKey(1)
import tkinter as tk
from tkinter import messagebox
import random
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
<<<<<<< HEAD
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
=======
detector = HandDetector(detectionCon=0.8, maxHands=2)


class MCQ():
    def __init__(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operation = random.choice(['+', '-'])
        if self.operation == '+':
            self.answer = self.num1 + self.num2
        else:
            self.answer = self.num1 - self.num2
>>>>>>> dfbeaa8ee53ba6a85004c1917d8463cdc05e7519

        self.choices = [self.answer]
        while len(self.choices) < 4:
            choice = random.randint(self.answer - 5, self.answer + 5)
            if choice != self.answer and choice not in self.choices:
                self.choices.append(choice)

        random.shuffle(self.choices)
        self.userAns = None

    def update(self, bboxs):
        for bbox in bboxs:
            x1, y1, x2, y2 = bbox
            if fingers == [0, 1, 0, 0, 0]:
                self.userAns = 1

            if fingers == [0, 1, 1, 0, 0]:
                self.userAns = 2

            if fingers == [0, 1, 1, 1, 0]:
                self.userAns = 3

            if fingers == [0, 1, 1, 1, 1]:
                self.userAns = 4
<<<<<<< HEAD
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)
            if fingers == [1,0,0,0,0]:
                self.userAns = 5
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)
=======
>>>>>>> dfbeaa8ee53ba6a85004c1917d8463cdc05e7519

        if self.userAns is not None:
            if self.userAns == self.choices.index(self.answer) + 1:  # Correct answer chosen
                return True
        return False
    
    def updatecolor(self, bboxs):
        for bbox in bboxs:
            x1, y1, x2, y2 = bbox
            if fingers == [0, 1, 0, 0, 0]:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
            if fingers == [0, 1, 1, 0, 0]:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
            if fingers == [0, 1, 1, 1, 0]:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
            if fingers == [0, 1, 1, 1, 1]:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)

mcq = MCQ()
qNo = 0
<<<<<<< HEAD
qNo2 = 0
qTotal = ((len(dataAll)))
cv2.destroyAllWindows()
=======
qTotal = 10  # Total number of questions
>>>>>>> dfbeaa8ee53ba6a85004c1917d8463cdc05e7519

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

<<<<<<< HEAD
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
        
        
=======
    if qNo < qTotal:
        img, bbox1 = cvzone.putTextRect(img, f"{mcq.num1} {mcq.operation} {mcq.num2} = ?",
                                        [100, 100], 2, 2, offset=50, border=5)
        img, bbox0 = cvzone.putTextRect(img, '1) ' + str(mcq.choices[0]), [100, 250], 2, 2, offset=50, border=5)
        img, bbox2 = cvzone.putTextRect(img, '2) ' + str(mcq.choices[1]), [400, 250], 2, 2, offset=50, border=5)
        img, bbox3 = cvzone.putTextRect(img, '3) ' + str(mcq.choices[2]), [100, 400], 2, 2, offset=50, border=5)
        img, bbox4 = cvzone.putTextRect(img, '4) ' + str(mcq.choices[3]), [400, 400], 2, 2, offset=50, border=5)
>>>>>>> dfbeaa8ee53ba6a85004c1917d8463cdc05e7519

        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]
            bbox1 = hand1["bbox"]
            centerPoint1 = hand1["center"]
            handType1 = hand1["type"]

            fingers = detector.fingersUp(hand1)
<<<<<<< HEAD
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
   
=======

            if fingers == [0,1,0,0,0]:
                mcq.updatecolor([bbox0])
                
            if fingers == [0,1,1,0,0]:
                mcq.updatecolor([bbox2])
                
            if fingers == [0,1,1,1,0]:
                mcq.updatecolor([bbox3])
    
            if fingers == [0,1,1,1,1]:
                mcq.updatecolor([bbox4])

            if mcq.update([bbox1, bbox2, bbox3, bbox4]):
                time.sleep(0.8)
                qNo += 1
                mcq = MCQ()

    barValue = 150 + (1005//qTotal)*(qNo)
    cv2.rectangle(img,(150,710),(barValue,650), (0,255,0), cv2.FILLED)    
    cv2.rectangle(img,(150,710),(1150,650), (255, 0, 255), 5)
    img, _ = cvzone.putTextRect(img,f'{qNo} / 10',[550,600], 2,2, offset=50)

    if qNo >= qTotal:
        cv2.putText(img, "Quiz Completed!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)  
    cv2.imshow("ImageWindow", img)
    if cv2.waitKey(1) == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
  
>>>>>>> dfbeaa8ee53ba6a85004c1917d8463cdc05e7519
