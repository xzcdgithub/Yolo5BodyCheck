import detect_api
import cv2
import torch
import time
if __name__ == '__main__':
    #ip_camera_url = 'rtsp://admin:admin@192.168.242.98:8554/live'
    ip_camera_url = 'http://admin:admin@192.168.242.98:8081/video'
    a = detect_api.DetectAPI(weights='yolov5s.pt')
    cap=cv2.VideoCapture(ip_camera_url)
    with torch.no_grad():
        while cap.isOpened():
            st_time = time.time()
            rec, img = cap.read()
            if rec:
                result, names = a.detect([img])
                img = result[0][0]  # 每一帧图片的处理结果图片
                # 每一帧图像的识别结果（可包含多个物体）
                for cls, (x1, y1, x2, y2), conf in result[0][1]:
                    print(names[cls], x1, y1, x2, y2, conf)  # 识别物体种类、左上角x坐标、左上角y轴坐标、右下角x轴坐标、右下角y轴坐标，置信度
                    '''
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0))
                    cv2.putText(img,names[cls],(x1,y1-20),cv2.FONT_HERSHEY_DUPLEX,1.5,(255,0,0))'''
                print()  # 将每一帧的结果输出分开
                cv2.imshow("video", img)

            if cv2.waitKey(1) == ord('q'):
                break
            print("eltime: {}".format(time.time()-st_timeq))
    print("quit")