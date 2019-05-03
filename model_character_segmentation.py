
import cv2


class CharSegmentation:
    def charSegments(self,contours):
        k=[]
        for obj in contours:

            area = cv2.contourArea(obj)
            if area < 50:
                # if sample is too small, probably just artifact
                continue
            x, y, w, h = cv2.boundingRect(obj)
            k.append([y + h, x, y, w, h])
        return k

    def arrange(self,k):
        k.sort()
        if len(k)==0:
            return k
        # print(k)
        ltr_width = 0
        ltr_height = 0
        for ltr in k:
            m, x, y, w, h = ltr
            ltr_width += w
            ltr_height += h
        ltr_width = ltr_width / len(k)
        ltr_height = ltr_height / len(k)
        j=1
        pm, px, py, pw, ph = k[0]
        k[0][0]=j
        for i in range(1,len(k)):
            m, x, y, w, h = k[i]
            if pm-h/2.0 <= m <= pm+h/2.0:
                k[i][0]=j

            else:
                pm, px, py, pw, ph = k[i]
                j=j+1
                k[i][0]=j

        k.sort()
        # print(k)
        return k


    def decode(self,pre):
        # pre.sort()
        # print(pre)
        if len(pre)==0:
            return pre
        pre=self.arrange(pre)
        ltr_width=0
        ltr_height=0
        for ltr in pre:
            m, x, y, w, h = ltr
            ltr_width +=w
            ltr_height+=h
        ltr_width=ltr_width/len(pre)
        ltr_height=ltr_height/len(pre)

        new=[]
        new.append(pre[0])
        x0=pre[0][1]
        y0=pre[0][0]
        for i in range(1,len(pre)):

            if (y0<pre[i][0]):
                new.append("enter")
            elif x0+ltr_width+5<pre[i][1] :
                new.append("space")
            x0=pre[i][1]
            y0=pre[i][0]
            # ltr_width=pre[i][3]
            new.append(pre[i])


        return new

    def textOrder(self,contours):
        k=self.charSegments(contours)
        new=self.decode(k)
        return new


